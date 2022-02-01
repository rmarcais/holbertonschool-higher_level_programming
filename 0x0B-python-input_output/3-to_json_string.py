#!/usr/bin/python3
"""3-to_json_string.py
- Prototype: def to_json_string(my_obj):
- You don’t need to manage exceptions if the object can’t be serialized.
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(represented
    by my_obj) (string).
    """
    return json.dumps(my_obj)
