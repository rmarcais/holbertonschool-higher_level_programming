#!/usr/bin/python3
def roman_to_int(roman_string):
    r = roman_string
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if isinstance(roman_string, str) == 0 or r is None or r == "":
        return 0
    for i in range(len(r)):
        if r[i] not in rd:
            return 0
        if i > 0 and rd[r[i]] > rd[r[i - 1]]:
            sum += rd[r[i]] - 2 * rd[r[i - 1]]
        else:
            sum += rd[r[i]]
    return sum
