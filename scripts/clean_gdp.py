# Michelle Sun
# 12292021
# cleaning GDP data
import pandas as pd

# read in data
gdp = pd.read_csv("data/gdp.csv")

# get country name, code, 2020
gdp_out = gdp[["Country Name", "Country Code", "2020"]]
print(gdp_out)

# output csv
gdp_out.to_csv(r"data/updated_gdp.csv")
