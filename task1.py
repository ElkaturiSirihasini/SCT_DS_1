import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\Siri\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_346039\API_SP.POP.TOTL_DS2_en_csv_v2_346039.csv",
    skiprows=4
)

# Select required columns
data = df[["Country Name", "2022"]].dropna()

# Remove rows that are not countries
exclude = [
    "World",
    "IDA & IBRD total",
    "Low & middle income",
    "Middle income",
    "IBRD only",
    "Early-demographic dividend",
    "Lower middle income",
    "Upper middle income",
    "East Asia & Pacific",
    "Late-demographic dividend"
]

data = data[~data["Country Name"].isin(exclude)]

# Get top 10
top10 = data.sort_values(by="2022", ascending=False).head(10)

print(top10)

# Create chart
plt.figure(figsize=(12, 6))
plt.bar(top10["Country Name"], top10["2022"])

plt.title("Top 10 Most Populous Countries (2022)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("population_chart.png", dpi=300)
plt.show()
