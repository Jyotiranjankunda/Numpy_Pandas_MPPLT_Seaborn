# Scalar operations on numpy arrays include performing addition or subtraction, or multiplication on each element of a numpy array; while arithmetic operations perform on whole array

import numpy as np

n1 = np.array([1,4,8,3,5])
n2 = np.array([7,3,7,1,9])

n1 = n1 + 10  # Add 10 to each element of n1
n2 = n2 + 5  # Add 5 to each element of n2
print(n1)
print(n2)

n1 = n1 - 6  # Subtract 6 to each element of n1
n2 = n2 - 8  # Subtract 8 to each element of n2
print(n1)
print(n2)

n1 = n1 * 3  # Multiply 3 to each element of n1
n2 = n2 * 2  # Multiply 2 to each element of n2
print(n1)
print(n2)

n1 = n1 / 4  # Divide 4 to each element of n1
n2 = n2 / 9  # Divide 9 to each element of n2
print(n1)
print(n2)