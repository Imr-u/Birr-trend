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

aed_buying = float(usd_entry["buying"])
aed_selling = float(usd_entry["selling"])
aed_weighted = float(usd_entry["weighted_average"])
scrape_time= datetime.date.today()

rates_= [[aed_buying, aed_selling, aed_weighted, scrape_time]]
columns_ = ["buying", "selling", "avg", "scrape_time"]

df_= pd.DataFrame(rates_,columns= columns_)
print(df_)

df_new_ = pd.DataFrame(rates, columns = columns_)


# In[22]:


if os.path.exists("AEDBIRR.csv"):
    df_old_ = pd.read_csv("AEDBIRR.csv")
else:
    df_old_= pd.DataFrame(columns=df_new.columns)

df_combined_a = pd.concat([df_old_, df_new_], ignore_index=True)
df_clean_a = df_combined_a.drop_duplicates(subset=["scrape_time"])


df_clean_a.to_csv("AEDBIRR.csv", index=False) 

