#!/usr/bin/env python3

first_num = input("Enter the first number:\n")
second_num = input("Enter the second number:\n")
try:
    num1 = float(first_num)
    num2 = float(second_num)
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")
except ValueError:
    pass
