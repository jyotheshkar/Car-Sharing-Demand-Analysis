import tempfile
import unittest
from pathlib import Path
from Testing import inspect_csv

class QualityTests(unittest.TestCase):
    def test_counts_duplicates_and_missing_without_changing_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.csv'
            path.write_text('id,demand\n1,2\n1,2\n2,\n')
            original = path.read_bytes()
            report = inspect_csv(path)
            self.assertEqual(report['rows'], 3)
            self.assertEqual(report['duplicate_rows'], 1)
            self.assertEqual(report['null_values']['demand'], 1)
            self.assertEqual(path.read_bytes(), original)
if __name__ == '__main__': unittest.main()
