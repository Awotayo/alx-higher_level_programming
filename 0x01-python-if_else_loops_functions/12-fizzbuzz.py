#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 10 == 3:
            print("Fizz ", end="")
        elif number % 10 == 5:
            print("Buzz ", end="")
        elif number % 15 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{number} ", end="")
