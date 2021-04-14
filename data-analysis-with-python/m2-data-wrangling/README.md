# Data Wrangling
Data Wrangling is the process of converting data from the initial format to a format that may be better for analysis.

- [Data Wrangling](#data-wrangling)
  - [Learning Objective](#learning-objective)
  - [Terms](#terms)
  - [Identify and handle missing values](#identify-and-handle-missing-values)
    - [How to drop missing values](#how-to-drop-missing-values)
    - [How to replace missing values](#how-to-replace-missing-values)
  - [Data Formatting](#data-formatting)
  - [Data Normalization](#data-normalization)
    - [Methods of normalizing data](#methods-of-normalizing-data)
  - [Data Binning](#data-binning)
    - [How to binning in python](#how-to-binning-in-python)
  - [Turning Categorical values to numeric variables](#turning-categorical-values-to-numeric-variables)
    - [one-hot encoding](#one-hot-encoding)


## Learning Objective
1. Identify and handle missing values
2. Data Formatting
3. Data Normalization (centering/scaling)
4. Data Binning
5. Turning Categorical values to numeric variables


## Terms
- __Data Pre-processing__: It is the process of converting or mapping data from one `raw` form into another format to make it ready for further analysis.
- Data Pre-processing == Data Cleaning == Data Wrangling 
- __Linear Regression__
- __one-hot encoding__


## Identify and handle missing values
- NaN, ?, N/A, 0, blank cell
- go back and collect the right data
- drop the data 
  - drop the whole row
  - drop the whole column
- replacing the data - less accurate - might be average of of the column / or most common string 
  - replace it by mean
  - replace it by frequency
  - replace it based on other functions
- Leave it as missing data


### How to drop missing values
- `dataframes.dropna()`
- `axis=0` drops the entire row
- `axis=1` drops the entire column
- `df.dropna(subset=["price"], axis=0, inplace=True)`
- Setting the argument “inplace” to “true” allows the modification to be done on the dataset directly. “Inplace=True” just writes the result back into the dataframe.


### How to replace missing values
- `dataframe.replace(missing_values, new_value)`
- first we find the mean value, then we replace
    ```python
    mean = df["normalized-losses"].mean()
    df["normalized-losses"].replace(np.nan, mean)
    ```

## Data Formatting
- Data is usually collected from different places, by different people, which may be stored in different formats. Data formatting means bringing data into a common standard of expression that allows users to make meaningful comparisons.
- We might want to convert mile to km for city-mpg value
    ```python
    df["city-mpg"] = 235/df["city-mpg"]
    df.rename(column={"city-mpg": "city-L/100km"}, inplace=True)
    ```
- We might needed to convert the datatype
    - `datatype.astype()`
    - e.g. convert data type to integer in column price
    ```python
    df["price"] = df["price"].astype("int")
    ```

## Data Normalization
When we take a look at the used car data set, we notice in the data that the feature “length”
ranges from 150 to 250, while feature “width” and “height” ranges from 50 to 100.
We may want to normalize these variables so that the range of the values is consistent.
This normalization can make some statistical analyses easier down the road.
By making the ranges consistent between variables, normalization enables a fairer comparison
between the different features.
Making sure they have the same impact, it is also important for computational reasons.

### Methods of normalizing data
- __Simple Feature Scaling__
  - just divides each value by the maximum value for that feature.
  - `X(new) = X(old)/X(max)`
    ```python
    df["length"] = df["length"]/df["length"].max()
    ```
- __Min-Max__
  - takes each value, X_old, subtracted from the minimum value of that feature, then divides by the range of that feature.
  - `X(new) = (X(old) - X(min)) / (X(max) - X(min))`
    ```python
    df["length"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())
    ```
- __Z-Score__ / Standard Score
  - for each value, we subtract the Mu which is the average of the feature, and then divide by the standard deviation (sigma). The resulting values hover around 0, and typically range between -3 and +3, but can be higher or lower.
  - `X(new) = (X(old) - μ) / σ`
    ```python
    df["length"] = (df["length"] - df["length"].mean()) / df["length"].std()
    ```
  - `mean()` method will return the average value of the feature in the dataset
  - `std()` method will return the standard deviation of the features in the dataset.


## Data Binning
Binning is when you group values together into bins. For example, you can bin “age” into [0 to 5], [6 to 10], [11 to 15] and so on.

### How to binning in python

we need 4 numbers as dividers that are equal distance apart.

1. First we use the numpy function “linspace” to return the array “bins” that contains 4 equally spaced numbers over the specified interval of the price.
  ```python
  bins = np.linspace(min(df["price"]), max(df["price"]), 4)
  ```
2. We create a list “group_names “ that contains the different bin names.
  ```python
  group_names = ["Low", "Medium", "High"]
  ```
3. We use the pandas function ”cut” to segment and sort the data values into bins.
  ```python
  df["price-binned"] = pd.cut(df["price"], bins, labels = group_names, include_lowest = True)
  ```

You can then use histograms to visualize the distribution of the data after they’ve been
divided into bins.


## Turning Categorical values to numeric variables

### one-hot encoding
Most statistical models cannot take in objects or strings as input and, for model training,
only take the numbers as inputs. In the car dataset, the "fuel-type" feature as a categorical variable has two values, "gas" or "diesel”, which are in String format. For further analysis, we can convert these variables into some form of numeric format. We encode the values by adding new features corresponding to each unique element in the original feature we would like to encode. In the case where the feature “Fuel” has two unique values, gas and diesel, we create two new features ‘gas’ and ‘diesel.' When a value occurs in the original feature we set the corresponding value to one in the new feature; the rest of the features are set to zero. In the fuel example, for car B, the fuel value is diesel. Therefore, we set the feature diesel equal to one and the gas feature to zero. Similarly, for car D the fuel value is gas. Therefore we set the feature gas equal to one and the feature diesel equal to zero.

In pandas, we can use get_dummies() method to convert categorical variables to dummy
variables. In Python, transforming categorical variables to dummy variables is simple.

```python
pd.get_dummies(df['fuel'])
```