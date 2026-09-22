#!/usr/bin/env python3

input_num = input("Enter a number\n")
try:
    num = int(input_num)
    i = 1
    while i <= 9:
        print(f"{i} x {num} = {num * i}")
        i += 1
except ValueError:
    pass