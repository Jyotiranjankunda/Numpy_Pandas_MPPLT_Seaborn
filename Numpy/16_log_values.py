# Numpy has some predefined functions to work with logs, such as numpy.log2(), numpy.log10(), etc.

import numpy as np

print(np.log2(45))
print(np.log10(100))

# calculate the log values of elements in an array
n = np.array([1,5,8,2,9])
print(n)
print("Log2 :", np.log2(n))
print("Log10 :", np.log10(n))