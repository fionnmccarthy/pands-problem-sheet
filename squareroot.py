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

# Below I define my squareroot funtion Sqrt() 
def Sqrt(n): 
    n = float(n)
    x1 = n/2    # x1 formula is n divide 2
    x2 = (x1 + n/x1) /2 #formula for x2
    while x2 != x1:   # loop until x1 and x2 are equal
        x1 = x2 
        x2 =  (x1 + n / x1) / 2      # x_i := (x_i + n / x_i) / 2 is formula used from research  
    return x1

number = float(input("Enter a positive number:"))                               # Enter pos number
if number > 0:                                                                  # Number must be positive so use if n>0
    Squareroot = Sqrt(number)                                                   # If positove then apply Sqrt() function to number 
    print("The approximate squareoot of {} is {} ".format(number, round(Squareroot,1)))   # Printing result rounded to one decimla place
else:
    print("Please enter a positive number")                                   # Number must be positive to get root

# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo 01/03/2021
# https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/ 01/03/2021
# https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf 01/03/2021