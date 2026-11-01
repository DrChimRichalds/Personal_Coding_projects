
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#### I want to generate box plots and histograms of the of the data

CDC_results = pd.read_csv("cdc_results.csv")
CDC_results_to_df = pd.DataFrame(CDC_results)
CDC_results_to_df.info()



# CDC_results_to_df[['CI_lower', 'CI_upper']] = (
#     CDC_results_to_df['_95_ci']
#     .str.split(' to ', expand=True)
# )
# CDC_results_to_df['CI_lower'] = pd.to_numeric(CDC_results_to_df['CI_lower'], errors='coerce')

# CDC_results_to_df['CI_upper'] = pd.to_numeric(CDC_results_to_df['CI_upper'], errors='coerce')

# geography = CDC_results_to_df["geography"]
# geography.value_counts().plot(kind='bar', title='Geography Distribution')
# plt.xlabel("Geography")
# plt.ylabel("Count") 
# plt.show()

dimension = CDC_results_to_df["dimension"]
dimension.

# dimension.value_counts().plot(kind='bar', title='Dimension Distribution')
# plt.xlabel("Dimension")
# plt.ylabel("Count")
# plt.show()


# coverage_estimates = CDC_results_to_df["coverage_estimate"]
# coverage_estimates = coverage_estimates.str.replace('NR †', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('NR', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('†', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace(' ', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('–', '', regex=False)
# coverage_estimates = coverage_estimates.str.replace('—', '', regex=False)
# coverage_estimates = coverage_estimates.dropna()
# coverage_estimates = coverage_estimates.str.strip()

# coverage_estimates = pd.to_numeric(coverage_estimates, errors='coerce')
# coverage_estimates.hist(bins=20, edgecolor='black')
# print("Histogram of Coverage Estimates")
# plt.title("Histogram of Coverage Estimates")
# plt.xlabel("Coverage Estimates", fontsize=15)
# plt.xticks(rotation=45)
# plt.ylabel("Frequency", fontsize=15)
# # plt.locator_params(axis='x', nbins=5)

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


###Calculate summary statistics and create visualizations for the data , the most important statistic is vaccine coverage. 


