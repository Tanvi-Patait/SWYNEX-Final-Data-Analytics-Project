import pandas as pd
df = pd.read_csv("data/Iris.csv")
print(df.head())

#Read Rows and Colums
print("Dataset Shape:")
print(df.shape)

#Missing values
print("Missing values:")
print(df.isnull().sum())

#duplicates records
print("Duplicate Records:")
print(df.duplicated().sum())

#Datatypes
print("Data types")
print(df.dtypes)

#Inconsistent values
print("Unique Species Values:")
print(df["Species"].unique())


print("\n--- DATA CLEANING REPORT ---")

print("Total Rows and columns:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nUnique Species Values:")
print(df["Species"].unique())

df.to_csv("data/cleaned_iris.csv",index=False)
print("Cleaned dataset saved successfuly!")