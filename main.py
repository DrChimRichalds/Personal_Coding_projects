#### CDC health data_set query page
import os

username = "charles.c.mullins@uth.tmc.edu"

password = os.environ.get("CDC_Password")
print(password)

API_KEY = os.environ.get("CDC_API_KEY")
print(API_KEY)

API_Secret_KEY = os.environ.get("CDC_API_Secret_KEY")

CDC_BASE_URL = f"https://data.cdc.gov/api/v3/views/vh55-3he6/query.json?pageNumber=1&pageSize=10&app_token={API_KEY}"

APP_TOKEN = os.environ.get("CDC_Project_1_Token")
print(APP_TOKEN)



import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata("data.cdc.gov",
#                  APP_TOKEN,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# results = client.get("vh55-3he6", limit=2000)

# Convert to pandas DataFrame
# results_df = pd.DataFrame.from_records(results)