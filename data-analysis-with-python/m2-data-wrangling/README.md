# Data Wrangling

## Learning Objective
1. [V] Identify and handle missing values
2. [V] Data Formatting
3. [V] Data Normalization (centering/scaling)
4. Data Binning
5. Turning Categorical values to numeric variables


## Terms
- __Data Pre-processing__: It is the process of converting or mapping data from one `raw` form into another format to make it ready for further analysis.
- Data Pre-processing == Data Cleaning == Data Wrangling 
- __Linear Regression__


## Identify and handle missing values
- NaN, ?, N/A, 0, blank cell
- go back and collect the right data
- drop the data 
- replacing the data - less accurate - might be average of of the column / or most common string 
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