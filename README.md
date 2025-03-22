# Meat-the-Economy, using the Meatmerizor model

# Project Description
Meat the Economy / Meatmerizor -  The Meatmerizor is a model that can predict the economic state of a country based on previous data of the country’s meat consumption and economic data. 
More specifically, the Meatmerizor takes in a country’s meat consumption per capita along with Gross National Income, IMF exchange rates, population etc. for a given year. 
The output is the predicted economic growth or decay. 
# Project Goals
Create a model to predict the country’s economic state based on the country’s meat consumption patterns. 
# Data Collection
National meat eating history (From Kaggle)
Global economic data (From Kaggle)
Datasets: 
https://www.kaggle.com/datasets/scibearia/meat-consumption-per-capita
https://www.kaggle.com/datasets/prasad22/global-economy-indicators
# Data Modeling
Polynomial/Linear Regression - starting with simple regression
Classification Model/ Logistic regression 
# Data Visualization
Heatmaps and Scatterplots
# Test Plan
We are most likely going to start by building predictive models for a few countries of our choosing and comparing their outputs to established data from government websites to see if our model is predicting correctly. 
We will then slowly add more countries until we finish a constructive that has all our countries and predicts out ten years. 
First, we’ll meatmerize data for Jamaica, Nepal, Egypt, Nigeria, and the United States from 1961-2021

# MIDTERM REPORT

# Preliminary visualizations of data:
![Linear Regression Graph]LinearRegressionGraph.png

# Detailed description of data processing done so far
We filtered through and dropped the years that contained null values for GDP per capita per purchasing power parity (PPP) for a given country. Since only 5% of the data set contained null GDP per capita PPP, abstaining from
using the null years won’t have a huge impact on the analysis. Next, we combined the various meats consumed at each given year for each given country into a “meatball.” This accounts for various cultural, religious, and 
geographical differences between the countries. Ultimately, we wanted to look strictly at the amount of meat with relation to the country’s GDP per capita PPP along with the growth rate of each country’s meatball.

# Detailed description of data modeling methods used so far
We ran a linear regression model with the GDP per capita PPP as the dependent variable and the meatball data as the independent. 

# Preliminary results. (e.g. we fit a linear model to the data and we achieve promising results, or we did some clustering and we notice a clear pattern in the data)
We fit the linear model onto our data and we achieved a promising result. The model suggests that the bigger a country’s meatball, the greater their GDP per capita PPP.  Our r^2 value was 0.51 which further supports the
positive correlation between meatball and GDP/PPP.


