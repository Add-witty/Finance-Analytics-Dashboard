# Personal Finance Analytics Dashboard

An end-to-end data analytics project built using PostgreSQL, SQL, Python, and Metabase.

## Overview

This project analyzes a synthetic personal finance dataset containing 3,000 monthly financial records across 944 users. The objective was to design a dimensional data model, perform exploratory analysis using SQL, and build interactive dashboards to uncover financial behavior patterns.

## Tech Stack

- PostgreSQL
- SQL
- Python (Pandas, SQLAlchemy, Psycopg2)
- Metabase

## Data Model

The raw dataset was transformed into a Star Schema for analytical querying.

### Fact Table
- fact_finance

### Dimension Tables
- dim_date
- dim_category
- dim_income_type
- dim_cashflow
- dim_scenario

### Modeling Features
- Primary Keys
- Foreign Keys
- Indexes for query optimization

## Dashboard Preview

<img width="592" height="668" alt="Screenshot 2026-06-06 at 1 26 21 AM" src="https://github.com/user-attachments/assets/dd91982d-b36e-4397-ac58-f68d5cdfb643" />

<img width="1440" height="900" alt="Screenshot 2026-06-06 at 1 27 37 AM" src="https://github.com/user-attachments/assets/c1fb690c-8ffa-4841-b11c-e902648c1339" />

<img width="808" height="125" alt="Screenshot 2026-06-06 at 1 28 04 AM" src="https://github.com/user-attachments/assets/b9abe863-4b37-419b-816b-a4ea2e713d00" />


## Key Metrics

- Total Financial Records
- Unique Users
- Average Monthly Income
- Average Monthly Expenses

## Dashboard Insights

- Cash Flow Status Distribution
- Financial Stress Distribution
- Users by Income Type
- Transactions by Spending Category
- Monthly Income Trend

## Sample SQL Analysis

### Total Users

sql SELECT COUNT(DISTINCT user_id) FROM fact_finance; 

### Transactions by Category

sql SELECT     dc.category,     COUNT(*) AS total_records FROM fact_finance ff JOIN dim_category dc ON ff.category_id = dc.category_id GROUP BY dc.category ORDER BY total_records DESC; 

<img width="1440" height="900" alt="Screenshot 2026-06-06 at 1 30 04 AM" src="https://github.com/user-attachments/assets/1335f7bc-91ad-4a83-b774-c60574bff53d" />


## Key Learnings

- Data warehouse modeling using Star Schema
- PostgreSQL database design
- Query optimization with indexes
- SQL-based exploratory analysis
- Dashboard development in Metabase

## Future Improvements

- Financial Health Scoring
- Fraud Detection Analysis
- User Segmentation
- Savings Goal Tracking

---
Built by Adwiti Jha
