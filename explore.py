# Self-Assessment
# 1. A boolean filter checks each row against a condition and keeps the rows
#    where the condition is True.
# 2. df["revenue"] is a Series; df[["revenue"]] is a one-column DataFrame.
#    Use the Series for a single column of values, or the DataFrame when you
#    need to keep a table structure or select multiple columns.
# 3. Pandas makes it easy to repeat filters, sorts, and calculations across
#    thousands of rows consistently, without doing each step by hand.

import pandas as pd

# Exercise 1: Load and inspect the data
df = pd.read_csv("data/retail_sales.csv")

print("Exercise 1: First five rows")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:")
print(df.dtypes)

# Exercise 2: Filter by region
south = df[df["region"] == "South"]

print("\nExercise 2: South region")
print("Number of South rows:", len(south))
print(south.head())

# Exercise 3: Find the five highest-revenue orders
top_five = df.sort_values("revenue", ascending=False).head(5)

print("\nExercise 3: Top five by revenue")
print(top_five)

# Exercise 4: Filter by region and revenue
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print("\nExercise 4: South orders over $1,000")
print("Number of matching rows:", len(big_south))
print(big_south.head(5))

# Exercise 5: Add a per-unit revenue column
df["per_unit"] = df["revenue"] / df["quantity"]

print("\nExercise 5: Per-unit revenue")
print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())

# Exercise 6: Show unique regions and their counts
print("\nExercise 6: Region values")
print(df["region"].unique())
print(df["region"].value_counts())

# Exercise 7: Select a subset of columns
sales_subset = df[["region", "product", "revenue"]]

print("\nExercise 7: Selected columns")
print("Shape:", sales_subset.shape)

# Exercise 8: Save the updated DataFrame
df.to_csv("data/explored.csv", index=False)
print("\nExercise 8: Saved data/explored.csv")