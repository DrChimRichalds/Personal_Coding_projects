import pandas as pd 
import numpy as np



CDC_results = pd.read_csv("data/raw/Full_CDC_Data_.csv")
CDC_results_to_df = pd.DataFrame(CDC_results)
#CDC_results_to_df.info()

# ### Check quality of the data, and clean it up if necessary

# # Dataset overview
# with open("CDC_data_quality_report.txt", "w") as f:

#     f.write(f"Dataset dimensions: {CDC_results_to_df.shape}\n")
#     f.write(f"Number of rows: {CDC_results_to_df.shape[0]}\n")
#     f.write(f"Number of columns: {CDC_results_to_df.shape[1]}\n")
#     f.write(f"Column names: {CDC_results_to_df.columns.tolist()}\n\n")
#     f.write("Data types:\n")
#     f.write(f"{CDC_results_to_df.dtypes}\n\n")
#     f.write("Summary statistics:\n")
#     f.write(f"{CDC_results_to_df.describe(include='all')}\n\n")
#     f.write("Missing values:\n")
#     f.write(f"{CDC_results_to_df.isnull().sum()}\n\n")
#     f.write("Percentage of missing values:\n")
#     f.write(f"{(CDC_results_to_df.isnull().mean() * 100).round(2)}\n\n")
#     f.write("Unique values per column:\n")
#     for col in CDC_results_to_df.columns:
#         f.write(f"{col}: {CDC_results_to_df[col].nunique()}\n")
#     f.write("Duplicate rows:\n")
#     f.write(f"{CDC_results_to_df.duplicated(keep=False).sum()}\n\n")
#     f.write("Duplicate rows details:\n")
#     duplicate_rows = CDC_results_to_df[CDC_results_to_df.duplicated(keep=False)]
#     f.write(f"{duplicate_rows}\n\n")
#     f.write("Blank or whitespace-only strings per column:\n")
#     blank_counts = (
#         CDC_results_to_df.select_dtypes(include="object")
#         .apply(lambda col: col.str.strip().eq("").sum())
#     )
#     f.write(f"{blank_counts}\n\n")  
#     f.write("Identify values outside the expected range for 'Estimate (%)':\n")
#     invalid_coverage = CDC_results_to_df[
#         (CDC_results_to_df["Estimate (%)"] < 0) |  
#         (CDC_results_to_df["Estimate (%)"] > 100)
#     ]
#     f.write(f"{invalid_coverage}\n\n")  


# f.close()

    

# DF_AgeCoverage = CDC_results_to_df[[
#     "Dimension Type",
#     "Dimension",
#     "Estimate (%)",
# ]]

# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace('NR †', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace('NR', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace('†', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace(' ', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace('–', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace('—', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.replace('nan', '', regex=False)
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].dropna()
# DF_AgeCoverage["Estimate (%)"] = DF_AgeCoverage["Estimate (%)"].str.strip()
# DF_AgeCoverage["Estimate (%)"] = pd.to_numeric(DF_AgeCoverage["Estimate (%)"], errors='coerce')
# # print(DF_AgeCoverage.head())

# zero_summary = (
#     DF_AgeCoverage.groupby("Dimension")["Estimate (%)"]
#     .agg(
#         Total="count",
#         Zeros=lambda x: (x == 0).sum(),
#         Mean="mean",
#         Median="median"
#     )
# )

# zero_summary["Zero_Percent"] = (
#     zero_summary["Zeros"] /
#     zero_summary["Total"] * 100
# )

# print(zero_summary)


# def data_quality_report(df):

#     report = pd.DataFrame(index=df.columns)

#     # Data types
#     report["Data_Type"] = df.dtypes.astype(str)

#     # Missing values
#     report["Missing_Count"] = df.isna().sum()

#     # Percentage missing
#     report["Missing_Percent"] = (
#         df.isna().mean() * 100
#     ).round(2)

#     # Unique values
#     report["Unique_Values"] = df.nunique(
#         dropna=True
#     )

#     # Non-missing observations
#     report["Non_Missing_Count"] = df.notna().sum()

#     # Empty strings
#     report["Blank_Strings"] = (
#         df.select_dtypes(include="object")
#         .apply(lambda x: x.str.strip().eq("").sum())
#         .reindex(df.columns, fill_value=0)
#     )

#     # Sort by missing percentage
#     report = report.sort_values(
#         "Missing_Percent",
#         ascending=False
#     )

#     return report


# # Generate report
# quality_report = data_quality_report(CDC_results_to_df)

# print(quality_report)

# # Export report
# quality_report.to_csv(
#     "CDC_data_quality_report.csv"
# )


## Begin cleaning the data, retain the values 


# CDC_results_to_df.to_csv("data/cleaned/Full_CDC_Data_Cleaned.csv", index=False)