# collatz.py
# Weekly Task 04.
# This program asks a user to input any positive integer,
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# author: Fionn McCarthy - G00301126.

# Ask the user to input a positive number
integer = int(input("Please input a positive number:"))

# Integer must be positive therefore where greater than zero execute 
# program ends when it is equal to 1

if integer > 0:                             # Check number integer inputted is positive
    while integer != 1:                     # While loop used as program stops when integer equals 1
        print(integer)
        if (integer % 2) == 0:              # Check if number is even,
            integer = (integer // 2)        # If number is even divide by 2 
        else:                               # Check if number is not even,
            integer = (3 * integer + 1)     # If number is not even then muliply by 3 and add 1
else: 
    print("That number is not positive! Please input a positive number.")


# References
# https://www.w3schools.com/python/python_conditions.asp 28/02/20201
# https://www.w3schools.com/python/python_while_loops.asp 28/02/2021

