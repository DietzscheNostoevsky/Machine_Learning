# Ques 2 : https://www.coursera.org/learn/multivariate-calculus-machine-learning/quiz/vV8Og/simple-artificial-neural-networks/attempt

import numpy as np

# First set up the network.
sigma = np.tanh
W = np.array([[-2, 4, -1], [6, 0, -3]])
b = np.array([0.1, -2.5])

# Define our input vector
x = np.array([0.3, 0.4, 0.1])

# Calculate the values by hand,
# and replace a1_0 and a1_1 here (to 2 decimal places)
# (Or if you feel adventurous, find the values with code!)

a1 = sigma((W @ x) + b)  # make a note of how to use input in a function

print(a1)
