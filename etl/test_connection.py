from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://adwitijha@localhost:5432/finance_analytics"
)

try:
    with engine.connect() as conn:
        print("Connected successfully!")
except Exception as e:
    print("Connection failed:")
    print(e)