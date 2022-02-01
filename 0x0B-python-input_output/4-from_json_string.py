#!/usr/bin/python3
"""4-from_json_string.py
- Prototype: def from_json_string(my_str):
- You don’t need to manage exceptions if the JSON string
 doesn’t represent an object.
"""


import json


def from_json_string(my_str):
    """Function that returns an object (Python data structure)
    represented by a JSON string (my_str)."""
    return json.loads(my_str)
