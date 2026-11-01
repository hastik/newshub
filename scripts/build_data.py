#!/usr/bin/env python3
"""
Sestaví data.json pro Alpine.js frontend newshubu.

Čte articles/, tasks/, tags.yml (a volitelně studies/)
a zapíše jeden soubor data.json do výstupní složky spolu s index.html ze site/.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml

WHY_HEADING = "Proč je to důležité"
# Nadpis sekce „proč“ – case-insensitive, volitelné ##
WHY_HEADING_RE = re.compile(
    r"^##\s+" + re.escape(WHY_HEADING) + r"\s*$",
    re.IGNORECASE | re.MULTILINE,
)
# Jakýkoli markdown nadpis úrovně 2
H2_RE = re.compile(r"^##\s+.+$", re.MULTILINE)


def json_default(obj: Any) -> Any:
    """Serializace date/datetime do ISO řetězců."""
    if isinstance(obj, datetime):
        return obj.date().isoformat()
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def load_front_matter(file_path: Path) -> tuple[dict | None, str]:
    """Načte YAML front matter a tělo markdown souboru."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Varování: nelze číst {file_path}: {exc}", file=sys.stderr)
        return None, ""

    if not content.startswith("---"):
        return None, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content

    try:
        front_matter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        print(f"Varování: neplatný YAML ve {file_path}: {exc}", file=sys.stderr)
        return None, content

    if not isinstance(front_matter, dict):
        return None, content

    body = parts[2].lstrip("\n")
    return front_matter, body


def split_perex_and_why(body: str) -> tuple[str, str]:
    """
    Rozdělí tělo článku na perex (text před prvním ##)
    a text sekce „Proč je to důležité“.
    """
    why_match = WHY_HEADING_RE.search(body)
    if why_match:
        perex = body[: why_match.start()].strip()
        after_why = body[why_match.end() :]
        next_h2 = H2_RE.search(after_why)
        why = (after_why[: next_h2.start()] if next_h2 else after_why).strip()
        return perex, why

    # Bez sekce „proč“: perex = vše před prvním ##, why prázdný
    first_h2 = H2_RE.search(body)
    if first_h2:
        return body[: first_h2.start()].strip(), ""
    return body.strip(), ""


def serialize_value(value: Any) -> Any:
    """Převod hodnot front matter do JSON-přátelských typů."""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, list):
        return [serialize_value(v) for v in value]
    if isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    return value


def load_categories(tasks_dir: Path) -> list[dict]:
    """Načte kategorie z tasks/*.md (slug, name, active)."""
    categories: list[dict] = []
    if not tasks_dir.is_dir():
        return categories

    for task_file in sorted(tasks_dir.glob("*.md")):
        front_matter, _ = load_front_matter(task_file)
        if not front_matter or "category" not in front_matter:
            continue
        categories.append(
            {
                "slug": front_matter["category"],
                "name": front_matter.get("name", front_matter["category"]),
                "active": bool(front_matter.get("active", True)),
            }
        )

    # Stabilní pořadí podle slug
    categories.sort(key=lambda c: c["slug"])
    return categories


def load_tags(tags_file: Path) -> list[dict]:
    """
    Flatten tags.yml do seznamu {tag, description, group}.
    group = název kategorie (logistika, ai, …) nebo „cross_category“.
    """
    tags: list[dict] = []
    if not tags_file.is_file():
        return tags

    data = yaml.safe_load(tags_file.read_text(encoding="utf-8")) or {}

    for group_name, tags_list in (data.get("categories") or {}).items():
        if not isinstance(tags_list, list):
            continue
        for item in tags_list:
            if not isinstance(item, dict) or "tag" not in item:
                continue
            tags.append(
                {
                    "tag": item["tag"],
                    "description": item.get("description", ""),
                    "group": group_name,
                }
            )

    for item in data.get("cross_category") or []:
        if not isinstance(item, dict) or "tag" not in item:
            continue
        tags.append(
            {
                "tag": item["tag"],
                "description": item.get("description", ""),
                "group": "cross_category",
            }
        )

    tags.sort(key=lambda t: (t["group"], t["tag"]))
    return tags


def load_articles(articles_dir: Path, repo_root: Path) -> list[dict]:
    """Načte všechny články z articles/YYYY/MM/*.md."""
    articles: list[dict] = []
    if not articles_dir.is_dir():
        return articles

    for article_file in sorted(articles_dir.rglob("*.md")):
        front_matter, body = load_front_matter(article_file)
        if front_matter is None:
            print(f"Varování: přeskakuji {article_file} (chybí front matter)", file=sys.stderr)
            continue

        perex, why = split_perex_and_why(body)
        rel_path = article_file.relative_to(repo_root).as_posix()

        article: dict[str, Any] = {
            # Všechna pole z front matter (serializovaná)
            **{k: serialize_value(v) for k, v in front_matter.items()},
            "path": rel_path,
            "perex": perex,
            "why": why,
            "body": body,
        }
        articles.append(article)

    def sort_key(a: dict) -> tuple:
        # Nejnovější first: vyšší datum = dřív; chybějící datum na konec
        added = a.get("added") or ""
        published = a.get("published") or ""
        return (added, published)

    articles.sort(key=sort_key, reverse=True)
    return articles


def load_studies(studies_dir: Path, repo_root: Path) -> dict | None:
    """
    Volitelná sekce studies/. Neexistuje-li, vrátí None (klíč se do JSON nedá).
    Zahrnuje queue.json (pokud je) a markdown souhrny mimo queue.md.
    """
    if not studies_dir.is_dir():
        return None

    result: dict[str, Any] = {"items": []}

    queue_json = studies_dir / "queue.json"
    if queue_json.is_file():
        try:
            result["queue"] = json.loads(queue_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"Varování: neplatný studies/queue.json: {exc}", file=sys.stderr)
            result["queue"] = []

    for study_file in sorted(studies_dir.glob("*.md")):
        if study_file.name == "queue.md":
            continue
        front_matter, body = load_front_matter(study_file)
        if front_matter is None:
            continue
        perex, why = split_perex_and_why(body)
        result["items"].append(
            {
                **{k: serialize_value(v) for k, v in front_matter.items()},
                "path": study_file.relative_to(repo_root).as_posix(),
                "perex": perex,
                "why": why,
                "body": body,
            }
        )

    # Nejnovější first podle added, pak year
    def study_sort_key(s: dict) -> tuple:
        return (s.get("added") or "", str(s.get("year") or ""))

    result["items"].sort(key=study_sort_key, reverse=True)
    return result


def build_data(repo_root: Path) -> dict:
    """Sestaví celý datový objekt pro data.json."""
    data: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "categories": load_categories(repo_root / "tasks"),
        "tags": load_tags(repo_root / "tags.yml"),
        "articles": load_articles(repo_root / "articles", repo_root),
    }

    studies = load_studies(repo_root / "studies", repo_root)
    if studies is not None:
        data["studies"] = studies

    return data


def write_site(repo_root: Path, output_dir: Path, data: dict) -> None:
    """Zapíše data.json a zkopíruje site/index.html do výstupní složky."""
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    data_path = output_dir / "data.json"
    data_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, default=json_default) + "\n",
        encoding="utf-8",
    )
    print(f"  Zapsáno {data_path.relative_to(repo_root)} "
          f"({len(data['articles'])} článků, {len(data['categories'])} kategorií, "
          f"{len(data['tags'])} tagů)")

    site_index = repo_root / "site" / "index.html"
    if not site_index.is_file():
        print(f"❌ Chybí {site_index}", file=sys.stderr)
        sys.exit(1)
    shutil.copy2(site_index, output_dir / "index.html")
    print(f"  Zkopírováno site/index.html → {output_dir.name}/index.html")


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    output_dir = repo_root / "_site"

    print(f"Sestavuji data z {repo_root} → {output_dir}")
    data = build_data(repo_root)
    write_site(repo_root, output_dir, data)
    print("✅ Hotovo.")


if __name__ == "__main__":
    main()
