#!/usr/bin/env python3
"""
将 JSON 数据迁移到 MySQL 数据库
用法: python3 scripts/migrate_to_mysql.py
"""
import json, os, glob, re, sys
import mysql.connector

# MySQL connection
DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3307,
    'database': 'history_parallel',
    'charset': 'utf8mb4',
    'unix_socket': '/tmp/mysql.sock',
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

# Read mockData.ts for regions and sources
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data')
PEOPLE_DIR = os.path.join(DATA_DIR, 'people')
EVENTS_DIR = os.path.join(DATA_DIR, 'events')

def migrate_regions(cursor):
    """Import regions from regions.ts or mockData.ts"""
    # Read regions from src/data/regions.ts
    regions_path = os.path.join(DATA_DIR, 'regions.ts')
    if not os.path.exists(regions_path):
        print("regions.ts not found, skipping regions")
        return 0
    
    with open(regions_path) as f:
        content = f.read()
    
    # Extract region objects
    region_objects = []
    # Match each region object
    for m in re.finditer(r'\{\s*id:\s*\'([^\']+)\'', content):
        start = m.start()
        # Find the matching closing brace
        depth = 0
        for i in range(start, len(content)):
            if content[i] == '{': depth += 1
            elif content[i] == '}':
                depth -= 1
                if depth == 0:
                    region_text = content[start:i+1]
                    # Parse fields
                    obj = {}
                    for field in ['id', 'name', 'nameEn', 'slug', 'parentRegionId', 'description', 'descriptionEn']:
                        m2 = re.search(rf"{field}:\s*'([^']*)'", region_text)
                        if m2 and m2.group(1):
                            # Convert camelCase to snake_case
                            db_field = re.sub(r'([A-Z])', r'_\1', field).lower()
                            obj[db_field] = m2.group(1)
                    if 'id' in obj:
                        region_objects.append(obj)
                    break
    
    count = 0
    for r in region_objects:
        try:
            cursor.execute("""
                INSERT INTO regions (id, name, name_en, slug, parent_region_id, description, description_en)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE name=VALUES(name), name_en=VALUES(name_en)
            """, (
                r.get('id', ''),
                r.get('name', ''),
                r.get('name_en'),
                r.get('slug', ''),
                r.get('parent_region_id'),
                r.get('description'),
                r.get('description_en'),
            ))
            count += 1
        except Exception as e:
            print(f"  Error inserting region {r.get('id')}: {e}")
    
    print(f"Regions: {count} imported")
    return count

def migrate_sources(cursor):
    """Import sources from mockData.ts"""
    mockdata_path = os.path.join(DATA_DIR, 'mockData.ts')
    with open(mockdata_path) as f:
        content = f.read()
    
    # Find sources array
    sources_start = content.find('// ==================== SOURCES')
    people_start = content.find('// ==================== PEOPLE')
    if sources_start == -1 or people_start == -1:
        return 0
    
    sources_section = content[sources_start:people_start]
    
    # Parse source objects
    source_objects = []
    for m in re.finditer(r"id:\s*'([^']+)'", sources_section):
        start = m.start()
        depth = 0
        for i in range(start, len(sources_section)):
            if sources_section[i] == '{': depth += 1
            elif sources_section[i] == '}':
                depth -= 1
                if depth == 0:
                    src_text = sources_section[start:i+1]
                    obj = {'id': m.group(1)}
                    for field in ['title', 'titleEn', 'author', 'url', 'publisher', 'note', 'license']:
                        m2 = re.search(rf"{field}:\s*'([^']*)'", src_text)
                        if m2:
                            db_field = 'title_en' if field == 'titleEn' else field
                            obj[db_field] = m2.group(1)
                    year_match = re.search(r'year:\s*(\d+)', src_text)
                    if year_match:
                        obj['year'] = int(year_match.group(1))
                    source_objects.append(obj)
                    break
    
    count = 0
    for s in source_objects:
        try:
            cursor.execute("""
                INSERT INTO sources (id, title, title_en, author, url, publisher, year, note, license)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE title=VALUES(title)
            """, (
                s.get('id', ''),
                s.get('title', ''),
                s.get('title_en'),
                s.get('author'),
                s.get('url'),
                s.get('publisher'),
                s.get('year'),
                s.get('note'),
                s.get('license'),
            ))
            count += 1
        except Exception as e:
            print(f"  Error inserting source {s.get('id')}: {e}")
    
    print(f"Sources: {count} imported")
    return count

def migrate_people(cursor):
    """Import people from JSON files"""
    count = 0
    batch = []
    batch_size = 1000
    
    for f in sorted(glob.glob(f'{PEOPLE_DIR}/*.json')):
        if 'biographical' in f or '_stats' in f:
            continue
        with open(f) as fh:
            data = json.load(fh)
        
        for p in data:
            pid = p.get('id', '')
            if not pid:
                continue
            
            batch.append((
                pid,
                p.get('name', ''),
                p.get('nameEn'),
                json.dumps(p.get('alternativeNames', []), ensure_ascii=False) if p.get('alternativeNames') else None,
                p.get('birthYear'),
                p.get('deathYear'),
                p.get('birthDatePrecision', 'year'),
                p.get('deathDatePrecision', 'year'),
                p.get('regionId'),
                p.get('civilizationId'),
                json.dumps(p.get('occupations', []), ensure_ascii=False) if p.get('occupations') else None,
                json.dumps(p.get('tags', []), ensure_ascii=False) if p.get('tags') else None,
                json.dumps(p.get('tagsEn', []), ensure_ascii=False) if p.get('tagsEn') else None,
                p.get('summary', ''),
                p.get('summaryEn'),
                p.get('description', ''),
                p.get('descriptionEn'),
                json.dumps(p.get('sourceIds', []), ensure_ascii=False) if p.get('sourceIds') else None,
                p.get('wikidataQid'),
                p.get('wikipediaPageId'),
                p.get('wikipediaSlug'),
                p.get('dataStatus', 'imported'),
                p.get('confidenceScore', 0.5),
                json.dumps(p.get('externalReferences', []), ensure_ascii=False) if p.get('externalReferences') else None,
                p.get('lastReviewedAt'),
                p.get('reviewedBy'),
            ))
            
            if len(batch) >= batch_size:
                _insert_people_batch(cursor, batch)
                count += len(batch)
                print(f"  People: {count} imported...")
                batch = []
    
    if batch:
        _insert_people_batch(cursor, batch)
        count += len(batch)
    
    print(f"People: {count} total imported")
    return count

def _insert_people_batch(cursor, batch):
    sql = """
        INSERT INTO people (id, name, name_en, alternative_names, birth_year, death_year,
            birth_date_precision, death_date_precision, region_id, civilization_id,
            occupations, tags, tags_en, summary, summary_en, description, description_en,
            source_ids, wikidata_qid, wikipedia_page_id, wikipedia_slug,
            data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE name=VALUES(name), summary=VALUES(summary), description=VALUES(description)
    """
    cursor.executemany(sql, batch)

def migrate_events(cursor):
    """Import events from all JSON files"""
    count = 0
    batch = []
    batch_size = 1000
    
    # Collect all event JSON files
    event_files = (
        sorted(glob.glob(f'{EVENTS_DIR}/_lifespanEvents*.json')) +
        sorted(glob.glob(f'{EVENTS_DIR}/_detailedEvents_*.json')) +
        sorted(glob.glob(f'{EVENTS_DIR}/_deepEvents_*.json'))
    )
    # Also include biographical events
    bio_file = os.path.join(PEOPLE_DIR, '_biographicalEvents.json')
    if os.path.exists(bio_file):
        event_files.append(bio_file)
    
    for f in event_files:
        try:
            with open(f) as fh:
                data = json.load(fh)
        except FileNotFoundError:
            print(f"  WARNING: File not found: {f}")
            continue
        except json.JSONDecodeError as e:
            print(f"  ERROR: Invalid JSON in {f}: {e}")
            continue
        except PermissionError as e:
            print(f"  ERROR: Permission denied reading {f}: {e}")
            continue
        except Exception as e:
            print(f"  ERROR: Unexpected error reading {f}: {type(e).__name__}: {e}")
            continue
        
        for e in data:
            eid = e.get('id', '')
            if not eid:
                continue
            
            batch.append((
                eid,
                e.get('title', ''),
                e.get('titleEn'),
                e.get('startYear'),
                e.get('endYear'),
                e.get('startDateText'),
                e.get('endDateText'),
                e.get('approximateDateText'),
                e.get('datePrecision', 'year'),
                e.get('isApproximate', False),
                e.get('regionId'),
                e.get('civilizationId'),
                e.get('placeName'),
                e.get('placeNameEn'),
                json.dumps(e.get('coordinates'), ensure_ascii=False) if e.get('coordinates') else None,
                json.dumps(e.get('personIds', []), ensure_ascii=False) if e.get('personIds') else None,
                json.dumps(e.get('tags', []), ensure_ascii=False) if e.get('tags') else None,
                json.dumps(e.get('tagsEn', []), ensure_ascii=False) if e.get('tagsEn') else None,
                e.get('importance', 2),
                e.get('summary', ''),
                e.get('summaryEn'),
                e.get('description', ''),
                e.get('descriptionEn'),
                json.dumps(e.get('sourceIds', []), ensure_ascii=False) if e.get('sourceIds') else None,
                json.dumps(e.get('relatedEventIds', []), ensure_ascii=False) if e.get('relatedEventIds') else None,
                e.get('wikidataQid'),
                e.get('wikipediaPageId'),
                e.get('wikipediaSlug'),
                e.get('dataStatus', 'published'),
                e.get('confidenceScore', 0.7),
                json.dumps(e.get('externalReferences', []), ensure_ascii=False) if e.get('externalReferences') else None,
                e.get('lastReviewedAt'),
                e.get('reviewedBy'),
            ))
            
            if len(batch) >= batch_size:
                _insert_events_batch(cursor, batch)
                count += len(batch)
                print(f"  Events: {count} imported...")
                batch = []
    
    if batch:
        _insert_events_batch(cursor, batch)
        count += len(batch)
    
    print(f"Events: {count} total imported")
    return count

def _insert_events_batch(cursor, batch):
    sql = """
        INSERT INTO events (id, title, title_en, start_year, end_year, start_date_text, end_date_text,
            approximate_date_text, date_precision, is_approximate, region_id, civilization_id,
            place_name, place_name_en, coordinates, person_ids, tags, tags_en,
            importance, summary, summary_en, description, description_en,
            source_ids, related_event_ids, wikidata_qid, wikipedia_page_id, wikipedia_slug,
            data_status, confidence_score, external_references, last_reviewed_at, reviewed_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE title=VALUES(title), summary=VALUES(summary), description=VALUES(description)
    """
    cursor.executemany(sql, batch)

def main():
    print("=" * 60)
    print("History Parallel: Migrating data to MySQL")
    print("=" * 60)
    
    conn = connect()
    cursor = conn.cursor()
    
    try:
        # 1. Regions
        print("\n[1/4] Migrating regions...")
        migrate_regions(cursor)
        conn.commit()
        
        # 2. Sources
        print("\n[2/4] Migrating sources...")
        migrate_sources(cursor)
        conn.commit()
        
        # 3. People
        print("\n[3/4] Migrating people...")
        migrate_people(cursor)
        conn.commit()
        
        # 4. Events
        print("\n[4/4] Migrating events...")
        migrate_events(cursor)
        conn.commit()
        
        # Show stats
        print("\n" + "=" * 60)
        print("Migration complete! Database stats:")
        cursor.execute("SELECT COUNT(*) FROM regions")
        print(f"  Regions: {cursor.fetchone()[0]}")
        cursor.execute("SELECT COUNT(*) FROM sources")
        print(f"  Sources: {cursor.fetchone()[0]}")
        cursor.execute("SELECT COUNT(*) FROM people")
        print(f"  People: {cursor.fetchone()[0]}")
        cursor.execute("SELECT COUNT(*) FROM events")
        print(f"  Events: {cursor.fetchone()[0]}")
        cursor.execute("SELECT data_status, COUNT(*) FROM people GROUP BY data_status")
        for row in cursor:
            print(f"  People ({row[0]}): {row[1]}")
        cursor.execute("SELECT data_status, COUNT(*) FROM events GROUP BY data_status")
        for row in cursor:
            print(f"  Events ({row[0]}): {row[1]}")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()
