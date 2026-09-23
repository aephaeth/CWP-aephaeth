import math

a_num =input("Give me a number: ")
try:
    number = float(a_num)
    result = math.ceil(number)
    print(result)
except ValueError:
    pass
