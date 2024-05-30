#!/usr/bin/python3
"""
mod 2
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and write the data to data.json.

    Parameters:
    csv_filename (str): The name of the input CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print("Conversion failed.")
