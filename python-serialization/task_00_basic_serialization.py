#!/usr/bin/python3
"""Basic Serialization"""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes and save data <data> in a file <filename>"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Returns a dictionary with the deserialized
    JSON data form the file <filename>
    """

    with open(filename, 'r') as f:
        json_data = json.load(f)

    return json_data
