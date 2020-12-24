# n = 1:100
#
# for test in range(100):
#     if test % 3  ==0
#         print(test)
"""
for test in range(100):
    if test % 3  == 0 and test != 0:
        print(test)
"""

import sys
import numpy as np
import folder1 as fl

def f(x):
    return x ** 2

def f(x):
    return x ** 3

def f(x):
    return x ** 4

x_plot = np.arange(-10,10,0.1)
y_plot = f( x = x_plot)
l_obj = fl.lineplot( xlim = (-10,10) , ylim = (-1,100), filename = "gurafu/gurafu_lineplot.png")
s_obj = fl.scatter( xlim = (-10,10) , ylim = (-1,100), filename = "gurafu/gurafu_scatter.png")

l_obj.plot(x = x_plot , y = y_plot)
s_obj.plot(x = x_plot , y = y_plot)
