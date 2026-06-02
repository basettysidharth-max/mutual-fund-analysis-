import pandas as pd

# Load datasets
fund_master = pd.read_csv("01_fund_master.csv")
nav_history = pd.read_csv("02_nav_history.csv")

# Display basic information
print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)

print("\nFund Master Columns:")
print(fund_master.columns)

print("\nNAV History Columns:")
print(nav_history.columns)

# Explore categories
print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

# Missing values check
print("\nMissing Values:")
print(fund_master.isnull().sum())
