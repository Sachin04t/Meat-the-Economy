import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from scipy.stats import entropy
from sklearn.ensemble import RandomForestRegressor



# === Load Data ===
gdp_df = pd.read_csv('GDP per capita PPP.csv')
meat_df = pd.read_csv('Consumption of meat per capita.csv')

meat_columns = ['Poultry', 'Beef', 'Sheep and goat', 'Pork', 'Other meats', 'Fish and seafood']
meat_df['Meatball'] = meat_df[meat_columns].sum(axis=1)

merged_df = pd.merge(meat_df, gdp_df, on=["Entity", "Year"], how="inner")
merged_df.dropna(subset=['GDP per capita, PPP (constant 2017 international $)'], inplace=True)

# === Linear Regression: Meatball vs GDP ===
X = merged_df[['Meatball']]
y = merged_df['GDP per capita, PPP (constant 2017 international $)']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("R² for Meatball:", r2_score(y_test, y_pred))

plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color="#80461B", label='Actual Data')
plt.plot(np.sort(X_test.values.flatten()), np.sort(y_pred), color='red', label='Prediction')
plt.title("Linear Regression: Meatball vs GDP per capita")
plt.xlabel("Meatball")
plt.ylabel("GDP per capita (PPP)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === R² per Meat Type ===
r2_scores = {}
for meat in meat_columns:
    df = merged_df[[meat, 'GDP per capita, PPP (constant 2017 international $)']].dropna()
    X = df[[meat]]
    y = df['GDP per capita, PPP (constant 2017 international $)']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2_scores[meat] = r2_score(y_test, y_pred)

plt.figure(figsize=(10, 6))
plt.bar(r2_scores.keys(), r2_scores.values(), color='mediumseagreen')
plt.title("R² Score: Individual Meat Types vs. GDP per capita PPP")
plt.ylabel("R²")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# === Weighted Meatball ===
weights = {'Poultry': 0.27, 'Beef': 0.20, 'Sheep and goat': 0.03, 'Pork': 0.49, 'Other meats': 0.00, 'Fish and seafood': 0.14}
merged_df['WeightedMeatball'] = sum(merged_df[k] * w for k, w in weights.items())

X = merged_df[['WeightedMeatball']].dropna()
y = merged_df['GDP per capita, PPP (constant 2017 international $)'].loc[X.index]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("R² for Weighted Meatball:", r2_score(y_test, y_pred))

# === KMeans Clustering ===
cluster_df = merged_df[['WeightedMeatball', 'GDP per capita, PPP (constant 2017 international $)']].dropna()
scaled = StandardScaler().fit_transform(cluster_df)
kmeans = KMeans(n_clusters=4, random_state=42)
cluster_df['Cluster'] = kmeans.fit_predict(scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=cluster_df, x='WeightedMeatball', y='GDP per capita, PPP (constant 2017 international $)', hue='Cluster', palette='tab10')
plt.title("KMeans Clustering: Weighted Meatball vs GDP per capita")
plt.tight_layout()
plt.show()

# === DBSCAN Clustering ===
dbscan = DBSCAN(eps=0.1, min_samples=10)
cluster_df['DBSCAN_Cluster'] = dbscan.fit_predict(scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=cluster_df, x='WeightedMeatball', y='GDP per capita, PPP (constant 2017 international $)', hue='DBSCAN_Cluster', palette='tab10')
plt.title("DBSCAN Clustering: Weighted Meatball vs GDP per capita")
plt.tight_layout()
plt.show()


#Bar Graph Rich vs Poor Countries
meat_columns = ['Poultry', 'Beef', 'Sheep and goat', 'Pork', 'Other meats', 'Fish and seafood']
gdp_avg = merged_df.groupby('Entity')['GDP per capita, PPP (constant 2017 international $)'].mean()

num_countries = int(0.10 * len(gdp_avg))
top_countries = gdp_avg.sort_values(ascending=False).head(num_countries).index

bottom_countries = gdp_avg.sort_values(ascending=True).head(num_countries).index
top_meat = merged_df[merged_df['Entity'].isin(top_countries)][meat_columns].mean()
bottom_meat = merged_df[merged_df['Entity'].isin(bottom_countries)][meat_columns].mean()

top_meat_pct = top_meat / top_meat.sum()
bottom_meat_pct = bottom_meat / bottom_meat.sum()

import matplotlib.pyplot as plt
import numpy as np

labels = meat_columns
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, top_meat_pct, width, label='Top 10% GDP')
bars2 = ax.bar(x + width/2, bottom_meat_pct, width, label='Bottom 10% GDP')

ax.set_ylabel('Proportion of Total Meat (%)')
ax.set_title('Meat Type Composition: Rich vs Poor Countries')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# === Entropy Plot ===
meat_props = merged_df[meat_columns].div(merged_df[meat_columns].sum(axis=1), axis=0)
merged_df['Meat_Entropy'] = meat_props.apply(lambda row: entropy(row.dropna()), axis=1)

sns.scatterplot(data=merged_df, x='Meat_Entropy', y='GDP per capita, PPP (constant 2017 international $)', alpha=0.5)
plt.title("Meat Diversity (Entropy) vs GDP per Capita")
plt.grid(True)
plt.tight_layout()
plt.show()

# === PCA of Meat Types ===
latest_meat = merged_df.groupby("Entity")[meat_columns].mean().dropna()
scaled_meat = StandardScaler().fit_transform(latest_meat)
pca_result = PCA(n_components=2).fit_transform(scaled_meat)
pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"], index=latest_meat.index)
pca_df["GDP"] = merged_df.groupby("Entity")["GDP per capita, PPP (constant 2017 international $)"].mean()
sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="GDP", palette="viridis")
plt.title("PCA of Meat Type Profiles (Colored by GDP)")
plt.grid(True)
plt.tight_layout()
plt.show()


#Meat Trends Over Time
countries = ['Egypt', 'United States', 'Brazil', 'Japan', 'Nigeria']
for country in countries:
    df = merged_df[merged_df['Entity'] == country].sort_values('Year')
    df[meat_columns].set_index(df['Year']).plot(figsize=(10,5), title=f"{country}: Meat Type Trends Over Time")
    plt.ylabel("kg per capita")
    plt.grid(True)
    plt.show()

#Avg Meat Consumption by Religion

# Sample religion labels
religion_map = {
    'India': 'Hindu',
    'Pakistan': 'Muslim',
    'USA': 'Christian',
    'Brazil': 'Christian',
    'Egypt': 'Muslim',
    'Japan': 'Secular',
    'Indonesia': 'Muslim',
    'Nigeria': 'Mixed',
    'Germany': 'Christian',
    'Saudi Arabia': 'Muslim',
}

# Add religion column
merged_df['Religion'] = merged_df['Entity'].map(religion_map)

# Average meat types per religion
religion_meat = merged_df.groupby('Religion')[meat_columns].mean()

religion_meat.T.plot(kind='bar', figsize=(12,6))
plt.title("Average Meat Composition by Religion")
plt.ylabel("kg per capita")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()



#Predictive Model

# Make sure meat_columns is already defined and merged_df exists
meat_columns = ['Poultry', 'Beef', 'Sheep and goat', 'Pork', 'Other meats', 'Fish and seafood']

# Add lagged GDP
merged_df['GDP_Lag'] = merged_df.groupby('Entity')['GDP per capita, PPP (constant 2017 international $)'].shift(1)

# Compute meat consumption trend slopes per country
temp_df = merged_df.copy()
for meat in meat_columns:
    trend_col = f"{meat}_trend"
    temp_df[trend_col] = np.nan
    for country in temp_df['Entity'].unique():
        country_data = temp_df[temp_df['Entity'] == country]
        if len(country_data) >= 5:
            slope = np.polyfit(country_data['Year'], country_data[meat], 1)[0]
            temp_df.loc[temp_df['Entity'] == country, trend_col] = slope
merged_df = temp_df.copy()

# Compute Meat Entropy (if not already done)
meat_props = merged_df[meat_columns].div(merged_df[meat_columns].sum(axis=1), axis=0)
merged_df['Meat_Entropy'] = meat_props.apply(lambda row: entropy(row.dropna()), axis=1)

# Feature set
trend_features = [f"{meat}_trend" for meat in meat_columns]
feature_cols = meat_columns + ['Meatball', 'Meat_Entropy', 'GDP_Lag'] + trend_features

features = merged_df[feature_cols]
target = merged_df['GDP per capita, PPP (constant 2017 international $)']

# Drop rows with missing values
valid_rows = features.dropna().index
X = features.loc[valid_rows]
y = target.loc[valid_rows]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Random Forest model
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Plot predicted vs actual
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolor='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual GDP per capita")
plt.ylabel("Predicted GDP per capita")
plt.title("Random Forest Predictions vs Actual")
plt.grid(True)
plt.tight_layout()
plt.show()

input("Press Enter to exit...")

