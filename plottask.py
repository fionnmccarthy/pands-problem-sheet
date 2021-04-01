# plottask.py
# Weekly Task 08.
# Write a program called plottask.py that displays a plot of the functions: 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# author: Fionn McCarthy - G00301126.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4)

fx = x #f(x) = x

gx = x**2 #g(x) = x^2

hx = x**3 #h(x) = x^3

plt.plot(fx, marker = 's', color = 'purple' , ls = ':', lw = '3', label = 'f(x)') #plot f(x), square marker, purple colour, linestyle is dotted, linewidth is 3, and label

plt.plot(gx, marker = 's', color = 'red' , ls = ':', lw = '3', label = 'g(x)') #plot g(x), square marker, red colour, linestyle is dotted, linewidth is 3, and label

plt.plot(hx, marker = 's', color = 'green' , ls = ':', lw = '3', label = 'h(x)') #plot h(x), square marker, green colour, linestyle is dotted, linewidth is 3, and label

font1 = {'family':'serif','color':'darkblue','size':15} #setting font1 type
font2 = {'family':'serif','color':'darkred','size':12} #setting font2 type

plt.title("Plot of f(x)=x, g(x)=X^2 & h(x)=x^3 in the range[0,4]", fontdict = font1) #include plot title with font2
plt.xlabel("X-axis", fontdict = font2) #include x-axis label with font2
plt.ylabel("Y-axis", fontdict = font2) #include y-axis label with font2

plt.grid(color = 'grey', ls = '--', lw = 0.5) #add grid lines to plot
plt.legend() # include legend in plot
plt.savefig('plottask_output.png') #save the plot output
plt.show()



# https://www.w3schools.com/python/matplotlib_intro.asp w3schools tutorial matplotlib 01/04/2021
