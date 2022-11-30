#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = abs(number) % 10
if number < 0:
    digits = -digits
print(f"Last digit of {number} is {digits} " , end = "")
if digits > 5:
    print("and is greater than 5")
elif digits == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
