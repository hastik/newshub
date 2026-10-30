#!/usr/bin/env python3
"""
Validátor pro newshub články a studie:
- Kontroluje povinná pole ve front matter
- Ověřuje, že tagy existují v tags.yml
- Ověřuje, že kategorie existuje v tasks/
- Hlásí duplicitní URL
- Validuje souhrny studií
- Kontroluje konzistenci queue.md a queue.json
"""

import sys
import yaml
import json
import re
from pathlib import Path
from collections import defaultdict

def load_yaml_front_matter(file_path):
    """Načte YAML front matter z markdown souboru."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None

def load_tags_vocabulary(tags_file):
    """Načte slovník tagů z tags.yml."""
    with open(tags_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    all_tags = set()
    
    # Kategoriální tagy
    for category, tags_list in data.get('categories', {}).items():
        for tag_item in tags_list:
            all_tags.add(tag_item['tag'])
    
    # Cross-category tagy
    for tag_item in data.get('cross_category', []):
        all_tags.add(tag_item['tag'])
    
    return all_tags

def load_categories(tasks_dir):
    """Načte seznam kategorií z tasks/*.md."""
    categories = set()
    tasks_path = Path(tasks_dir)
    
    for task_file in tasks_path.glob('*.md'):
        front_matter = load_yaml_front_matter(task_file)
        if front_matter and 'category' in front_matter:
            categories.add(front_matter['category'])
    
    return categories

def parse_queue_md(queue_md_path):
    """Parsuje queue.md a vrací seznam záznamů."""
    with open(queue_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Najít tabulku (řádky s |)
    lines = content.split('\n')
    records = []
    
    for line in lines:
        # Přeskočit řádky, které nejsou tabulkové nebo jsou hlavičky
        if not line.strip().startswith('|') or line.strip().startswith('|---|'):
            continue
        
        # Parsovat řádek tabulky
        parts = [p.strip() for p in line.split('|')]
        # Očekáváme formát: | n | status | topic | title | authors | year | venue | url | OA | reason |
        # Index 0 je prázdný (před prvním |), index -1 je prázdný (za posledním |)
        if len(parts) >= 11:
            try:
                n = int(parts[1])
                status = parts[2]
                records.append({
                    'n': n,
                    'status': status,
                    'topic': parts[3],
                    'title': parts[4],
                    'authors': parts[5],
                    'year': int(parts[6]) if parts[6].isdigit() else None,
                    'venue': parts[7],
                    'url': parts[8],
                    'open_access': parts[9],
                    'reason': parts[10]
                })
            except (ValueError, IndexError):
                # Přeskočit nevalidní řádky
                pass
    
    return records

def check_queue_consistency(studies_dir):
    """Kontroluje konzistenci queue.md a queue.json."""
    errors = []
    warnings = []
    
    queue_md_path = Path(studies_dir) / 'queue.md'
    queue_json_path = Path(studies_dir) / 'queue.json'
    
    if not queue_md_path.exists():
        warnings.append(f"{queue_md_path} neexistuje")
        return errors, warnings
    
    if not queue_json_path.exists():
        warnings.append(f"{queue_json_path} neexistuje")
        return errors, warnings
    
    # Načíst oba soubory
    try:
        md_records = parse_queue_md(queue_md_path)
    except Exception as e:
        errors.append(f"Chyba při parsování {queue_md_path}: {e}")
        return errors, warnings
    
    try:
        with open(queue_json_path, 'r', encoding='utf-8') as f:
            json_records = json.load(f)
    except Exception as e:
        errors.append(f"Chyba při parsování {queue_json_path}: {e}")
        return errors, warnings
    
    # Kontrola počtu záznamů
    if len(md_records) != len(json_records):
        errors.append(f"Rozdílný počet záznamů: queue.md má {len(md_records)}, queue.json má {len(json_records)}")
    
    # Kontrola konzistence jednotlivých záznamů
    md_by_n = {r['n']: r for r in md_records}
    json_by_n = {r['n']: r for r in json_records}
    
    all_ns = set(md_by_n.keys()) | set(json_by_n.keys())
    
    for n in sorted(all_ns):
        md_record = md_by_n.get(n)
        json_record = json_by_n.get(n)
        
        if md_record is None:
            errors.append(f"queue.json: záznam n={n} chybí v queue.md")
            continue
        
        if json_record is None:
            errors.append(f"queue.md: záznam n={n} chybí v queue.json")
            continue
        
        # Kontrola status
        if md_record['status'] != json_record['status']:
            errors.append(f"n={n}: rozdílný status (md: {md_record['status']}, json: {json_record['status']})")
        
        # Kontrola title
        if md_record['title'] != json_record['title']:
            errors.append(f"n={n}: rozdílný title")
        
        # Kontrola URL
        if md_record['url'] != json_record['url']:
            errors.append(f"n={n}: rozdílná URL")
    
    return errors, warnings

def validate_studies(studies_dir, valid_tags):
    """Validuje souhrny studií v studies/."""
    errors = []
    warnings = []
    
    studies_path = Path(studies_dir)
    
    if not studies_path.exists():
        return errors, warnings
    
    # Najít všechny markdown soubory kromě queue.md
    study_files = [f for f in studies_path.glob('*.md') if f.name != 'queue.md']
    
    if not study_files:
        # Není chyba, studie zatím nemusí být
        return errors, warnings
    
    for study_file in study_files:
        front_matter = load_yaml_front_matter(study_file)
        
        if front_matter is None:
            errors.append(f"{study_file}: Chybí nebo je nevalidní YAML front matter")
            continue
        
        # Kontrola povinných polí pro studie
        required_fields = ['title', 'url', 'authors', 'year', 'venue', 'added', 'category', 'tags', 'queue_n']
        for field in required_fields:
            if field not in front_matter:
                errors.append(f"{study_file}: Chybí povinné pole '{field}'")
        
        # Kontrola, že category je 'studie'
        if 'category' in front_matter and front_matter['category'] != 'studie':
            errors.append(f"{study_file}: Kategorie musí být 'studie', je '{front_matter['category']}'")
        
        # Kontrola tagů
        if 'tags' in front_matter:
            tags = front_matter['tags']
            if not isinstance(tags, list):
                errors.append(f"{study_file}: Pole 'tags' musí být seznam")
            elif len(tags) == 0:
                errors.append(f"{study_file}: Pole 'tags' je prázdné (vyžadován alespoň tag 'studie')")
            else:
                if 'studie' not in tags:
                    errors.append(f"{study_file}: Musí obsahovat tag 'studie'")
                for tag in tags:
                    if tag not in valid_tags:
                        errors.append(f"{study_file}: Neznámý tag '{tag}'")
        
        # Kontrola queue_n
        if 'queue_n' in front_matter:
            queue_n = front_matter['queue_n']
            if not isinstance(queue_n, int) or queue_n < 1:
                errors.append(f"{study_file}: 'queue_n' musí být kladné celé číslo")
    
    return errors, warnings

def validate_articles(articles_dir, valid_tags, valid_categories):
    """Validuje všechny články v articles/."""
    errors = []
    warnings = []
    urls = defaultdict(list)
    
    articles_path = Path(articles_dir)
    article_files = list(articles_path.rglob('*.md'))
    
    if not article_files:
        warnings.append("Žádné články nenalezeny")
        return errors, warnings, urls
    
    for article_file in article_files:
        front_matter = load_yaml_front_matter(article_file)
        
        if front_matter is None:
            errors.append(f"{article_file}: Chybí nebo je nevalidní YAML front matter")
            continue
        
        # Kontrola povinných polí
        required_fields = ['title', 'url', 'source', 'added', 'category', 'tags']
        for field in required_fields:
            if field not in front_matter:
                errors.append(f"{article_file}: Chybí povinné pole '{field}'")
        
        # Kontrola kategorie
        if 'category' in front_matter:
            category = front_matter['category']
            if category not in valid_categories:
                errors.append(f"{article_file}: Neznámá kategorie '{category}'")
        
        # Kontrola tagů
        if 'tags' in front_matter:
            tags = front_matter['tags']
            if not isinstance(tags, list):
                errors.append(f"{article_file}: Pole 'tags' musí být seznam")
            elif len(tags) == 0:
                errors.append(f"{article_file}: Pole 'tags' je prázdné (vyžadován alespoň jeden tag)")
            else:
                for tag in tags:
                    if tag not in valid_tags:
                        errors.append(f"{article_file}: Neznámý tag '{tag}'")
        
        # Sbírání URL pro kontrolu duplikátů
        if 'url' in front_matter:
            urls[front_matter['url']].append(str(article_file))
    
    # Kontrola duplicitních URL
    for url, files in urls.items():
        if len(files) > 1:
            errors.append(f"Duplicitní URL {url} v souborech: {', '.join(files)}")
    
    return errors, warnings, urls

def main():
    repo_root = Path(__file__).parent.parent
    tags_file = repo_root / 'tags.yml'
    tasks_dir = repo_root / 'tasks'
    articles_dir = repo_root / 'articles'
    studies_dir = repo_root / 'studies'
    
    # Kontrola existence souborů
    if not tags_file.exists():
        print(f"❌ Soubor {tags_file} neexistuje")
        sys.exit(1)
    
    if not tasks_dir.exists():
        print(f"❌ Složka {tasks_dir} neexistuje")
        sys.exit(1)
    
    if not articles_dir.exists():
        print(f"⚠️  Složka {articles_dir} neexistuje")
    
    # Načtení dat
    try:
        valid_tags = load_tags_vocabulary(tags_file)
        valid_categories = load_categories(tasks_dir)
        # Přidat 'studie' jako validní kategorii
        valid_categories.add('studie')
    except Exception as e:
        print(f"❌ Chyba při načítání konfigurace: {e}")
        sys.exit(1)
    
    print(f"✓ Načteno {len(valid_tags)} tagů")
    print(f"✓ Načteno {len(valid_categories)} kategorií: {', '.join(sorted(valid_categories))}")
    
    all_errors = []
    all_warnings = []
    
    # Validace článků
    if articles_dir.exists():
        errors, warnings, urls = validate_articles(articles_dir, valid_tags, valid_categories)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        print(f"\n📊 Zkontrolováno {len(urls)} článků")
    
    # Validace studií
    if studies_dir.exists():
        print("\n📚 Kontrola studií...")
        
        # Kontrola konzistence fronty
        queue_errors, queue_warnings = check_queue_consistency(studies_dir)
        all_errors.extend(queue_errors)
        all_warnings.extend(queue_warnings)
        
        if not queue_errors:
            print("  ✓ queue.md a queue.json jsou konzistentní")
        
        # Validace souboru souhrnu studií
        study_errors, study_warnings = validate_studies(studies_dir, valid_tags)
        all_errors.extend(study_errors)
        all_warnings.extend(study_warnings)
        
        study_files = [f for f in (studies_dir).glob('*.md') if f.name != 'queue.md']
        if study_files:
            print(f"  ✓ Zkontrolováno {len(study_files)} souhrnu studií")
    
    # Výpis varování a chyb
    if all_warnings:
        print("\n⚠️  Varování:")
        for warning in all_warnings:
            print(f"  • {warning}")
    
    if all_errors:
        print("\n❌ Nalezené chyby:")
        for error in all_errors:
            print(f"  • {error}")
        sys.exit(1)
    else:
        print("\n✅ Všechny soubory jsou validní!")
        sys.exit(0)

if __name__ == '__main__':
    main()
