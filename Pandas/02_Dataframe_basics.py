# Dataframe is a main object in pandas. It is used to represent data with rows and columns (e.g, excel data)

'''
Different ways to creating dataframe in pandas

1. Using CSV
2. Using Excel
3. From python dictionary
4. From list of tuples
5. From list of dictionaries
'''

import pandas as pd

# Dataframe from csv file
df = pd.read_csv("Excel files/weather_data.csv")
print(df)

# Dataframe from excel file
df_excel = pd.read_excel("Excel files/weather_data_excel.xlsx", "Sheet1")
print(df_excel)

# Create dataframe using dictionary
weather_data = {
    'day': ['01-01-2017', '01-02-2017', '01-03-2017', '01-04-2017', '01-05-2017', '01-06-2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

data = pd.DataFrame(weather_data)
print(data)

# Data frame from list of tuples
weather_data = [
    ('01-01-2017', '01-02-2017', '01-03-2017', '01-04-2017', '01-05-2017', '01-06-2017'),
    (32, 35, 28, 24, 32, 31),
    (6,7,2,7,4,2),
    ('Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny')
]

data = pd.DataFrame(data, columns=['day', 'temperature', 'windspeed', 'event'])
print(data)

# Dataframe from list of dictionaries
weather_data = [
    {'day': '01-01-2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '01-02-2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '01-03-2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    {'day': '01-04-2017', 'temperature': 24, 'windspeed': 7, 'event': 'Snow'},
    {'day': '01-05-2017', 'temperature': 32, 'windspeed': 4, 'event': 'Rain'},
    {'day': '01-06-2017', 'temperature': 31, 'windspeed': 2, 'event': 'Sunny'},
]

data = pd.DataFrame(weather_data)
print(data)

rows, columns = df.shape  # Shape is the dimension ..  Here 6 X 4
print("Rows :", rows)
print("Columns :", columns)

# Printing rows
print(df.head())  # By default, print initial 5 rows
print(df.head(2))  # Print first 2 rows

print(df.tail())  # Print last 5 rows (by default)
print(df.tail(3))  # Print last 3 rows

print(df[2:5])  # from 2nd row to 4th row, 5th not included.
# Row no. starts from 0, just like indexing

print(df.loc[1])  # row at 1st index
print(df.loc[2])  # row at 2nd index

# Printing columns
print(df.columns)  # Print all the column names

print(df.day)  # Print day columns
# Or another syntax is :
print(df['day'])

# For printing any one column the above syntax is correct, but for printing more than one columns specificially, then we need to pass all those selected columns in a list
print(df[['day', 'temperature']])

print(type(df['event']))

# Print only selected columns
print(df[['windspeed', 'event']])

# Operations on data frame

# arithmetic operations
print(df['temperature'].max())
print(df['temperature'].min())
print(df['temperature'].max())
print(df['temperature'].std())

# describe function will print all the statistical values of the numerical data in the dataframe
print(df.describe())

# Selecting conditional data in dataframe

# Q: print all the rows where temperature >= 32
print(df[df['temperature'] >= 32])
# or, another syntax
print(df[df.temperature >= 32])

# Q: Find maximum temperature
print(df[df.temperature == df['temperature'].max()])
# If column name consists of spaces, then you need to write the column names in this syntax: df['col name'], otherwise its fine to write in any syntax

# Q: Print day when temperature is maximum
# Like this, we can print specific attributes based on condition
print(df['day'][df.temperature == df['temperature'].max()])

# Q: Print day and windspeed, when temperature is minimum
print(df[['day', 'windspeed']][df.temperature == df['temperature'].min()])

# set index and reset index
# By default every row is given an index starting from 0
# If we want to modify the index, as any attribute, then we have to set index

df.set_index('day', inplace=True)  # inplace = True will modify the original dataset
print(df)
print(df.loc['1/3/2017'])  # Get at data at 1/3/2017 index

df.reset_index(inplace=True)  # Reset the df back to original