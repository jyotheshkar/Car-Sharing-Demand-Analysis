"""Read-only CSV quality report. Historical database transformation scripts are separate."""
import argparse
from pathlib import Path
import pandas as pd

def inspect_csv(csv_path):
    frame = pd.read_csv(csv_path)
    return {'rows': len(frame), 'duplicate_rows': int(frame.duplicated().sum()),
            'null_values': frame.isna().sum().to_dict()}

def main():
    parser = argparse.ArgumentParser(description='Report duplicate rows and missing values without modifying data.')
    parser.add_argument('csv_file', type=Path)
    args = parser.parse_args()
    result = inspect_csv(args.csv_file)
    print(f"Rows: {result['rows']}; duplicate rows: {result['duplicate_rows']}")
    print(pd.Series(result['null_values'], name='Null values'))

if __name__ == '__main__': main()
