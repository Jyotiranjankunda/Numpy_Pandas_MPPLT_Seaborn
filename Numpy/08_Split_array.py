# syntax: array_split(arr_name, split_num)
# split_num is the count of splits.
# It will do the optimal division, i.e, approximately equal division to all the parts

import numpy as np

n = np.array([10, 20, 30, 40, 50, 60, 70])
arr = np.array_split(n, 2)  # Divide into 2 parts, (4, 3)
for i in arr:
    print(i)

arr = np.array_split(n, 3)  # Divide into 3 parts, (3, 2, 2)
for i in arr:
    print(i)

# access any element in splitted array
print(arr[0])
print(arr[0][1])

print(arr[1])
print(arr[1][0])

# split 2-D array
n = np.array([[1,3,5], [4,8,12]])
result = np.array_split(n, 2)

for array in result:
    print(array)