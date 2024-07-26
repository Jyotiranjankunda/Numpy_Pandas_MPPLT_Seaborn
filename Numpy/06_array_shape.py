# Shape is the no. of elements in each dimension of an array.

import numpy as np

n = np.array(10)
print(n.shape)  # shape : ()

n = np.array([1,5,6,7])
print(n.shape)  # shape : (4, )

n = np.array([[5,6,7], [2,3,4]])
print(n.shape)  # shape : (2, 3) i.e, 2 X 3 matrix

n = np.array([[[1,2,3], [2,3,4]], [[5,6,7], [7,8,9]]])
print(n.shape)  # shape : (2, 2, 3), i.e, 2 X 2 X 3  3-D matrix

# Array reshape
# reshape 1D to 2D
n = np.array([5,10,15,20,25,30])
reshaped_arr = n.reshape(2, 3)  # Convert the 1-D array to 2-D array, having size =  2 X 3
print(reshaped_arr)  # output: [[5,10,15], [20,25,30]]

# Flatten to 1D array
n = np.array([[[1,2,3], [2,3,4]], [[5,6,7], [7,8,9]]])
flatten_arr = n.reshape(-1)
print(flatten_arr)