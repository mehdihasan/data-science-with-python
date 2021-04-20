# EDA - Exploratory Data Analysis
- Summarize main characteristics of the data 
- Gain better understanding of the dataset.
- Uncover relationships between different variables, and
- Extract important variables for the problem we are trying to solve.

>> What are the characteristics that have the most impact on the car price?


## Learning Objectives
- DESCRIPTIVE STATISTICS: which describe basic features of a dataset and obtains a short summary about the sample and measures of the data.
- GROUP BY: Basic of Grouping Data using group by, and how this can help to transform our dataset.
- ANOVA: the analysis of variance, a statistical method in which the variation in a set of observations is divided into distinct components.
- CORRELATION: The Correlation between different variables.
- ADVANCED CORRELATION: where we’ll introduce you to various correlation statistical methods, namely Pearson Correlation and Correlation Heatmaps.


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