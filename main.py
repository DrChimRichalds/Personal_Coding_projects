
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#### I want to generate box plots and histograms of the of the data

CDC_results = pd.read_csv("data/raw/cdc_results.csv")
CDC_results_to_df = pd.DataFrame(CDC_results)
#CDC_results_to_df.info()


# CDC_results_to_df[['CI_lower', 'CI_upper']] = (
#     CDC_results_to_df['_95_ci']
#     .str.split(' to ', expand=True)
# )
# CDC_results_to_df['CI_lower'] = pd.to_numeric(CDC_results_to_df['CI_lower'], errors='coerce')
# CDC_results_to_df['CI_upper'] = pd.to_numeric(CDC_results_to_df['CI_upper'], errors='coerce')

### Geography based histogram 
# geography = CDC_results_to_df["geography"]
# geography.value_counts().plot(kind='bar', title='Geography Distribution')
# plt.xlabel("Geography")
# plt.ylabel("Count") 
# plt.show()

#print(CDC_results_to_df["dimension"].unique())

### Creating a histogram of the coverage estimates for the dimension "18-64 Years not at High Risk"
# DF_AgeCoverage[
#     DF_AgeCoverage["dimension"] == "18-64 Years not at High Risk"
# ]["coverage_estimate"].hist(
#     bins=20,
#     edgecolor="black"
# )
# plt.title("Histogram of Coverage Estimates for 18-64 Years not at High Risk Dimension")
# plt.xlabel("Coverage Estimates", fontsize=15)
# plt.xticks(rotation=45)
# plt.ylabel("Frequency", fontsize=15)
# plt.show()


#Filtering the data to only include coverage estimates that are not null and are numeric
# coverage_estimates = CDC_results_to_df["coverage_estimate"]
# coverage_estimates = CDC_results_to_df["coverage_estimate"]
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

# population_sample_sizes = CDC_results_to_df["population_sample_size"]
# population_sample_sizes = population_sample_sizes.dropna()
# population_sample_sizes.info()



# population_sample_sizes.hist(bins=50, edgecolor='black')
# print("Histogram of Population Sample Sizes")
# plt.title("Histogram of Population Sample Sizes")
# plt.xlabel("Population Sample Size")
# plt.ylabel("Frequency")
# plt.show()

#boxplot = population_sample_sizes.plot.box(title="Box Plot of Population Sample Sizes")

# confidence_intervals = CDC_results_to_df["_95_ci"]
# conditional_intervals = confidence_intervals.str.replace('to', '', regex=False)

### many subplots for the different dimensions of the data, each with their own histogram of coverage estimates
# CDC_results_to_df.info()


# DF_AgeCoverage = CDC_results_to_df[[
#     "dimension_type",
#     "dimension",
#     "coverage_estimate",
# ]]

# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace('NR †', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace('NR', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace('†', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace(' ', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace('–', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace('—', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.replace('nan', '', regex=False)
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].dropna()
# DF_AgeCoverage["coverage_estimate"] = DF_AgeCoverage["coverage_estimate"].str.strip()
# DF_AgeCoverage["coverage_estimate"] = pd.to_numeric(DF_AgeCoverage["coverage_estimate"], errors='coerce')
# print(DF_AgeCoverage.head())

# fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# ### use this to examien the data for different dimensions of the data, and create histograms for each dimension
# print(CDC_results_to_df["dimension"].unique())

# # Histogram 1
# DF_AgeCoverage[
#     DF_AgeCoverage["dimension"] == "Black, Non-Hispanic"
# ]["coverage_estimate"].hist(
#     bins=20, edgecolor="black", ax=axes[0]
# )
# axes[0].set_title("Black, Non-Hispanic")

# # Histogram 2
# DF_AgeCoverage[
#     DF_AgeCoverage["dimension"] == "Hispanic"
# ]["coverage_estimate"].hist(
#     bins=20, edgecolor="black", ax=axes[1]
# )
# axes[1].set_title("Hispanic")

# # Histogram 3
# DF_AgeCoverage[
#     DF_AgeCoverage["dimension"] == "White, Non-Hispanic"
# ]["coverage_estimate"].hist(
#     bins=20, edgecolor="black", ax=axes[2]
# )
# axes[2].set_title("White, Non-Hispanic")
# plt.title("Histogram of Coverage Estimates by Age Group")
# plt.tight_layout()
# plt.show()




###Calculate summary statistics and create visualizations for the data , the most important statistic is vaccine coverage. 


