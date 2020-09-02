#!/usr/bin/python3
def fizzbuzz():
    """FUNCTION THAT PRINTS THE NUMBERS FROM 1 TO 100 SEPARATED BY A SPACE"""
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 10 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
