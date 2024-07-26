# set Intersection - using intersect1d() method

import numpy as np

n1 = np.array([10,50,30,20,60,40])
n2 = np.array([80,50,90,100,40,70])

res = np.intersect1d(n1, n2)
print(res)  # intersection array is always sorted

# Intersection of disjoint arrays
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

res = np.intersect1d(arr1, arr2)
print(res)  # output: []

# Difference between 2 arrays - setdiff1d() method
res = np.setdiff1d(n1, n2)  # n1 - n2 = {10, 20, 30, 60}
# It also displays sorted results
print(res)

res = np.setdiff1d(n2, n1)  # n2 - n1 = {70, 80, 90, 100}
print(res)

# Similarily, other set operations are there