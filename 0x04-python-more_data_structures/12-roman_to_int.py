#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "DM": 900,
            "M": 1000, "IV": 4, "IX": 9, "XL": 40,
            "XC": 90, "CD": 400
            }
    num = 0

    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return (0)
        if (i != (len(roman_string) - 1) and
                roman_dict[roman_string[i]] <
                roman_dict[roman_string[i + 1]]):
            num += roman_dict[roman_string[i]] * -1
        else:
            num += roman_dict[roman_string[i]]
    return (num)
