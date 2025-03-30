# Meat-the-Economy, using the Meatmerizor model

# Video link: https://www.youtube.com/watch?v=eEIQnOcHQdU

# Project Description
Meat the Economy / Meatmerizor -  The Meatmerizor is a model that can predict the economic state of a country based on previous data of the country’s meat consumption and economic data. 
More specifically, the Meatmerizor takes in a country’s meat consumption per capita along with GDP per capita PPP for a given year in order to predict future trends. 

# Project Goals
Create a model to predict the country’s economic state based on the country’s meat consumption patterns.
Find correlations between meat consumption habits of countries with upward and downward trends on GDP per capita PPP.

# Data Collection
National meat eating history (From Kaggle)
Global GDP per capita, PPP data (From Kaggle)
Datasets: 
https://www.kaggle.com/datasets/scibearia/meat-consumption-per-capita

# Preliminary visualizations of data:
![Linear Regression Graph](LinearRegressionGraph)

# Detailed description of data processing done so far
We filtered through and dropped the years that contained null values for GDP per capita per purchasing power parity (PPP) for a given country. Since only 5% of the data set contained null GDP per capita PPP, abstaining from
using the null years won’t have a huge impact on the analysis. Next, we combined the various meats consumed at each given year for each given country into a “meatball.” This accounts for various cultural, religious, and 
geographical differences between the countries. Ultimately, we wanted to look strictly at the amount of meat with relation to the country’s GDP per capita PPP along with the growth rate of each country’s meatball.

# Detailed description of data modeling methods used so far
We ran a linear regression model with the GDP per capita PPP as the dependent variable and the meatball data as the independent. 

# Preliminary results. (e.g. we fit a linear model to the data and we achieve promising results, or we did some clustering and we notice a clear pattern in the data)
We fit the linear model onto our data and we achieved a promising result. The model suggests that the bigger a country’s meatball, the greater their GDP per capita PPP.  Our r^2 value was 0.51 which further supports the
positive correlation between meatball and GDP/PPP.
