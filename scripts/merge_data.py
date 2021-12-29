# Michelle Sun
# 12292021
# merging data with gdp
import pandas as pd

# read in both data sets
vaccs = pd.read_csv("data/updated_vaccinations.csv")
gdps = pd.read_csv("data/updated_gdp.csv")

# merge by country code

merged = vaccs.merge(gdps, left_on='iso_code', right_on="Country Code")

# output
merged.to_csv(r"data/merged.csv")
