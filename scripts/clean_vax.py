# Michelle Sun
# 12292021
# clean vaccination data
import pandas as pd

# read in data
vaccinations = pd.read_csv("data/vaccinations.csv")

# get the latest date for each country / bottommost row
print(vaccinations)

latest = vaccinations.groupby("iso_code").last()

latest.to_csv(r"data/updated_vaccinations.csv")

# get total vaccinations for each country

# output data
