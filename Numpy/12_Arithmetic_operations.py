import numpy as np

# sum
n1 = np.array([1,2,3,4,5])
n2 = np.array([6,7,8,9,10])

arr_sum = np.sum([n1,n2])
print("Sum : ", arr_sum)  # output: 55

# add column values
print(n1)
print(n2)
arr_sum = np.sum([n1,n2], axis=0)  # It will add column by column, like 1+6 = 7, 2+7 = 9, and return all columns sum in the form of an array

print(arr_sum)

# add row values
print(n1)
print(n2)
arr_sum = np.sum([n1,n2], axis=1)  # It will add row by row, and return the sum of 2 rows in an resultant array

print(arr_sum)

# subtraction
res = np.subtract(n1, n2)  # It will subtract column by column and result in a new array
print(res)

# multiply
res = np.multiply(n1, n2)  # column by column and result in a new array
print(res)

# divide
res = np.divide(n1, n2)  # # column by column and result in a new array. If any dividend is 0, then error
print(res)