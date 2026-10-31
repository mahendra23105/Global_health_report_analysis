# Global Happiness Report Analysis
# A simple Python project to study happiness in different countries.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
file_name = "world_happiness.csv"
data = pd.read_csv(file_name)

print("First five rows of the dataset:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())

# Remove rows where important values are missing
columns = [
    "Life Ladder",
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth"
]

data = data.dropna(subset=columns)

# Calculate average happiness score by country
country_happiness = data.groupby("Country name")["Life Ladder"].mean()
country_happiness = country_happiness.sort_values(ascending=False)

print("\nTop 10 happiest countries:")
print(country_happiness.head(10))

print("\nBottom 10 countries:")
print(country_happiness.tail(10))

# Bar chart: Top 10 happiest countries
plt.figure(figsize=(10, 5))
country_happiness.head(10).sort_values().plot(kind="barh", color="skyblue")
plt.title("Top 10 Happiest Countries")
plt.xlabel("Average Happiness Score")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_10_happiest_countries.png")
plt.show()

# Scatter plot: GDP and happiness
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="Log GDP per capita", y="Life Ladder")
plt.title("GDP per Capita vs Happiness")
plt.xlabel("Log GDP per Capita")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.savefig("gdp_vs_happiness.png")
plt.show()

# Scatter plot: Social support and happiness
plt.figure(figsize=(8, 5))
sns.scatterplot(data=data, x="Social support", y="Life Ladder")
plt.title("Social Support vs Happiness")
plt.xlabel("Social Support")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.savefig("social_support_vs_happiness.png")
plt.show()

# Scatter plot: Life expectancy and happiness
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=data,
    x="Healthy life expectancy at birth",
    y="Life Ladder"
)
plt.title("Life Expectancy vs Happiness")
plt.xlabel("Healthy Life Expectancy")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.savefig("life_expectancy_vs_happiness.png")
plt.show()

# Correlation between the main columns
print("\nCorrelation with happiness score:")
print(data[columns].corr()["Life Ladder"].sort_values(ascending=False))

print("\nAnalysis completed!")
