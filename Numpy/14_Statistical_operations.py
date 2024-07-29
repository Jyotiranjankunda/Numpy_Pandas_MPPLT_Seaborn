# Statistical operations on arrays - mean, median, s.d

import numpy as np

n = np.array([1,4,8,3,5])

mean = np.mean(n)
median = np.median(n)
standard_deviation = np.std(n)

print("Array :", n)
print("Mean :", mean)
print("Median :", median)
print("Standard Deviation :", standard_deviation)