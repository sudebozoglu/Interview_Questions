
import pandas as pd


data = pd.read_csv("country_vaccination_stats.csv")

data.fillna(data.median(), inplace=True)

countrydata = data.groupby('country')['daily_vaccinations'].median().reset_index()

top = countrydata.sort_values('daily_vaccinations', ascending=False).head(3)


print(top)
