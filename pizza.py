import argparse
from tabulate import tabulate
import csv
import sys

def read_csv_file(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        sys.exit(f"Error: File '{file_path}' not found")

def print_tabulated_data(data):
    print(tabulate(data, headers="keys", tablefmt="grid"))

def parse_command_line():
    parser = argparse.ArgumentParser(description="Print CSV data in tabular format")
    parser.add_argument("csv_file", help="Path to the CSV file")
    args = parser.parse_args()
    return args.csv_file

def main():
    csv_file_path = parse_command_line()
    data = read_csv_file(csv_file_path)
    print_tabulated_data(data)

if __name__ == "__main__":
    main()
