#!/usr/bin/env python3

input_num = input("Enter a number less than 25:\n") 
try:
    num = int(input_num)
    if num > 25:
        print ("Error")
    else:
        while num <= 25:
            print(num)
            num += 1
except ValueError:
    pass
