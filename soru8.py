import pandas as pd

# Verileri yükle
df = pd.read_csv("C:/Users/User/Desktop/veriler.txt")

# stats_Access sütunundaki URL'lerden saf URL'yi ayıkla
df["saf_url"] = df["stats_Access"].apply(lambda x: x.split(">")[1].split("<")[0])

# İlk 5 satırı yazdır
print(df.head())
