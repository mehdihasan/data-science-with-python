import pandas as pd

##
## Reading a CSV file using Pandas
##

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)


##
## Replace default headers
##

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers


##
## Printing part of data
##

print(df.head(5))
print(df.tail(3))

##
## Exporting a Pandas dataframe to CSV
##

path = "../results/test_result.csv"
df.to_csv(path)