import pandas as pd
import numpy as np

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print(df.head())

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nSales Analysis:")
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sales:", df["Sales"].max())

print("\nProfit Analysis:")
print("Total Profit:", df["Profit"].sum())
print("Average Profit:", df["Profit"].mean())
print("Maximum Profit:", df["Profit"].max())

print("\nQuantity Analysis:")
print("Total Quantity:", df["Quantity"].sum())
print("Average Quantity:", df["Quantity"].mean())
print("Maximum Quantity:", df["Quantity"].max())

print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum())

print("\nSub-Category-wise Sales:")
print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))

print("\nRegion-wise Sales:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nDiscount Analysis:")
print("Average Discount:", df["Discount"].mean())
print("Maximum Discount:", df["Discount"].max())

print("\nLoss Analysis:")
print("Loss-making Records:", (df["Profit"] < 0).sum())
print("Total Loss:", df.loc[df["Profit"] < 0, "Profit"].sum())

print("\nTop 5 Highest Profit Records:")
print(df.nlargest(5, "Profit")[["Order ID", "Product Name", "Sales", "Profit"]])

print("\nTop 5 Lowest Profit Records:")
print(df.nsmallest(5, "Profit")[["Order ID", "Product Name", "Sales", "Profit"]])

print("\nSales-Profit Correlation:")
print(df["Sales"].corr(df["Profit"]))

print("\nDate Columns Data Types:")
print(df[["Order Date", "Ship Date"]].dtypes)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


print("\nAfter Date Conversion:")
print(df[["Order Date", "Ship Date"]].dtypes)

print("\nOrder Date Range:")
print("First Order Date:", df["Order Date"].min())
print("Last Order Date:", df["Order Date"].max())

print("\nYear-wise Sales:")
print(df.groupby(df["Order Date"].dt.year)["Sales"].sum())

print("\nYear-wise Profit:")
print(df.groupby(df["Order Date"].dt.year)["Profit"].sum())

# Step 24 - Year-wise Quantity
print("\nYear-wise Quantity:")
print(df.groupby(df["Order Date"].dt.year)["Quantity"].sum())


# Step 25 - Region-wise Profit
print("\nRegion-wise Profit:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))


# Step 26 - Category-wise Profit
print("\nCategory-wise Profit:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))


# Step 27 - Sub-Category-wise Profit
print("\nSub-Category-wise Profit:")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False))


# Step 28 - Top 5 Sales Records
print("\nTop 5 Highest Sales Records:")
print(df.nlargest(5, "Sales")[["Order ID", "Product Name", "Sales", "Profit"]])


# Step 29 - Top 5 Loss Records
print("\nTop 5 Loss Records:")
print(df.nsmallest(5, "Profit")[["Order ID", "Product Name", "Sales", "Profit"]])


# Step 30 - Discount and Profit Relationship
print("\nDiscount-Profit Correlation:")
print(df["Discount"].corr(df["Profit"]))


# Step 31 - Overall Correlation
print("\nCorrelation Matrix:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].corr())


# Step 32 - Check Negative Profit by Category
print("\nNegative Profit by Category:")
print(df[df["Profit"] < 0].groupby("Category")["Profit"].count())


# Step 33 - Check Negative Profit by Sub-Category
print("\nNegative Profit by Sub-Category:")
print(df[df["Profit"] < 0].groupby("Sub-Category")["Profit"].count())


# Step 34 - Final Dataset Information
print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())


print("\nEDA CONCLUSION:")
print("Technology has the highest total sales.")
print("West region has the highest sales.")
print("Technology has the highest total profit.")
print("Higher discount is associated with lower profit.")
print("Some sub-categories generate negative profit.")

print("\nKEY FINDINGS:")
print("1. Total records:", len(df))
print("2. Total sales:", round(df["Sales"].sum(), 2))
print("3. Total profit:", round(df["Profit"].sum(), 2))
print("4. Loss-making records:", (df["Profit"] < 0).sum())
print("5. Highest sales category:", df.groupby("Category")["Sales"].sum().idxmax())
print("6. Highest profit category:", df.groupby("Category")["Profit"].sum().idxmax())
print("7. Highest sales region:", df.groupby("Region")["Sales"].sum().idxmax())

print("\nEDA VALIDATION:")
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

if df.isnull().sum().sum() == 0 and df.duplicated().sum() == 0:
    print("EDA validation successful.")
else:
    print("Please check the dataset for data quality issues.")
