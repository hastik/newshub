#!/usr/bin/env python3
"""
Validátor pro newshub články:
- Kontroluje povinná pole ve front matter
- Ověřuje, že tagy existují v tags.yml
- Ověřuje, že kategorie existuje v tasks/
- Hlásí duplicitní URL
"""

import sys
import yaml
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
    
    # Kontrola existence souborů
    if not tags_file.exists():
        print(f"❌ Soubor {tags_file} neexistuje")
        sys.exit(1)
    
    if not tasks_dir.exists():
        print(f"❌ Složka {tasks_dir} neexistuje")
        sys.exit(1)
    
    if not articles_dir.exists():
        print(f"⚠️  Složka {articles_dir} neexistuje")
        sys.exit(0)
    
    # Načtení dat
    try:
        valid_tags = load_tags_vocabulary(tags_file)
        valid_categories = load_categories(tasks_dir)
    except Exception as e:
        print(f"❌ Chyba při načítání konfigurace: {e}")
        sys.exit(1)
    
    print(f"✓ Načteno {len(valid_tags)} tagů")
    print(f"✓ Načteno {len(valid_categories)} kategorií: {', '.join(sorted(valid_categories))}")
    
    # Validace článků
    errors, warnings, urls = validate_articles(articles_dir, valid_tags, valid_categories)
    
    print(f"\n📊 Zkontrolováno {len(urls)} článků")
    
    if warnings:
        print("\n⚠️  Varování:")
        for warning in warnings:
            print(f"  • {warning}")
    
    if errors:
        print("\n❌ Nalezené chyby:")
        for error in errors:
            print(f"  • {error}")
        sys.exit(1)
    else:
        print("\n✅ Všechny články jsou validní!")
        sys.exit(0)

if __name__ == '__main__':
    main()
