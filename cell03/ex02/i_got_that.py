#!/usr/bin/env python3

user_input = input("What you gotta say? :\n")
try:
    str_input = str(user_input)
    while(True):
        if str_input == "STOP":
            break
        print(str_input)
        user_input = input("I got that! Anything else? :\n")
        str_input =str(user_input)
except ValueError:
    pass
