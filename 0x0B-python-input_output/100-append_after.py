#!/usr/bin/python3
"""100-append_after.py
- Prototype: def append_after(filename="", search_string="", new_string=""):
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file,
    after each line containing a specific string.
    """
    txt = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w", encoding="utf-8") as g:
        g.write(txt)
