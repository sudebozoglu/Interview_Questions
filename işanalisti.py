import pandas as pd
import numpy as np

df = pd.read_csv('country_vaccination_stats.csv')

df = df.groupby(['country']).apply(lambda x: x.sort_values('date'))


for country in df['country'].unique():
    country_data = df[df['country'] == country]
    missing_data = country_data['daily_vaccinations'].isnull()
    if missing_data.any():

        relevant_countries = df[df['date'].isin(country_data['date'])]
        min_daily_vaccinations = relevant_countries['daily_vaccinations'].min()

        country_data.loc[missing_data, 'daily_vaccinations'] = min_daily_vaccinations

    country_data['daily_vaccinations'].fillna(0, inplace=True)

df.to_csv('imputed.csv', index=False)


