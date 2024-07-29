from numpy import random

# Get any random number from 0 to 10
n = random.randint(10)
print("Random no. between 0 to 10 :", n)

# Get 4 random numbers as array elements from 0 to 10
arr = random.randint(10, size=4)
print(arr)

# Get a random number from the following array values
a = random.choice([10,30,4,6,12,89,23,90,45])
print(a)