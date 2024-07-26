'''
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
'''

import numpy as np

n = np.array([10, 20, 30])
print(n.dtype)

n = np.array(["watermelon", "mango", "banana", "litchi"])
print(n.dtype)  # <U10 => U : unicode string, 10 : maximum characters input (here, watermelon has max length, i.e, 10)

# set the data type
n = np.array(["watermelon", "mango", "banana", "litchi"], dtype='S5')
# s : byte string (ascii string), 5 : maximum length of string
#  When you specify a data type like S10, it means each string in the array can have a maximum length of 10 characters. If you attempt to store a string longer than this, it will be truncated to the specified length.

print(n.dtype)
print(n)  # output : [b'water' b'mango' b'banan' b'litch']

# Difference between unicode and byte strings

# 1. Unicode Strings Can represent a wide range of characters from various languages and symbols while Byte Strings are limited to 256 different values, typically representing ASCII characters when used as text.

# 2. Unicode strins sse multi-byte encodings (UTF-8, UTF-16, UTF-32) to represent characters while Byte Strings use single-byte values for each character (when representing ASCII text) or can represent arbitrary binary data.

# 3. for e.g, the Unicode array can handle characters like "水" (Chinese character) and "🍌" (banana emoji), while the byte string array cannot represent these characters and is limited to ASCII text.


# Convert one data type to other
# astype() method : used to create a copy of an array and then set the new data type to it.

# converting U to I
arr = np.array(['10', '20', '30', '40', '50'])
print(arr.dtype)

arr2 = arr.astype('i')
print(arr2.dtype)

