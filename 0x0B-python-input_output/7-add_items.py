#!/usr/bin/python3
"""7-add_item.py
. Write a script that adds all arguments to a Python list,
 and then save them to a file:
- You must use your function save_to_json_file from 5-save_to_json_file.py
- You must use your function load_from_json_file from 6-load_from_json_file.py
- The list must be saved as a JSON representation in a file named add_item.json
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except Exception:
    my_list = []
for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, "add_item.json")
