#### 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

##### generate reports based on comparison of the data from the CDC health data set and the cleaned version of the data set.

CDC_results = pd.read_csv("data/processed/cdc_results_clean.csv")
df = pd.DataFrame(CDC_results)

dimension = df["dimension"].unique()

print(f"Unique dimensions in the cleaned data set:\n{dimension}")

Comparison_group_1 = df[df["dimension"] == "18-64 Years not at High Risk"]
Comparison_group_2 = df[df["dimension"] == "18-64 Years at High Risk"]

CDC_results.groupby("dimension")["coverage_estimate"].describe()

df["coverage_estimate"] = df["coverage_estimate"].str.replace('NR †', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].str.replace('NR', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].str.replace('†', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].str.replace(' ', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].str.replace('–', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].str.replace('—', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].str.replace('nan', '', regex=False)
df["coverage_estimate"] = df["coverage_estimate"].dropna()
df["coverage_estimate"] = df["coverage_estimate"].str.strip()
df["coverage_estimate"] = pd.to_numeric(df["coverage_estimate"], errors='coerce')

# Separate histogram for each vaccine

# sns.histplot(
#     data=CDC_results,
#     x="coverage_estimate",
#     hue="vaccine",
#     kde=True
# )

# plt.xlabel("Vaccine Coverage (%)")
# plt.ylabel("Frequency")
# plt.title("Distribution of Vaccine Coverage")
# plt.show()


# sns.boxplot(
#     data=CDC_results,
#     x="vaccine",
#     y="coverage_estimate"
# )

# plt.title("Vaccine Coverage by Vaccine Type")
# plt.xlabel("Vaccine")
# plt.ylabel("Coverage Estimate (%)")
# plt.show()





# Generate Q-Q plot
stats.probplot(
    df["coverage_estimate"],
    dist="norm",
    plot=plt
)

plt.title(f"Q-Q Plot: vaccine Coverage Estimates")
plt.show()