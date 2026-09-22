#!/usr/bin/env python3

num_str = input()
try: 
    number = float(num_str)
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("This is not a number.")