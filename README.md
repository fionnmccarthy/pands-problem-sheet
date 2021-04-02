# pands-problem-sheet 2021 

## Fionn McCarthy - G00301126.
---
## Overview

This is the README file for the Programming and Scripting 2021 module weekly task repository - PANDS-PROBLEM-SHEET. This file will outline each task, explain the code used in order to complete each of the weekly tasks and list the references used in the research of each of the problems. 

---
## Weekly Task 01 

The first weekly task was for us to introduce ourselves on the discussion forum and install the software needed to complete the weekly tasks.

---
## Weekly Task 02 - bmi.py
#### Problem:
Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py

The inputs are the person's height in centimetres and weight in kilograms.
The output  is their weight divided by their height in metres squared.
#### Code:
~~~
weight = float(input('Please enter weight(kg):'))
height = float(input('Please enter height(cm):'))
heightinmetres = float(height/100)
BMI = weight/(heightinmetres**2)
print ('BMI is {:.2f}.'.format(BMI))
~~~
#### Solution:

#### References:
 
---
## Weekly Task 03 - secondstring.py 
#### Problem:
Write a program that takes asks a user to input a string and outputs every second letter in reverse order.
#### Code:
~~~
input_string = input('Please enter a sentence:')
print(input_string[::-2])
~~~
#### Solution:

#### References:
 
---
## Weekly Task 04 - collatz.py
#### Problem:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.
#### Code:
~~~
integer = int(input("Please input a positive number:"))

if integer > 0:                             
    while integer != 1:                     
        print(integer)
        if (integer % 2) == 0:              
            integer = (integer // 2)        
        else:                               
            integer = (3 * integer + 1)     
else: 
    print("That number is not positive! Please input a positive number.")

~~~
#### Solution:

#### References:
 
---
## Weekly Task 05 - weekday.py
#### Problem:
Write a program that outputs whether or not today is a weekday.

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!
#### Code:
~~~
import datetime 

daynumber = datetime.datetime.today().weekday() 

if daynumber < 5:
    print("Yes, unfortunately today is a weekday!") 
else:
    print("It is the weekend, yay!") 
~~~
#### Solution:

#### References:
 
---
## Weekly Task 06 - squareroot.py
#### Problem:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

I suggest that you look at the newton method at estimating square roots.

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
#### Code:
~~~
def Sqrt(x_i): 
    n = float(x_i)
    precision = 10**(-10)              
    while abs(n-x_i*x_i) > precision:   
        x_i =  (x_i + n / x_i) / 2      
    return x_i

number = float(input("Enter a positive number:"))                               
if number > 0:                                                                  
    Squareroot = Sqrt(number)                                                   
    print("The approimate squareoot of {} is {} ".format(number, Squareroot))   
else:
    print("Please enter a positive number") 
~~~
#### Solution:

#### References:
 
---
## Weekly Task 07 - es.py
#### Problem:
Write a program that reads in a text file and outputs the number of e's it contains.

The program should take the filename from an argument on the command line.
#### Code:
~~~
import sys 
filename = sys.argv[1] 

with open(filename, "r") as f:  
    filedata = f.read() 
    print(filedata.count('e')) 
~~~
#### Solution:

#### References:
 
---
## Weekly Task 08 - plottask.py
#### Problem:
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.

Some marks will be given for making the plot look nice.
#### Code:
~~~
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4)
fx = x 
gx = x**2 
hx = x**3 

plt.plot(fx, marker = 's', color = 'purple' , ls = ':', lw = '3', label = 'f(x)') 
plt.plot(gx, marker = 's', color = 'red' , ls = ':', lw = '3', label = 'g(x)') 
plt.plot(hx, marker = 's', color = 'green' , ls = ':', lw = '3', label = 'h(x)') 

font1 = {'family':'serif','color':'darkblue','size':15} #setting font1 type
font2 = {'family':'serif','color':'darkred','size':12} #setting font2 type

plt.title("Plot of f(x)=x, g(x)=X^2 & h(x)=x^3 in the range[0,4]", fontdict = font1) 
plt.xlabel("X-axis", fontdict = font2) #include x-axis label with font2
plt.ylabel("Y-axis", fontdict = font2) #include y-axis label with font2

plt.grid(color = 'grey', ls = '--', lw = 0.5) 
plt.legend()
plt.savefig('plottask_output.png') 
plt.show()
~~~
#### Solution:

#### References:
 