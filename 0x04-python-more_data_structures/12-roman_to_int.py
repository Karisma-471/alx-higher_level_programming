#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    prev_val = 0
    total = 0

    for ch in reversed(roman_string):
        val = rom_num[ch]
        if val >= prev_val:
            total += val
        else:
            total -= val
        prev_val = val

    return total
