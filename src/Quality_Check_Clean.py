import pandas as pd 
import numpy as np



CDC_results = pd.read_csv("data/raw/cdc_results.csv")
CDC_results_to_df = pd.DataFrame(CDC_results)
#CDC_results_to_df.info()

# ### Check quality of the data, and clean it up if necessary

# # Dataset overview
# print("Dataset dimensions:", CDC_results_to_df.shape)

# # Number of rows and columns
# print("Rows:", CDC_results_to_df.shape[0])
# print("Columns:", CDC_results_to_df.shape[1])

# # Column names
# print(CDC_results_to_df.columns.tolist())

# # Data types and non-null counts
# CDC_results_to_df.info()

# # Summary statistics
# print(CDC_results_to_df.describe(include="all"))


# # Count missing values in each column
# missing_values = CDC_results_to_df.isnull().sum()
# print("Missing values in each column:\n", missing_values)


# # Calculate percentage of missing values
# missing_percent = (
#     CDC_results_to_df.isnull().mean() * 100
# )

# # Combine into a DataFrame
# missing_summary = pd.DataFrame({
#     "Missing_Count": missing_values,
#     "Missing_Percent": missing_percent
# })

# # Sort from highest to lowest missingness
# missing_summary = missing_summary.sort_values(
#     by="Missing_Percent",
#     ascending=False
# )

# print(missing_summary)


# Display unique values in each object column

# for col in CDC_results_to_df.select_dtypes(include="object").columns:
#     print(f"\n{col}")
#     print(CDC_results_to_df[col].value_counts(dropna=False))

# # Count blank or whitespace-only strings
# blank_counts = (
#     CDC_results_to_df.select_dtypes(include="object")
#     .apply(lambda col: col.str.strip().eq("").sum())
# )

# print(blank_counts)

# # Count duplicate rows
# duplicates = CDC_results_to_df.duplicated().sum()

# print("Number of duplicate rows:", duplicates)

# # Display duplicates
# duplicate_rows = CDC_results_to_df[
#     CDC_results_to_df.duplicated(keep=False)
# ]

# print(duplicate_rows)

# Convert coverage estimates to numeric
# CDC_results_to_df["coverage_estimate"] = pd.to_numeric(
#     CDC_results_to_df["coverage_estimate"]
#         .astype("string")
#         .str.replace("%", "", regex=False),
#     errors="coerce"
# )

# # Identify values outside the expected range
# invalid_coverage = CDC_results_to_df[
#     (CDC_results_to_df["coverage_estimate"] < 0) |
#     (CDC_results_to_df["coverage_estimate"] > 100)
# ]

# print(f"Invalid coverage estimates:\n{invalid_coverage}")

### there is nothign to clean but I will write a clean version of a file to practice saving a cleaned version of the data.

CDC_results_to_df.to_csv("data/processed/cdc_results_clean.csv", index=False)
