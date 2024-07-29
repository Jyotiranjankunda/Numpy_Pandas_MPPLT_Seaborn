# Pandas is a Python library used for working with data sets.
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# It makes data science easy and effective.

# Data science or data analytics is a process of analyzing large set of data points to get answers on questions related to that data set.

import pandas as pd
df = pd.read_csv("Excel files/nyc_weather.csv")
print(df)

# Q: What was the max. temperature ?
print("Max. temperature :", df['Temperature'].max())  # Maximum temperature from Temperature column in the csv file

# Q: On which days did it rain ?
print("\nDays on which rain occur :")
print(df['EST'][df['Events']=='Rain'])

# Q: What was average speed of wind during the month.
print("\nAverage speed of wind : (With NaN values)")
print(df['WindSpeedMPH'].mean())
# mean may not be correct, as many fields in the excel sheet are blank, so NaN values are there.

# First we have to clean the data
# Process of cleaning messy data is called data munging or data wrangling

# Fill the NaN values with 0
df.fillna(0, inplace=True)

# Now the mean value will be different as compared to previous result.
print("\nAverage speed of wind : (With cleaned data)")
print(df['WindSpeedMPH'].mean())
