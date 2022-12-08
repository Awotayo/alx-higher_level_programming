#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000
            }
    num = 0
    cnt = len(roman_string)

    for (id, c) in enumerate(roman_string):
        if id < cnt - 1 and roman[c] < roman[roman_string[id + 1]):
            num -= roman[c]

        else:
            num += roman[c]
    return num
