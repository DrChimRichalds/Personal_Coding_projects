
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#### I want to generate box plots and histograms of the of the data

CDC_results = pd.read_csv("data/raw/Full_CDC_Data_.csv")
CDC_results_to_df = pd.DataFrame(CDC_results)
#CDC_results_to_df.info()


# CDC_results_to_df[['CI_lower', 'CI_upper']] = (
#     CDC_results_to_df['_95_ci']
#     .str.split(' to ', expand=True)
# )
# CDC_results_to_df['CI_lower'] = pd.to_numeric(CDC_results_to_df['CI_lower'], errors='coerce')
# CDC_results_to_df['CI_upper'] = pd.to_numeric(CDC_results_to_df['CI_upper'], errors='coerce')

## Geography based histogram 
# geography = CDC_results_to_df["Geography"]
# geography.value_counts().plot(kind='bar', title='Geography Distribution')
# plt.xlabel("Geography")
# plt.ylabel("Count") 
# plt.show()



#Filtering the data to only include coverage estimates that are not null and are numeric
# coverage_estimates = CDC_results_to_df["Estimate (%)"]
# coverage_estimates = coverage_estimates.str.replace('NR †', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('NR', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('†', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace(' ', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('–', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('—', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('nan', '', regex=False)
# coverage_estimates = coverage_estimates.dropna()
# coverage_estimates = coverage_estimates.str.strip()
# coverage_estimates = pd.to_numeric(coverage_estimates, errors='coerce')
# print(coverage_estimates.unique())



# coverage_estimates.hist(bins=20, edgecolor='black')
# print("Histogram of Coverage Estimates")
# plt.title("Histogram of Coverage Estimates")
# plt.xlabel("Coverage Estimates", fontsize=15)
# plt.xticks(rotation=45)
# plt.ylabel("Frequency", fontsize=15)
# plt.locator_params(axis='x', nbins=5)
# plt.show()

# population_sample_sizes = CDC_results_to_df["Sample Size"]
# population_sample_sizes = population_sample_sizes.dropna()
# population_sample_sizes.info()



# population_sample_sizes.hist(bins=50, edgecolor='black')
# print("Histogram of Population Sample Sizes")
# plt.title("Histogram of Population Sample Sizes")
# plt.xlabel("Population Sample Size")
# plt.ylabel("Frequency")
# plt.show()

##T this is not very helpful because the sample sizes are very large and the histogram is not very informative.
# boxplot = CDC_results_to_df.boxplot(by = "Sample Size", grid = True)
# print("Boxplot of Sample Sizes")
# plt.title("Boxplot of Sample Sizes")
# plt.xlabel("Sample Size")
# plt.ylabel("Frequency")
# plt.show()

# confidence_intervals = CDC_results_to_df["_95_ci"]
# conditional_intervals = confidence_intervals.str.replace('to', '', regex=False)

### many subplots for the different dimensions of the data, each with their own histogram of coverage estimates
# CDC_results_to_df.info()


DF_AgeCoverage = CDC_results_to_df[[
    "Dimension Type",
    "Dimension",
    "Estimate (%)",
    "Month"
]]

# Preserve original data
DF_AgeCoverage["Estimate_Original"] = DF_AgeCoverage["Estimate (%)"]

# Remove footnote symbols and whitespace
clean_estimate = (
    DF_AgeCoverage["Estimate (%)"]
    .astype("string")
    .str.replace("†", "", regex=False)
    .str.replace("‡", "", regex=False)
    .str.strip()
)

# Convert NR and other non-numeric entries to missing values
clean_estimate = clean_estimate.replace(
    ["NR", "N/A", "nan", ""], pd.NA
)

# Convert to numeric
DF_AgeCoverage["Estimate (%)"] = pd.to_numeric(
    clean_estimate, errors="coerce"
)
########


# # Count numeric zeros
# print(
#     "Number of zero estimates:",
#     (DF_AgeCoverage["Estimate (%)"] == 0).sum()
# )

# # Count missing values
# print(
#     "Number of missing estimates:",
#     DF_AgeCoverage["Estimate (%)"].isna().sum()
# )

# # Inspect original values associated with zero estimates
# zero_estimates = DF_AgeCoverage[
#     DF_AgeCoverage["Estimate (%)"] == 0
# ]

# print(zero_estimates[
#     ["Estimate_Original", "Estimate (%)"]
# ])
# print(DF_AgeCoverage.head())

zero_estimates = DF_AgeCoverage[
    DF_AgeCoverage["Estimate (%)"] == 0
]

#print(zero_estimates["Estimate_Original"].value_counts(dropna=False))

# print(zero_estimates.head())

# print(
#     zero_estimates.groupby("Dimension")["Estimate (%)"]
#     .agg(["count"])
# )

race_groups = [
    "Black, Non-Hispanic",
    "Hispanic",
    "White, Non-Hispanic"
]

race_data = DF_AgeCoverage[
    DF_AgeCoverage["Dimension"].isin(race_groups)
]

# print(
#     race_data.groupby("Dimension")["Estimate (%)"]
#     .agg(
#         Total="count",
#         Exact_Zeros=lambda x: (x == 0).sum(),
#         Near_Zero=lambda x: ((x > 0) & (x <= 5)).sum(),
#         Minimum="min",
#         Median="median",
#         Maximum="max"
#     )
# )

# near_zero_data = race_data[
#     race_data["Estimate (%)"] <= 5
# ]

# print(
#     near_zero_data.groupby(
#         ["Dimension", "Month"]
#     ).size()
# )

print(CDC_results_to_df["Vaccine"].unique())

monthly_summary = (
    race_data
    .groupby(["Dimension", "Month"])["Estimate (%)"]
    .agg(["count", "mean", "median"])
    .reset_index()
)

#print(monthly_summary.to_string(index=False))

sns.lineplot(
    data=monthly_summary,
    x="Month",
    y="median",
    hue="Dimension",
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Median Vaccination Coverage (%)")
plt.title("Vaccination Coverage by Month and Race")
plt.show()


# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# ### use this to examien the data for different dimensions of the data, and create histograms for each dimension
# print(CDC_results_to_df["Dimension"].unique())

# dimensions = [
#     'Black, Non-Hispanic',
#                                                 'Hispanic',
#                    'Other or Multiple Races, Non-Hispanic',
#                                      'White, Non-Hispanic',
#                                              '50-64 Years',
#                                               '>=65 Years',
#                                               '>=6 Months',
#                                      '6 Months - 17 Years',
#                                       '6 Months - 4 Years',
#                                               '5-12 Years',
#                                              '13-17 Years',
#                                               '>=18 Years',
#                                              '18-64 Years',
#                                 '18-64 Years at High Risk',
#                             '18-64 Years not at High Risk',
#                                              '18-49 Years',
#                                 '18-49 Years at High Risk',
#                             '18-49 Years not at High Risk',
#           'American Indian or Alaska Native, Non-Hispanic',
#                                      'Asian, Non-Hispanic',
#  '6 Months - 64 Years at High Risk (Initial Target Group)',
#                                 '25-64 Years at High Risk',
#                  '25-64 Years not in Initial Target Group',
#                                                   'School',
#                                          'Medical Setting',
#                                           'Pharmacy/Store',
#                                                'Workplace',
#                                      'Non-Medical Setting',
#                                'Greater than 18 Years flu',
#                                'Greater than 6 Months flu',
#                                               'Greater 65']

# # Histogram 1
# DF_AgeCoverage[
#     DF_AgeCoverage["Dimension"] == "Hispanic"
# ]["Estimate (%)"].hist(
#     bins=20, edgecolor="black", ax=axes[0]
# )
# axes[0].set_title("Hispanic")

# # Histogram 2
# DF_AgeCoverage[
#     DF_AgeCoverage["Dimension"] == "White, Non-Hispanic"
# ]["Estimate (%)"].hist(
#     bins=20, edgecolor="black", ax=axes[1]
# )
# axes[1].set_title("White, Non-Hispanic")

# # Histogram 3
# DF_AgeCoverage[
#     DF_AgeCoverage["Dimension"] == "Black, Non-Hispanic"
# ]["Estimate (%)"].hist(
#     bins=20, edgecolor="black", ax=axes[2]
# )
# axes[2].set_title("Black, Non-Hispanic")
# plt.tight_layout()
# plt.show()




# ###Calculate summary statistics and create visualizations for the data , the most important statistic is vaccine coverage. 


