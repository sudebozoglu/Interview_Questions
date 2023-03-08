import pandas as pd


df = pd.read_csv("veriler.csv")

df["date"] = pd.to_datetime(df["date"])


total_vaccinations = df.loc[df["date"] == "2021-06-01", "daily_vaccinations"].sum()

print("2021 -06-01:", total_vaccinations)
