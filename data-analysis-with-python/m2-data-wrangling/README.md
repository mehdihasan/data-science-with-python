# Data Wrangling


## Terms
- __Data Pre-processing__: It is the process of converting or mapping data from one `raw` form into another format to make it ready for further analysis.
- Data Pre-processing == Data Cleaning == Data Wrangling 


## Learning Objective
1. Identify and handle missing values
2. Data Formatting
3. Data Normalization (centering/scaling)
4. Data Binning
5. Turning Categorical values to numeric variables


## Identify and handle missing values
- NaN, ?, N/A, 0, blank cell
- go back and collect the right data
- drop the data 
- replacing the data - less accurate - might be average of of the column / or most common string 
- Leave it as missing data


### How to drop 
- `dataframes.dropna()`
- `axis=0` drops the entire row
- `axis=1` drops the entire column
- `df.dropna(subset=["price"], axis=0, inplace=True)`
- Setting the argument “inplace” to “true” allows the modification to be done on the dataset directly. “Inplace=True” just writes the result back into the dataframe.


### How to replace missing values
- `dataframe.replace(missing_values, new_value)`
- first we find the mean value, then we replace
    ```py
    mean = df["normalized-losses"].mean()
    df["normalized-losses"].replace(np.nan, mean)
    ```