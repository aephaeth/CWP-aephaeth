a_num =input("Give me a number: ")
try:
    number = float(a_num)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This is not a number.")
    


    