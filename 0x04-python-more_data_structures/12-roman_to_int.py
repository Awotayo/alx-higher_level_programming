#!/usr/bin/python3
def roman_to_int(roman_string):
    def roman_to_int(roman_string):
        roman = {
                "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                "D": 500, "DM": 900,
                "M": 1000, "IV": 4, "IX": 9, "XL": 40,
                "XC": 90, "CD": 400
                }
        if not isinstance(roman_string, str):
            return 0
        num = 0
        digits = 0
        len = len(roman_string)
        while digits < len:
            if digits + 1 < len and roman_string[digits:digits + 2] in roman:
                : num += roman[roman_string[digits:digits + 2]]
                digits += 2
            else:
                num += roman[roman_string[digits]]
                digits += 1
        return num
