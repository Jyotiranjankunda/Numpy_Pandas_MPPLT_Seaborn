# we can search for a specific value using numpy.where() method

import numpy as np

# Searching
n = np.array([4,5,7,89,34,3,6,7])

ind = np.where(n == 7)
print(ind)  # It will print all those indexes where 7 is present

# Sorting
sort_arr = np.sort(n)
print(sort_arr)

n = [[5,8,2], [9,1,2], [0,5,1], [1,2,3]]
sort_arr = np.sort(n)  # It will sort row wise
print(sort_arr)

arr = np.array(["java", "python", "cpp", "go", "javascript"])
print(np.sort(arr))