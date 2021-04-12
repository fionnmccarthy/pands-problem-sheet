# bmi.py
# Weely Task 02.
# This program calcluates a person's Body Mass Index (BMI) by inputting height(cm) and weigh(kg). 
# The program then coverts the height to metres and applies the BMI formula.
# The BMI formula is weight(kg) divided by height(m) squared.
# Author: Fionn McCarthy - G00301126.

# The user is instructed to enter weight in kg and height in cm.
# We must set the input to be a float in order to allow for decimal place values eg 88.5kg
weight = float(input('Please enter weight(kg):'))
height = float(input('Please enter height(cm):'))

# We must convert height to metres in order to input in to formula.
heightinmetres = float(height/100)

# The formula to calculate BMI is weight(kg) divided by height(m) squared.
# Therefore we sqaure the height and apply it in the BMI formula. 
# '**2' squares a number
BMI = weight/(heightinmetres**2)

# Print BMI to 2 decimal places using the '2f' here as gives a floating number to decimal places
print ('BMI is {:.2f}.'.format(BMI))

# References
# https://docs.python.org/3/library/functions.html python built in functions 28/02-2021
# https://www.w3schools.com/python/python_numbers.asp python numbers w3schools 28/02-2021