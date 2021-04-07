## Should check:
## 1. Data Type
## 2. Data Distribution

## Pandas Data Types VS Python Data Type
## 1. Object == string
## 2. int64 == int
## 3. float64 == float
## 4. datetime64, timedelta[ns] == N/A (ref python datetime module)

import pandas as pd


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers

##
## Describe data types
##

print(df.dtypes)
print(df.describe)

##
## Returns statistical summary
##

# print(df.describe())

##
## Returns full statistical summary
##

## Unique > The number of distinct objects in the column

## Top > Most frequent occuring object

## Freq > The number of times top objects appear in the column

print(df.describe(include="all"))

##
## Provides a concise summary of the dataframe based on: top and bottom 30 rows of dataframe
##

print(df.info())