import pandas as pd

df = pd.read_csv("dataset/personal-finance-dataset.csv")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary:")
print(df.describe())