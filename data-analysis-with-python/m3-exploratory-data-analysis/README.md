- [EDA - Exploratory Data Analysis](#eda---exploratory-data-analysis)
  - [Learning Objectives](#learning-objectives)
  - [Descriptive Statistics](#descriptive-statistics)
  - [Group By](#group-by)
    - [How to](#how-to)
    - [Visualization](#visualization)
      - [pivot method](#pivot-method)
      - [heatmap](#heatmap)
  - [Analysis of Variance ANOVA](#analysis-of-variance-anova)
    - [Why do we perform ANOVA?](#why-do-we-perform-anova)
    - [What we obtain from ANOVA?](#what-we-obtain-from-anova)
    - [How to perform](#how-to-perform)
  - [Correlation](#correlation)
    - [What is Correlation?](#what-is-correlation)
    - [Example and how to](#example-and-how-to)
      - [Positive Correlation](#positive-correlation)
      - [Negative Correlation](#negative-correlation)
      - [Weak Correlation](#weak-correlation)
  - [Advanced Correlation](#advanced-correlation)
    - [Example and how to](#example-and-how-to-1)
      - [Strong Positive Correlation](#strong-positive-correlation)



# EDA - Exploratory Data Analysis
- Summarize main characteristics of the data 
- Gain better understanding of the dataset.
- Uncover relationships between different variables, and
- Extract important variables for the problem we are trying to solve.

>> What are the characteristics that have the most impact on the car price?


## Learning Objectives
- __DESCRIPTIVE STATISTICS__: which describe basic features of a dataset and obtains a short summary about the sample and measures of the data.
- __GROUP BY__: Basic of Grouping Data using group by, and how this can help to transform our dataset.
- __ANOVA__: the analysis of variance, a statistical method in which the variation in a set of observations is divided into distinct components.
- __CORRELATION__: The Correlation between different variables.
- __ADVANCED CORRELATION__: where we’ll introduce you to various correlation statistical methods, namely Pearson Correlation and Correlation Heatmaps.


## Descriptive Statistics
- `df.describe()`
    - Using the describe function and applying it on your dataframe, the "describe" function automatically computes basic statistics for all numerical variables. It shows the mean, the total number of data points, the standard deviation, the quartiles and the extreme values. Any NaN values are automatically skipped in these statistics. This function will give you a clearer idea of the distribution of your different variables. 
- `value_counts()`    
    - You could have also categorical variables in your dataset. These are variables that can be divided up into different categories, or groups and have discrete values. For example, in our dataset we have the drive system as a categorical variable, which consists of the categories: forward-wheel drive, rear-wheel drive, and four-wheel drive. One way you can summarize the categorical data is by using the function value_counts(). We can change the name of the column to make it easier to read. We see that we have 118 cars in the fwd (front wheel drive) category, 75 cars in the rwd (rear wheel drive) category, and 8 cars in the 4wd (four wheel drive) category.
    - drive_wheels_counts=df["drive-wheels"].values_counts()
    - drive_wheels_counts.rename(columns={'drive-wheels':'values_counts' inplace=True})
    - drive_wheels_counts.index.name='drive-wheels'
- Box Plots
    - `sns.boxplot(x="drive-wheels", y="price", data=df)`
    - Boxplots are a great way to visualize numeric data, since you can visualize the various distributions of the data. The main features that the boxplot shows are the median of the data, which represents where the middle datapoint is. The Upper Quartile shows where the 75th percentile is, the Lower Quartile shows where the 25th percentile is. The data between the Upper and Lower Quartile represents the Interquartile Range. Next, you have the Lower and Upper Extremes. These are calculated as 1.5 times the interquartile range above the 75th percentile, and as 1.5 times the IQR below the 25th percentile. Finally, boxplots also display outliers as individual dots that occur outside the upper and lower extremes. With boxplots, you can easily spot outliers and also see the distribution and skewness of the data. Boxplots make it easy to compare between groups. In this example, using Boxplot we can see the distribution of different categories of the “drive-wheels” feature over price feature. We can see that the distribution of price between the rwd (rear wheel drive) and the other categories are distinct, but the price for fwd (front wheel drive) and 4wd (four wheel drive) are almost indistinguishable.
- Scatter Plot
    - Often times we tend to see continuous variables in our data. These data points are numbers contained in some range. For example, in our dataset, price and engine size are continuous variables. What if we want to understand the relationship between “engine size” and ”price”? Could engine size possibly predict the price of a car? One good way to visualize this is using a scatter plot. Each observation in a scatter plot is represented as a point. This plot shows the relationship between two variables: The predictor variable: is the variable that you are using to predict an outcome. In this case, our predictor variable is the engine size. The target variable: is the variable that you are trying to predict. In this case, our target variable is the price, since this would be the outcome. In a scatterplot, we typically set the predictor variable on the x-axis, or horizontal axis and we set the target variable on the y-axis or vertical axis. In this case, we will thus plot the engine size on the x-axis and the price on the y-axis. We are using the Matplotlib function “scatter” here, taking in x and a y variable. Something to note is that it’s always important to label your axes and write a general plot title, so that you know what you are looking at. Now how is the variable Engine Size related to Price? From the scatterplot we see that as the engine size goes up, the price of the car also goes up. This is giving us an initial indication that there is a positive linear relationship between these two variables.


## Group By

The group by method is used on categorical variables, groups the data into subsets according to the different categories of that variable. Group by can be applied to a single variable or multiple variables by passing in multiple variable names.

### How to 

```python
df_test = df[['drive-wheels', 'body-style', 'price']]
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
```

### Visualization

#### pivot method
using pivot table: A pivot table has one variable displayed along the columns and the other variable displayed along the rows.
rectangular grid: easier to visualize. This is similar to what is usually done in Excel spreadsheets.

```python
df_pivot = df_grp.pivot(index='drive-wheels', columns='body-style')
```

#### heatmap
heatmap plot: Heat map takes a rectangular grid of data and assigns a color intensity based on the data value at the grid points. It is a great way to plot the target variable over multiple variables and through this get visual clues of the relationship between these variables and the target.

```python
plt.pcolor(df_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
```


## Analysis of Variance ANOVA

### Why do we perform ANOVA?
ANOVA is a statistical test that stands for "Analysis of Variance". ANOVA can be used to find the correlation between different groups of a categorical variable. According to the car dataset, we can use ANOVA to see if there is any difference in mean price for the different car makes such as Subaru and Honda.

### What we obtain from ANOVA?
The ANOVA test returns two values: (1) the F-test score and (2) the p-value.

__The F-test__ calculates the ratio of variation between the group's mean over the variation within each of the sample groups.

__The p-value__ shows whether the obtained result is statistically significant.

### How to perform

```python
df_anova = df[["make", "price"]]
grouped_anova = df_anova.groupby(["make"])
## ANOVA between "Honda" and "Subaru"
anova_resulta_1 = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("subaru")["price"])
## ANOVA between "Honda" and "Jaguar"
anova_resulta_2 = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("jaguar")["price"])
```

>>> ANOVA result 1: F=0.197..., p=F_onewayResult(statistic=0.197...), pvalue=0.660...

>>> ANOVA result 1:  F=400.925..., p=F_onewayResult(statistic=400.925...), pvalue=1.058...e-11



## Correlation

### What is Correlation?
Correlation is a statistical metric for measuring to what extent different variables are interdependent.  
In other words, when we look at two variables over time, if one variable changes how does this affect change in the other variable?  
### Example and how to 

#### Positive Correlation
e.g. 1, engine size vs price.  
(using seaborn.regplot to create the scatter plot)
```python
sns.regplot(x="engine-size", y="prices", data=df)
plt.ylim(0,)
```
#### Negative Correlation
e.g. 2, highway-mpg and price
```python
sns.regplot(x="highway-mpg", y="prices", data=df)
plt.ylim(0,)
```

#### Weak Correlation
e.g. 3, peak-rpm and price
```python
sns.regplot(x="peak-rpm", y="prices", data=df)
plt.ylim(0,)
```


## Advanced Correlation

One way to measure the strength of the correlation between continuous numerical variable is by using a method called Pearson correlation. Pearson correlation method will give you two values: (1) the correlation coefficient and (2) the P-value.

__(1) Correlation Coefficient__
- Close to +1: Large Positive relationship
- Close to -1: Large Negative relationship
- Close to 0: No relationship

__(2) P-value__
- P-value < 0.001 Strong certainty in the result
- P-value < 0.05 Moderate certainty in the result
- P-value < 0.1 Weak certainty in the result
- P-value > 0.1 No certainty in the result

__Strong Correlation__
- Correlation Coefficient close to 1 or -1
- P value less than 0.001

### Example and how to 

#### Strong Positive Correlation
e.g. 1, horsepower vs price.  
```python
pearson_coef, p_value = stats.pearsonr(df["horsepower"], df["price"])
```
>> Pearson correlation: 0.81
>> P-value: 9.35 e-48