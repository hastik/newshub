# newshub

Kurátorovaná databáze důležitých novinek v oblastech logistiky, AI, ProcessWire a vývoje her. Repo slouží jako zdroj pravdy pro AI zpracování; na tomto základě budou později postavené weby a další pohledy.

**Webová stránka:** [https://hastik.github.io/newshub/](https://hastik.github.io/newshub/)

Statická webová stránka je automaticky generována při každém push do `main` větve a zobrazuje procházitelnou strukturu adresářů s vyrenderovanými články.

## Účel

Sbírka článků v češtině pro Ondřeje Hastíka – product ownera v e-commerce logistice (Notino), který se zajímá o automatizaci skladů, pokročilé AI, ProcessWire CMS a začíná s vývojem her (idle games, shootery).

Každý pátek ráno automatická AI rutina:
1. Přečte `tasks/*.md` a zjistí, jaké kategorie existují a co v nich hledat
2. Prohledá existující `articles/` a vyhne se duplikátům (stejná URL nebo stejný příběh)
3. Zapíše nové články do příslušných souborů

## Struktura

```
newshub/
├── README.md           – tento dokument
├── tags.yml            – kontrolovaný slovník štítků
├── tasks/              – definice kategorií (jeden soubor = jedna kategorie)
│   ├── logistika.md
│   ├── ai.md
│   ├── processwire.md
│   └── gamedev.md
├── articles/           – články organizované podle data přidání
│   └── YYYY/
│       └── MM/
│           └── YYYY-MM-DD-slug.md
└── scripts/
    └── check.py        – validátor (front matter, štítky, duplikáty)
```

## Kategorie (tasks)

Každá kategorie je definovaná jedním souborem v `tasks/`. **Přidání souboru = přidání kategorie, smazání souboru = odebrání kategorie.**

### Formát task souboru

```markdown
---
category: slug-kategorie
name: Lidsky čitelný název
active: true
max_items: 5
---

## Kontext
Pro koho a proč tuto kategorii sledujeme.

## Co hledat
Konkrétní témata, klíčová slova, typy obsahu.

## Co ignorovat
Co nás nezajímá, i když to může vypadat relevantně.

## Preferované zdroje
Seznam webů, blogů, kanálů, které pravidelně vydávají kvalitní obsah v kategorii.

## Doporučené štítky
Seznam tagů z `tags.yml`, které se typicky v kategorii používají.
```

- `category`: slug kategorie (lowercase, bez diakritiky, jen `a-z`, `-`)
- `name`: zobrazovaný název
- `active`: `true` / `false` – deaktivovaná kategorie se neskenovává
- `max_items`: kolik nových článků přibližně za týden

## Články

### Umístění a název souboru

Každý článek je samostatný markdown soubor v `articles/YYYY/MM/YYYY-MM-DD-slug.md`, kde datum odpovídá poli `added` (datum přidání do databáze).

### Formát článku

```markdown
---
title: Titulek článku
url: https://example.com/article
source: Název publishera (web, blog, firma)
published: 2026-10-29           # datum publikace původního článku (pokud známe)
added: 2026-10-30                # datum přidání do databáze
category: logistika              # slug kategorie z tasks/
tags:                            # pole tagů z tags.yml
  - amr
  - goods-to-person
  - studie
related_urls:                    # volitelné – související odkazy
  - https://example.com/related
follow_up_of: 2026-10-20-nejaky-clanek.md  # volitelné – navazuje na starší článek
---

Perex v jedné až dvou větách. Stručné shrnutí toho, co je v článku nového nebo důležitého.

## Proč je to důležité

Pár vět nebo odstavec vysvětlující, proč si toho všimnout – kontext, dopad, jak to souvisí s Ondřejovým zaměřením.
```

### Povinná pole front matter

- `title`
- `url`
- `source`
- `added`
- `category` (musí existovat v `tasks/`)
- `tags` (alespoň jeden tag z `tags.yml`)

### Volitelná pole

- `published` – datum publikace (pokud známe)
- `related_urls` – další odkazy spojené s tématem
- `follow_up_of` – odkaz na starší článek (relativní cesta od `articles/`)

## Štítky (tags)

Všechny tagy jsou definované v `tags.yml`. Struktura:

```yaml
categories:
  logistika:
    - tag: amr
      description: Autonomous Mobile Robots
    - tag: goods-to-person
      description: Systémy přinášející zboží k pracovníkovi
  # ...

cross_category:
  - tag: studie
    description: Vědecké studie, výzkum, benchmarky
  - tag: tutorial
    description: Návody, tutoriály
```

**Pravidla:**
- Tagy lowercase, kebab-case, bez diakritiky
- Každý tag má krátký popis (česky)
- Kategoriální tagy se typicky používají v příslušné kategorii
- Cross-category tagy lze použít v libovolné kategorii

## Deduplikace

AI rutina kontroluje duplikáty dvěma způsoby:

1. **Podle URL**: článek se stejnou URL už existuje
2. **Podle příběhu**: stejná zpráva z jiného zdroje (např. stejná tisková zpráva přebraná více weby)

Pokud jde o update starší zprávy, použít `follow_up_of` a odkázat původní článek.

## Validace

Před commitem (nebo v PR) lze spustit `python scripts/check.py`, který zkontroluje:
- Povinná pole ve front matter článků
- Tagy odpovídají slovníku v `tags.yml`
- Kategorie existuje v `tasks/`
- Duplikátní URL

GitHub Action spouští validaci na každém PR.

## Příklad workflow

1. Každý pátek AI přečte task soubory v `tasks/`
2. Pro každou aktivní kategorii najde nové články podle kritérií
3. Prohledá `articles/` a vyloučí duplikáty
4. Vytvoří nové markdown soubory s datem `added: YYYY-MM-DD`
5. Otevře PR s novými články

Manuálně lze kdykoli:
- Přidat task soubor → přidat kategorii
- Smazat task soubor → odstranit kategorii
- Nastavit `active: false` → dočasně vypnout skenování
- Přidat tag do `tags.yml` → rozšířit slovník
