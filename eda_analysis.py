import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_iris.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Dataset information
print("\nDataset Shape:")
print(df.shape)

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Species count
print("\nSpecies Count:")
print(df["Species"].value_counts())


import matplotlib.pyplot as plt
import seaborn as sns

# Create one figure with three charts
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1: Species Count
sns.countplot(data=df, x="Species", ax=axes[0])
axes[0].set_title("Count of Each Iris Species")
axes[0].set_xlabel("Species")
axes[0].set_ylabel("Number of Flowers")
axes[0].tick_params(axis="x", rotation=45)

# Chart 2: Sepal Length by Species
sns.boxplot(data=df, x="Species", y="SepalLengthCm", ax=axes[1])
axes[1].set_title("Sepal Length by Iris Species")
axes[1].set_xlabel("Species")
axes[1].set_ylabel("Sepal Length (cm)")
axes[1].tick_params(axis="x", rotation=45)

# Chart 3: Petal Length vs Petal Width
sns.scatterplot(
    data=df,
    x="PetalLengthCm",
    y="PetalWidthCm",
    hue="Species",
    ax=axes[2]
)
axes[2].set_title("Petal Length vs Petal Width")
axes[2].set_xlabel("Petal Length (cm)")
axes[2].set_ylabel("Petal Width (cm)")

plt.tight_layout()
plt.show()
