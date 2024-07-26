# arr[start : end] => end is excluded

import numpy as np

n = np.array([1,6,8,4,2,7,8,3,2])
print(n[2:5])
print(n[2:])  # From 2nd index till last
print(n[:5])  # From beginning till 5th index(excluded)

# slicing by jump
# arr[start : end : step]

print(n[0:9:2])  # jump 2 steps

n2 = np.array([[6,8,9,3], [0,3,5,4]])
print(n2[0, 1:3])  # slice from 0 to 3 in the 0th index of 2D array, i.e, from [6,8,9,3]
print(n2[0:2, 1:3])  # It will slice 0 to 2 in 0th index, 1 to 3 in 1st index

