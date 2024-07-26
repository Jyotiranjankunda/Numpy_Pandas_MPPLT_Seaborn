import numpy as np

#  In NumPy, all elements of the array must have the same length at each dimension.

# 0-D numpy array
n0 = np.array(10)
print(n0)
print("Dimension :", n0.ndim)  # ndim function is used to print the dimension

# 1-D numpy array
n1 = np.array([1,2,3,4,5])
print(n1)
print(n1[1])
print("Dimension :", n1.ndim)

# using negative indexes
print(n1[-1])

# 2-D numpy array
n2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(n2)
print(n2[2])  # print the 3rd row, [7,8,9]
print(n2[1,2])  # same as saying n2[1][2]
print("Dimensions :", n2.ndim)
print(n2[0, -1])  # Row 1 - last element
print(n2[1, -2])  # Row 2 - last 2nd element

# 3-D numpy array
n3 = np.array([[[4,5,6], [8,2,6], [7,8,9], [1,5,4]]])
print(n3)
print(n3[0])
print(n3[0,3])
print(n3[0,2,2])
print("Dimensions :", n3.ndim)

# If you need to work with arrays of irregular shapes, you can create an array with dtype=object
n4 = np.array([[5,6,7,8], [2,3,4], [9,0,8]], dtype=object)
print(n4)
print("Dimensions :", n4.ndim)