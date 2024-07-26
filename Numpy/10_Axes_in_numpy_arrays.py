# In numpy arrays, the axis is the direction along the rows  and columns. A 2-D numpy array has the following two corresponding axes.

# vertical axis (axis 0)
# horizontal axis (axis 1)

import numpy as np

# Get minimum value along axis
n = np.array([[22,50,7,91,6], [0,39,35,24,75], [10,67,45,1,90]])  # 3 X 5 matrix
print(n)

min_val = n.min()
min_val_vaxis = n.min(axis=0)
min_val_haxis = n.min(axis=1)

print("Min value in whole matrix : ", min_val)
print("Min value in vertical axis : ", min_val_vaxis)
print("Min value in horizontal axis : ", min_val_haxis)

'''
matrix :
22 50 7  91 6
0  39 35 24 75
10 67 45 1  90

Now, n.min(axis=0) returns an array having the minimum elements from all columns
in 0th col, min val = 0
in 1st col, min val = 39
in 2nd col, min val = 7
in 3rd col, min val = 1
in 4th col, min val = 6

so o/p = [ 0 39  7  1  6]

Similarily, n.min(axis=1) returns an array having the minimum elements from all rows
o/p = [6 0 1]

Similar for max value.
'''