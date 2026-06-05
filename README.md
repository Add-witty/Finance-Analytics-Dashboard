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

> Add dashboard screenshot here

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
