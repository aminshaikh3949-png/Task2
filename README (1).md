# Exploratory Data Analysis (EDA) – Superstore Sales

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Sample Superstore dataset.

The objective is to understand the structure of the dataset, identify trends and patterns, detect data quality issues, and generate meaningful business insights using Python and Pandas.

## Dataset

Dataset: Sample Superstore Sales Dataset

The dataset contains information about:

- Orders
- Customers
- Products
- Categories
- Regions
- Sales
- Quantity
- Discount
- Profit
- Order and Ship Dates

## Tools and Technologies

- Python
- Pandas
- NumPy
- VS Code

## EDA Questions

The analysis focuses on the following questions:

1. What is the overall sales and profit performance?
2. Which product categories generate the highest sales?
3. Which sub-categories generate the highest sales?
4. Which region has the highest sales and profit?
5. How do sales and profit change over the years?
6. Which categories and sub-categories generate negative profit?
7. Is there a relationship between discount and profit?
8. Are there missing values or duplicate records?
9. Which records have the highest and lowest profit?

## Data Analysis Performed

### Dataset Structure

- Checked number of rows and columns
- Examined column names
- Checked data types
- Checked missing values
- Checked duplicate records

### Statistical Analysis

Calculated:

- Total Sales
- Average Sales
- Maximum Sales
- Total Profit
- Average Profit
- Maximum Profit
- Total Quantity
- Average Quantity
- Maximum Quantity

### Category and Region Analysis

Analyzed:

- Category-wise Sales
- Sub-Category-wise Sales
- Region-wise Sales
- Category-wise Profit
- Sub-Category-wise Profit
- Region-wise Profit

### Time Analysis

Converted Order Date and Ship Date into datetime format and analyzed:

- Order date range
- Year-wise Sales
- Year-wise Profit
- Year-wise Quantity

### Profit and Discount Analysis

Analyzed:

- Loss-making records
- Total loss
- Highest profit records
- Lowest profit records
- Discount-Profit correlation
- Overall correlation between Sales, Quantity, Discount and Profit

## Key Findings

- Technology has the highest total sales among the categories.
- West region has the highest sales.
- Technology has the highest total profit.
- Higher discount is associated with lower profit in this dataset.
- Several sub-categories generate negative profit.
- The dataset contains no missing values.
- The dataset contains no duplicate rows.

## Data Quality Validation

The final dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Date conversion

The final validation showed no missing values and no duplicate rows.

## Project Files

- `Sample - Superstore.csv` – Dataset
- `task2_eda.py` – Python EDA source code
- `eda_output.txt` – Generated analysis output
- `README.md` – Project documentation

## Conclusion

The EDA provides an overall understanding of sales, profit, quantity, discount, product categories, regions, and yearly business performance. The analysis also identifies loss-making areas and relationships between important business variables.

## Author

Fareez Khan