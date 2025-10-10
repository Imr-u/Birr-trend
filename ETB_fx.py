#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import datetime
import os
import pandas as pd


url = "https://api.nbe.gov.et/api/get-selected-exchange-rates"


page = requests.get(url)

data = page.json()
file_path = "ETB_fx.csv"
records = [ ]

if data.get("success") and "data" in data:
    for item in data["data"]:
        currency_code = item["currency"]["code"]  # USD, EUR, etc.
        buying = item["buying"]
        selling = item["selling"]
        date_val = item["date"]
        avg = item["weighted_average"]
        scrape_time = datetime.date.today()
        pair = f"{currency_code}BIRR"

        records.append({
            "buying": buying,
            "selling": selling,
            "avg": avg,
            "scrape_time": scrape_time,
            "Pair": pair
        })
df_new = pd.DataFrame(records)


if os.path.exists(file_path):
    old_df = pd.read_csv(file_path)
    df_combined = pd.concat([old_df, df_new], ignore_index=True).drop_duplicates()
else:
    df_combined = df_new

# Step 4: save
df_combined.to_csv(file_path, index=False)



