# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc["Egypt":"India"])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")])

# Subset in both directions at once
print(temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"), "2005":"2010"])
