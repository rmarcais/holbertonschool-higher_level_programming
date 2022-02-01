#!/usr/bin/python3
"""101-stats.py
Write a script that reads stdin line by line and computes metrics.
"""


import sys
import os

for line in sys.stdin:
    print(os.stat(line))
