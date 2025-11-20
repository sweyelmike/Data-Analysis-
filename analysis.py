# -------------------------------------------------------
# TASK 5: DATA ANALYSIS ON CSV FILES (Corrected for your CSV)
# -------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv("sales_data.csv")

print("----- FIRST 5 ROWS -----")
print(df.head())


# -------------------------------------------------------
# Step 2: BASIC DATA INSIGHTS
# -------------------------------------------------------
print("\n----- SHAPE OF DATA -----")
print(df.shape)

print("\n----- SUMMARY STATISTICS -----")
print(df.describe())

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())


# -------------------------------------------------------
# Step 3: GROUPBY OPERATIONS (Based on your actual columns)
# -------------------------------------------------------

# 1. Total Sales Amount by Region
print("\n----- TOTAL SALES BY REGION -----")
sales_by_region = df.groupby("Region")["Sales_Amount"].sum()
print(sales_by_region)

# 2. Total Sales by Product Category
print("\n----- TOTAL SALES BY PRODUCT CATEGORY -----")
sales_by_category = df.groupby("Product_Category")["Sales_Amount"].sum()
print(sales_by_category)

# 3. Total Sales by Sales Representative
print("\n----- TOTAL SALES BY SALES REP -----")
sales_by_rep = df.groupby("Sales_Rep")["Sales_Amount"].sum()
print(sales_by_rep)


# -------------------------------------------------------
# Step 4: FILTERING ROWS
# -------------------------------------------------------
print("\n----- FILTER: HIGH VALUE SALES (> 8000) -----")
high_sales = df[df["Sales_Amount"] > 8000]
print(high_sales)


# -------------------------------------------------------
# Step 5: VISUALIZATIONS
# -------------------------------------------------------

# BAR CHART – Sales by Region
plt.figure(figsize=(8,5))
sales_by_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.grid(axis="y")
plt.show()

# BAR CHART – Sales by Product Category
plt.figure(figsize=(8,5))
sales_by_category.plot(kind="bar", color="orange")
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Amount")
plt.grid(axis="y")
plt.show()

# BAR CHART – Sales by Sales Representative
plt.figure(figsize=(8,5))
sales_by_rep.plot(kind="bar", color="green")
plt.title("Total Sales by Sales Representative")
plt.xlabel("Sales Rep")
plt.ylabel("Sales Amount")
plt.grid(axis="y")
plt.show()

print("\n✔ TASK COMPLETED SUCCESSFULLY!")
