import pandas as pd
from sqlalchemy import create_engine

# Read dataset
df = pd.read_csv("dataset/personal-finance-dataset.csv")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://adwitijha@localhost:5432/finance_analytics"
)

# Load dataframe into PostgreSQL
df.to_sql(
    "finance_raw",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")