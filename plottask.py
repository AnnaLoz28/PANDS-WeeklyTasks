# plottask.py
# program that displays on the one set of axes:
#  a) a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2. 
#  b) a plot of the function  h(x)=x3 in the range 0 to 10.
# the resulting plots images should be saved in png files.
# author: Anna Lozenko


import numpy as np
import matplotlib.pyplot as plt


rng = np.random.default_rng(seed = 123) # generate random numbers with NumPy. Define a seed to always generate the same set of values any time the program is run (https://numpy.org/doc/2.1/reference/random/generator.html)
norm_num = rng.normal(5, 2, 1000) # generate an array of 1000 normally distributed values with a mean of 5 and standard deviation of 2 (https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html)

# create a histogram plot of the normally distributed numbers and save it to a png file:
plt.hist(norm_num, color = "red", edgecolor = "black") # set the plot color to red and the bins borders to black
title_font= {"family": "sans-serif", "color" : "black", "size" : 16, "weight" : "bold"} # set a custom font for the title of the plot
plt.title("Histogram Plot of 1000 Normally Distributed Numbers", fontdict= title_font)
plt.xlabel("Values") 
plt.ylabel("Frequency")
plt.grid(alpha = 0.2) # add a grid with 80% transparency
plt.savefig("Histogram Plot of 1000 Normally Distributed Numbers.png")
plt.show()


# generate an array of 1000 numbers in the range of 0 to 10:
x = np.linspace(0, 10, 100) 
func = x ** 3 # use the array for the function h(x) = x^3

# create a plot that displays the h(x) = x^3 function and saves it to a png file:
plt.plot(func, "g-") # use green line for the plot
plt.xlabel("Values")
plt.ylabel("$x^3$") # use LaTex to display math symbols better
title_font= {"family": "sans-serif", "color" : "black", "size" : 16, "weight" : "bold"} # set a custom font for the title of the plot
plt.title("Function h(x) =" "$x^3$", fontdict= title_font)
plt.savefig("Function h(x) = x ^ 3.png")
plt.show()