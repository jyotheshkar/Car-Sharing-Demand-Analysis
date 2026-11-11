import importlib.util
from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'scripts/inspect_database.py'
spec = importlib.util.spec_from_file_location('inspection', SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class InspectionTests(unittest.TestCase):
    def test_database_remains_identical_and_export_is_bounded(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'source.db'
            with sqlite3.connect(path) as db:
                db.execute('CREATE TABLE "odd""name" (id INTEGER, demand REAL)')
                db.executemany('INSERT INTO "odd""name" VALUES (?, ?)', [(1, 1.), (2, 2.)])
            before = path.read_bytes()
            self.assertEqual(module.inspect_database(path)['odd"name']['rows'], 2)
            output = Path(directory) / 'sample.csv'
            module.export_table(path, 'odd"name', output, limit=1)
            self.assertEqual(len(output.read_text().splitlines()), 2)
            self.assertEqual(path.read_bytes(), before)
            with self.assertRaises(FileExistsError):
                module.export_table(path, 'odd"name', output)
            with self.assertRaises(ValueError):
                module.export_table(path, 'unknown', Path(directory) / 'bad.csv')
            with self.assertRaises(sqlite3.OperationalError):
                db = module.connect_readonly(path)
                try:
                    db.execute('CREATE TABLE forbidden(id)')
                finally:
                    db.close()

    def test_missing_database_is_not_silently_created(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'absent.db'
            with self.assertRaises(FileNotFoundError):
                module.inspect_database(path)
            self.assertFalse(path.exists())

if __name__ == '__main__':
    unittest.main()
