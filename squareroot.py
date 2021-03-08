# squareroot.py
# Weekly Task 06.
# This program computes the approximate squareroot of a number
# The method of Newton Raphson was used here
# author: Fionn McCarthy - G00301126.

# From research:
# Take a reasonable guess (approximate root) for the square root.
# Add the approximate root with the original number divided by the approximate root and divide by 2.
# x_i := (x_i + n / x_i) / 2
# The number of iterations must be large to get better approximation of root (from research)
# I decided to use 1,000,000 iterations here although it may take longer to run it will be more accurate 

# Below I define my squareroot funtion Sqrt() and also the number of iterations
def Sqrt(x_i, iterations = 1000000): # number of iterations must be large to get better approximation of root (from research)
    n = float(x_i)
    for i in range(iterations):      
        x_i =  (x_i + n / x_i) / 2      # x_i := (x_i + n / x_i) / 2 is formula used from research  
    return x_i

number = float(input("Enter a positive number:"))                               # Enter pos number
if number > 0:                                                                  # Number must be positive so use if n>0
    Squareroot = Sqrt(number)                                                   # If posotove then apply Sqrt() function to number 
    print("The approimate squareoot of {} is {} ".format(number, Squareroot))   # Printing result 
else:
    print("Please enter a positive number")                                     # Number must be positive

# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo 01/03/2021
# https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/ 01/03/2021
# https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf 01/03/2021