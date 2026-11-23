from io import StringIO
import pandas as pd

csv_data = """county,coverage_raw
Aspen,42.5%
Birch,0%
Cedar,NR †
Douglas,—
Elm,0.8%
Fir, 51.2% †
Grove,
Hazel,38.5%
"""

df = pd.read_csv(StringIO(csv_data), keep_default_na=False)

#TODO: Inspect coverage_raw, then create a numeric column called coverage_pct. Keep the original column so you can compare values before and after cleaning.


df.info()
# print(df['coverage_raw'].isnull())
# print(df['coverage_raw'].unique())
# print(df['coverage_raw'].value_counts())

df['coverage_pct']= df['coverage_raw']
df.info()

#TODO: ##Count the missing estimates, exact zeros, and values strictly between 0% and 1%.

print("Number of missing estimates:", df['coverage_pct'].isnull().sum())
print("Number of exact zero estimates:", (df['coverage_pct'] == '0%').sum())
df['coverage_pct'] = df['coverage_pct'].replace(['NR †', '—', '', ' †'], pd.NA)
df['coverage_pct'] = df['coverage_pct'].str.rstrip('%')
df['coverage_pct'] = pd.to_numeric(
    df['coverage_pct'], errors="coerce"
)

print("Number of values strictl between 0 and 1::", df['coverage_pct'].apply(lambda x: 0 < x < 1).sum())



#TODO: ##Calculate the mean of the reported county estimates. In one sentence, explain what that mean represents.