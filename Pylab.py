# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:47:40 2024

@author: Santos Family
"""

import math
import pylab
import random


pylab.plot([5,4,3,2,1])
pylab.show()


pylab.plot([1,2,3,4,5,6,7,8,9,10], 'rx--', linewidth = 3)
pylab.show()


pylab.linspace(0, 4*math.pi, 100)
pylab.show()


x_values = pylab.linspace(0, math.pi*4, 50)
y_values = [math.sin(x) for x in x_values]
pylab.plot(x_values, y_values)
pylab.xlabel('x values')
pylab.ylabel('sine of x')
pylab.title('Plot of sine from 0 to 4pi')
pylab.show()


x = pylab.linspace(0, 20, 100)

pylab.plot(x, x, color="blue", label="y=x")

pylab.plot(x, x**2, color="green", linewidth = 2, label = "y=x"+ u' \u00B2')

pylab.plot(x, x**3, color = "red", linewidth = 3, label = "y=x" + u' \u00B3')

pylab.legend(loc = " upper right", title = " Legend")

pylab.ylim(0.0, 100.0)

pylab.show()



x_values = [random.randint(0,1000) for x in range(10000)]

pylab.hist(x_values, 100)
pylab.xlabel('bins of size 10')
pylab.ylabel('frequency')
pylab.title('plot of 10,000 random ints 0-1000, bins of size 10')
pylab.show()


pylab.axes(aspect = 1)
values = [10,20,50,100,200,1000]
pie_labels = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

pylab.pie(values, labels=pie_labels,colors=color_list)
pylab.title('Pie chart of 6 values')
pylab.show()