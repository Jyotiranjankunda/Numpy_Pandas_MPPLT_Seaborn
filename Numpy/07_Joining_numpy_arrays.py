# For joining 2 or more arrays:
# concatenate() method : Joining along the existing axis, unlike keys in SQL. Resulting array has the same no. of dimensions as the input arrays
# stack methods : Joining along a new axis, unlike keys in SQL. An extra dimension will be added in the resultant array.

# con

import numpy as np

# using concatenate method
n1 = np.array([1,2,3,4,5])
n2 = np.array([6,7,8,9,10])

res_arr = np.concatenate((n1, n2))
print(res_arr)

# Using stack methods : stack(), hstack(), vstack(), dstack(), column_stack()
res_arr = np.stack((n1, n2))  # By default axis is horizontal
print(res_arr)

res_arr = np.stack((n1, n2), axis=1)  # Axis is vertical
print(res_arr)

res = np.hstack((n1, n2))  # stack along rows. New dimension will not be created
print(res)

res = np.vstack((n1, n2))  # joining along columns.
print(res)

res = np.dstack((n1, n2))  # stack along depth, i.e, height
print(res)

res = np.column_stack((n1, n2))
print(res)