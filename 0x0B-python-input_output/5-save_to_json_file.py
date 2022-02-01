#!/usr/bin/python3
"""5-save_to_json_file.py
- Prototype: def save_to_json_file(my_obj, filename):
- You must use the with statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object (my_obj) to a text file (filename),
    using a JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
