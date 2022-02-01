#!/usr/bin/python3
"""2-append_write.py
- Prototype: def append_write(filename="", text=""):
- If the file doesn’t exist, it should be created
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module
"""


def append_write(filename="", text=""):
    """Functions that append a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        nb = f.write(text)
    return nb
