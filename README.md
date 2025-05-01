<!-- README.md -->

<h1 align="center">🥩 Meat-the-Economy <br><sub>using the <em>Meatmerizor</em> model</sub></h1>

<p align="center">
  <a href="https://www.youtube.com/watch?v=eEIQnOcHQdU">
    <img alt="demo-video" src="https://img.shields.io/badge/🎬-Watch Demo-red?logo=youtube">
  </a>
  <img alt="python" src="https://img.shields.io/badge/Made with-Python-blue?logo=python">
</p>

> **Predicting economic trends one 🥩 at a time**

---
### Instructions for Building and Running our Code
1. **Clone this repository** or download the following files into the same folder:
   - `cs506_meattheeconomy.py`
   - `requirements.txt`
   - `GDP per capita PPP.csv`
   - `Consumption of meat per capita.csv`

2. **Run the Makefile** using Git Bash (or any terminal with `make` installed):
   - **use commands:**
     - make install
     - make run
       
3. **Important Warning**
 
  - This project uses **SHAP** to generate model explainability plots.

  - SHAP can be **resource-intensive** and may not work reliably on machines without a compatible GPU or proper `torch` installation.

  - If you experience issues running SHAP (e.g., the script hangs, your computer slows down, or a plot window won’t close), you can safely skip the SHAP explanation by:

       1. **Force quitting the terminal or pressing `Ctrl + C`** to stop execution
       2. **Commenting out the `import shap` line and the SHAP block** in `cs506_meattheeconomy.py`

  - ✅ The main analysis and all other plots will still work without SHAP so you won’t lose any critical results by skipping the SHAP explanation.
    
---

## 📜 Table of Contents
|                                                                                                 |                                                                                                      |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------:|
|[Video link](#video-link)                                                                        |[Rich vs Poor Meat Composition](#meat-type-composition-rich-vs-poor-individual-meats)                 |
|[Project Description](#project-description)                                                      |[Meat Diversity (Entropy)](#meat-diversity-entropy-vs-gdp-per-capita)                                 |
|[Project Goals](#project-goals)                                                                  |[PCA of Meat Types](#pca-of-meat-types-individual-meats-colored-by-gdp)                               |
|[Data Collection](#data-collection)                                                              |[Country Spotlights](#country-spotlights---diet-development)                                                                                                      |
|[Detailed description of data processing](#detailed-description-of-data-processing)              |[Average Meat Composition by Religion](#average-meat-composition-by-religion-individual-meats)        |
|[Detailed description of data modeling methods](#detailed-description-of-data-modeling-methods)  |[Random Forest Predictor](#random-forest-prediction-of-gdp-using-meat-consumption-along-with-past-gdp)|
|[R^2 Results for Individual Meats](#r2-results-for-individual-meats)                             |[SHAP Values for Predictor](#average-shap-values-shapley-values)                                   |
|[Kmeans Clustering Results](#kmeans-clustering-results-meatballs-and-gdp-per-capita)             |[Meat the Team](#about-us)                                                                            |
|[DBSCAN Results](#dbscan-results-meatballs-and-gdp-per-capita)                                   |                                                                                                      |

---

### Project Description
**The Meatmerizor** is a model that can predict the economic state of a country based on previous data of the country’s meat consumption and economic data.  
More specifically, the Meatmerizor takes in a country’s meat consumption per capita along with GDP per capita PPP for a given year in order to predict future trends. 

---

### Project Goals
- **Quantify the relationship** between meat consumption and economic growth.
- **Model economic patterns** using linear regression and clustering techniques.
- **Interpret findings** through the lens of cultural factors (e.g., religion) and dietary diversity (entropy).

---

### Data Collection
- **National meat eating history (From Kaggle)** 
- **Global GDP per capita, PPP data (From Kaggle)**

Datasets:  
https://www.kaggle.com/datasets/scibearia/meat-consumption-per-capita

---

### Detailed description of data preparation

- **Data Cleaning**: Removed records with missing GDP or meat values. (5% of the data set contained null GDP per capita PPP, abstaining from using the null years won’t have a huge impact on the analysis)
- **Feature Engineering**:
   - **Meatball**: Total per capita meat consumption.
   - **Meat Entropy**: Shannon entropy to capture meat diversity per country-year.
   - **GDP Lag**: Previous year’s GDP to reflect economic momentum.
   - **Meat Trend Slopes**: Computed per-country, per-meat trends over time.
- **Merging**: Combined cleaned meat and GDP datasets by country and year.
- **Normalization**: Applied scaling where appropriate for clustering and PCA.

---

### Detailed description of data modeling methods 
We implemented a variety of modeling techniques to analyze and predict the relationship between meat consumption and GDP:

- **Linear Regression**: Initially used to explore the Meatball–GDP relationship (R² ≈ 0.51).
- **Weighted Meatball Score**: Improved predictive power by weighting meat types based on individual R² scores (R² ≈ 0.55).
- **Clustering Models**:
  - **KMeans** revealed macro patterns in global dietary-economic groupings.
  - **DBSCAN** uncovered finer distinctions and outlier countries.
- **Random Forest Regressor**:
  - Trained on meat type trends, meatball score, entropy, and GDP lag.
  - Achieved strong performance (**R² ≈ 0.73**), showing meat data alone is a robust economic signal.
- **SHAP (SHapley Additive Values)**:
  - Interpreted feature importance.
  - Confirmed **GDP lag**, **meatball**, and **poultry trend** were dominant drivers of predictions.

This modeling progression helped us move from correlation-based insight to fully interpretable economic prediction.

---

### Linear Regression (Meatball)
![Linear Regression Graph](Graphs/LinearRegressionGraph)


---

### R^2 Results for Individual Meats
- R² for Poultry: 0.2709
- R² for Beef: 0.2062
- R² for Sheep and goat: 0.0279
- R² for Pork: 0.4859
- R² for Other meats: -0.0001
- R² for Fish and seafood: 0.1376

![R^2 Individual Meats](Graphs/R^2IndividualMeats)

- R² Score for Weighted Meatball: 0.5545

While the original meatball score provided a general signal (R² ≈ 0.51), creating a weighted average based on individual meat type performance raised the model’s explanatory power to R² = 0.5545. This indicates that pork and poultry, for example, are more predictive of GDP levels than other meats like sheep or fish, and the model improves when this is reflected in the data representation.

---

### Kmeans Clustering results. (Meatballs and GDP per capita)
![KMeans Clustering](Graphs/KmeansGraphMeatball)

KMeans clustering revealed four global country profiles based on GDP and weighted meat consumption. One cluster captured low-GDP, low-meatball nations, often limited by cultural or structural barriers to meat access. Another grouped developing economies with rising meat intake, signaling growing industrial food capacity. A third cluster highlighted wealthy, high-meatball countries with Western-style diets and strong agricultural infrastructure. Finally, a small elite cluster included extremely rich nations with high meat diversity, reflecting both affluence and globalized consumption.

Cluster <br>  
0    [Albania, Antigua and Barbuda, Argentina, Armenia]  <br>
1    [Antigua and Barbuda, Australia, Austria, Baha...]  <br>
2     [Afghanistan, Albania, Algeria, Angola, Armenia]  <br>
3         [Bermuda, Ireland, Luxembourg, Macao, Qatar]  <br>
Name: Entity, dtype: object

---

### DBSCAN results. (Meatballs and GDP per capita)
![DBSCAN Clustering](Graphs/DBSCANMeatballs)

Cluster -1: ['Antigua and Barbuda' 'Austria' 'Bahamas' 'Bahrain' 'Belgium'] <br>
Cluster 0: ['Afghanistan' 'Albania' 'Algeria' 'Angola' 'Antigua and Barbuda'] <br>
Cluster 1: ['Austria' 'Denmark' 'Spain'] <br>
Cluster 2: ['Belgium' 'Denmark' 'Ireland' 'Netherlands' 'Norway'] <br>
Cluster 3: ['Brunei' 'Switzerland'] <br>
Cluster 4: ['Bahamas' 'Croatia' 'Poland' 'Portugal' 'Spain'] <br> 
Cluster 5: ['Israel' 'New Zealand' 'Panama' 'Slovakia' 'Trinidad and Tobago'] <br>
Cluster 6: ['Bermuda' 'Norway' 'Switzerland'] <br>
Cluster 7: ['Saint Lucia' 'Saint Vincent and the Grenadines']


|DBSCAN_Cluster  |   WeightedMeatball | GDP per capita, PPP (constant 2017 international $)|
|----------------|-------------------:|---------------------------------------------------:|
|-1              |28.056932           |49359.614343                                        |
|0               |12.585853           |12853.347468                                        |
|1               |37.575794           |38839.518000                                        |
|2               |24.093620           |52637.827727                                        |
|3               |21.595027           |70663.221250                                        |
|4               |33.670416           |30578.904682                                        |
|5               |17.865095           |27974.776857                                        |
|6               |24.497552           |63758.010111                                        |
|7               |29.962399           |14131.533455                                        |


DBSCAN revealed micro-communities of economic/meat behavior that KMeans blurred out — such as “rich but moderate meat” countries (Cluster 2) vs “rich and very meaty” (Cluster 1).
Small wealthy nations (e.g. Bermuda, Brunei) tend to form their own clusters — likely due to tourism, imports, or elite consumption patterns.
Cluster 0 represents the bulk of lower-to-middle income nations, reinforcing meat as a luxury signal in global food systems.
Meatball score still matters: countries with scores over 30 consistently map to higher GDP clusters or noise (elite states).
Meanwhile, the highest GDP countries with low meatball scores didn’t even cluster well — they were marked as outliers, reinforcing their uniqueness.

---

### Meat Type Composition: Rich vs Poor. (Individual Meats)
![Meat Type Composition: Rich vs Poor](Graphs/MeatTypeByRichandPoor)

While wealthier nations consume more meat overall, their diet composition is also distinct. Richer countries lean heavily on pork and poultry — meats typically associated with industrial farming and Westernized dietary patterns — while poorer countries consume more beef, goat, and fish, likely driven by regional availability, cultural practices, and economic access.

---

### Meat Diversity (Entropy) vs GDP per Capita
![Meat Entropy vs GDP per Capita](Graphs/MeatEntropyVsGDPPerCapita)

This entropy-based analysis suggests that dietary diversity may serve as a proxy for a country's position in the globalized economy. Nations with limited meat variety appear structurally constrained (by geography, religion, or supply chains) while those with higher entropy demonstrate the logistical and cultural infrastructure of developed economies.

---

### PCA of Meat Types (Individual meats, colored by GDP)
![PCA of Meat Profiles](Graphs/PCAOfMeatProfilesByGDP)

PCA reveals that meat consumption profiles are not randomly distributed. Instead, GDP stratifies countries along a dietary axis dominated by pork and poultry. This suggests that economic growth is often accompanied by dietary convergence (toward a Westernized, industrial meat standard) potentially at the expense of cultural diversity.

---

### Country Spotlights - Diet Development
<div style="overflow-x: auto; white-space: nowrap;">
  <img src="Graphs/EgyptMeatTrend" alt="Egypt Meat Trend" width="300" style="display: inline-block; margin-right: 10px;" />
  <img src="Graphs/UnitedStateMeaTTrend" alt="U.S. Meat Trend" width="300" style="display: inline-block; margin-right: 10px;" />
  <img src="Graphs/BrazilMeatTrend" alt="Brazil Meat Trend" width="300" style="display: inline-block; margin-right: 10px;" />
  <img src="Graphs/JapanMeatTrend" alt="Japan Meat Trend" width="300" style="display: inline-block; margin-right: 10px;" />
  <img src="Graphs/NigeriaMeatTrend" alt="Nigeria Meat Trend" width="300" style="display: inline-block; margin-right: 10px;" />
</div>

- Egypt’s meat evolution reflects an economically responsive, religiously bound system: high fish suggests coastal dependence, rising poultry signals industrialization.
- The US shows what happens after dietary industrialization peaks — poultry optimization, beef retreat, and little cultural incentive to diversify
- Brazil exemplifies the economic transition pathway: from cattle dominance → poultry surge → slight dietary diversification.
- Japan proves that you can develop economically while retaining cultural dietary roots — meat diversification here is measured, not disruptive.
- Nigeria reflects a resource-dependent diet vulnerable to shocks (climate, imports, conflict). Low meat diversity = food system fragility.

## This shows...

- Poultry is the first industrial step as countries develop
- Beef shrinks as economies mature or costs rise
- Fish is versatile: cultural in Japan, fallback in Nigeria, trade-driven in Egypt
- Pork only thrives where religion allows it
- Meat transitions are not linear — they reflect identity, geography, and infrastructure

---

### Average Meat Composition by Religion (Individual meats)
![Avg Meat Composition by Religion](Graphs/AvgMeatByReligion)

The structure of meat consumption across countries reflects long-standing religious taboos, philosophical values, and substitution strategies. Secular and Christian-majority nations tend toward industrial meat diversity, while Muslim and Hindu populations shape diets through prohibitions and adaptations, often reinforcing regional protein alternatives like fish, goat, or poultry.

---

### Random Forest Prediction of GDP (Using meat consumption along with past GDP)
![Random Forest Prediction vs Actual](Graphs/RandomForestPredictionsVsActual.png)

## Features we trained on
- Individual meat types
- Total per capita meat consumption (Meatball)
- Meat Entropy (a measure of dietary diversity)
- GDP Lag (previous year’s GDP)
- Year-over-year trends in meat consumption per type

The model worked exceptionally with an R^2 Score: 0.9947286920285141 and RMSE: $1422.8991966523777


### Average |SHAP| Values (Shapley Values)
![Features Vs Mean(|SHAP|)](Graphs/FeaturesVsMeanSHAPValues.png)

To interpret the model’s predictions, we used SHAP values — a game-theory-based tool that explains how much each feature contributes to a prediction. See: https://shap.readthedocs.io/en/latest/example_notebooks/tabular_examples/tree_based_models/Python%20Version%20of%20Tree%20SHAP.html#Train-sklearn-random-forest

Key takeaways from the SHAP analysis:
- GDP Lag is by far the most influential feature, highlighting that economic momentum is a major driver of current GDP.
- Meatball score and Meat Entropy were also high-impact, suggesting that both the volume and diversity of meat consumption are meaningful economic signals.
- Among individual meats, poultry trend emerged as the strongest predictor — likely due to poultry's widespread adoption and affordability during economic transitions.
- Lower-impact meats (like sheep or fish) reflected more regional or culturally constrained signals.

---
### About Us
<details>
<summary>🤝 <strong>Meat the Team</strong></summary>

1. Kaizia: I am a Computer Science major with a minor in Biology and my favorite meat dish is Oxtail.
2. Yeabsera: I am a Data Science and Political Science major with a minor in Public Policy Analysis and my favorite meat dish is Tibs(Ethiopian dish). 
3. Adham: I am a Data Science major and my favorite meat dish is Crab Legs.   
4. Sachin: I am Computer Science major and my favorite meat dish right now is Crispy Pork Belly.

Thanks for helping make the Meatmerizor sizzle! 🔥
</details>

---
<p align="center">Made with ❤ and 🥩 by the Meatmerizor team</p>

