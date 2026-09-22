#!/usr/bin/env python3

num_str = input()
try:
    number = float(num_str)
    if number > 0:
        print("This number is positive.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("This is not a number.")