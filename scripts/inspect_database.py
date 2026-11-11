"""Inspect the supplied academic database without mutating its original tables."""
import argparse
import csv
import json
from pathlib import Path
import sqlite3

DEFAULT_DATABASE = Path(__file__).resolve().parents[1] / 'CarSharing.db'

def connect_readonly(path):
    path = Path(path).resolve(strict=True)
    return sqlite3.connect(path.as_uri() + '?mode=ro', uri=True)

def quote_identifier(value):
    return '"' + value.replace('"', '""') + '"'

def list_tables(connection):
    return [r[0] for r in connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]

def inspect_database(path=DEFAULT_DATABASE):
    connection = connect_readonly(path)
    try:
        result = {}
        for table in list_tables(connection):
            quoted = quote_identifier(table)
            result[table] = {
                'rows': connection.execute(f'SELECT COUNT(*) FROM {quoted}').fetchone()[0],
                'columns': [r[1] for r in connection.execute(f'PRAGMA table_info({quoted})')],
            }
        return result
    finally:
        connection.close()

def export_table(path, table, output, limit=10000):
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100000:
        raise ValueError('limit must be an integer between 1 and 100000')
    connection = connect_readonly(path)
    try:
        if table not in list_tables(connection):
            raise ValueError('table must be one of the inspected database tables')
        cursor = connection.execute(f'SELECT * FROM {quote_identifier(table)} LIMIT ?', (limit,))
        # Exclusive creation protects both originals and previous exports.
        with Path(output).open('x', encoding='utf-8', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow([c[0] for c in cursor.description])
            writer.writerows(cursor)
    finally:
        connection.close()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, default=DEFAULT_DATABASE)
    parser.add_argument('--table')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--limit', type=int, default=10000)
    args = parser.parse_args()
    if bool(args.table) != bool(args.output):
        parser.error('--table and --output must be supplied together')
    if args.table:
        export_table(args.database, args.table, args.output, args.limit)
    else:
        print(json.dumps(inspect_database(args.database), indent=2))

if __name__ == '__main__':
    main()
