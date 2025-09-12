#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import datetime
import os
import pandas as pd


# In[3]:


url = "https://api.nbe.gov.et/api/get-selected-exchange-rates"


# In[4]:


page = requests.get(url)

data = page.json()


aed_entry = next(item for item in data["data"] if item["currency"]["code"] == "AED")

aed_buying = float(aed_entry["buying"])
aed_selling = float(aed_entry["selling"])
aed_weighted = float(aed_entry["weighted_average"])
scrape_time= datetime.date.today()

rates_= [[aed_buying, aed_selling, aed_weighted, scrape_time]]
columns_ = ["buying", "selling", "avg", "scrape_time"]

df_= pd.DataFrame(rates_,columns= columns_)
print(df_)

df_new_ = pd.DataFrame(rates, columns = columns_)

eur_buying = float(usd_entry["buying"])
eur_selling = float(usd_entry["selling"])
eur_weighted = float(usd_entry["weighted_average"])
scrape_time = datetime.date.today()

rates= [[eur_buying, eur_selling, eur_weighted, scrape_time]]
columns = ["buying", "selling", "avg", "scrape_time"]


# In[5]:


df= pd.DataFrame(rates,columns= columns)

df_new = pd.DataFrame(rates, columns = columns)


# In[8]:


if os.path.exists("EURBIRR.csv"):
    df_old = pd.read_csv("EURBIRR.csv")
else:
    df_old= pd.DataFrame(columns=df_new.columns)

df_combined = pd.concat([df_old, df_new], ignore_index=True)
df_clean = df_combined.drop_duplicates(subset=["scrape_time"])


df_clean.to_csv("EURBIRR.csv", index=False) 






