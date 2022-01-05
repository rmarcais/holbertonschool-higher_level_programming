#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if roman_string is None:
        return None
    for char in range(len(roman_string)):
        if char != len(roman_string) - 1:
            if roman_string[char] == 'I' and roman_string[char + 1] == 'V':
                sum += 4
                char += 1
                break
            elif roman_string[char] == 'I' and roman_string[char + 1] == 'X':
                sum += 9
                char += 1
                break
        if roman_string[char] == 'I':
            sum += 1
        elif roman_string[char] == 'V':
            sum += 5
        elif roman_string[char] == 'X':
            sum += 10
        elif roman_string[char] == 'L':
            sum += 50
        elif roman_string[char] == 'C':
            sum += 100
        elif roman_string[char] == 'D':
            sum += 500
        elif roman_string[char] == 'M':
            sum += 1000
        else:
            return None
    return sum
