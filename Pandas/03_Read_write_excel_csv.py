# CSV : Comma separated values

import pandas as pd

# READING CSV FILES

df = pd.read_csv("Excel files/stock_data.csv", na_values=["not available", "n.a."])
# na_values means where ever "not available" or "n.a." is encountered, fill that with NaN  => Used for cleaning data
print(df)

# In the data set, we also encounter revenue = -1, which is practically impossible. Also we have one more -1 in eps column, but if we provide -1 in the na_values list, then the other -1 in the eps col also get converted to NaN.

# Therefore, we can provide a dictionary of list
df = pd.read_csv("Excel files/stock_data.csv", na_values={
    'eps': ["not available", "n.a."],
    'revenue': ["not available", "n.a.", -1],
    'price': ["not available", "n.a."]
    'people': ["not available", "n.a."]
})
print(df)

# Skip the 1st row, and start reading from 2nd row
# Since rows no.s are like indexes, so 1st row means 0th index, and so on.. Here, we have given skiprow=1 means start reading from 1st index row, i.e, 2nd row
df2 = pd.read_csv("Excel files/stock_data.csv", skiprows=1)
print(df2)

# Same thing can be done through header instead of skiprows
# df2 = pd.read_csv("Excel files/stock_data.csv", header=1)  # Skip the 1st row, and start reading from 2nd row

# Header=None means no column names will be shown, instead indexes will be shown, 0,1,2..
# nrows = 3 means, only 3 rows will be displayed
df2 = pd.read_csv("Excel files/stock_data.csv", header=None, nrows=3)
print(df2)

# We can also provide column names of our own
df2 = pd.read_csv("Excel files/stock_data.csv", header=1, names=["TICKETS", "EPS", "REVENUE", "PRICE", "PEOPLE"])
print(df2)

# WRITE CSV FILES
