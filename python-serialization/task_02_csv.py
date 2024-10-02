#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""

import json
import csv


def convert_csv_to_json(filename):
    """
    Takes a CSV file and writes
    the JSON data to data.json
    """

    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append(row)

        with open("data.json", "w") as jsonfile:
            json.dump(data, jsonfile)

        return True
    except (FileNotFoundError, csv.Error):
        return False
