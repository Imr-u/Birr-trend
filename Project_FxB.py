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

usd_entry = next(item for item in data["data"] if item["currency"]["code"] == "EUR")

eur_buying = float(usd_entry["buying"])
eur_selling = float(usd_entry["selling"])
eur_weighted = float(usd_entry["weighted_average"])
scrape_time = datetime.date.today()

print( eur_buying)
print( eur_selling)
print( eur_weighted)
print(scrape_time)

rates= [[eur_buying, eur_selling, eur_weighted, scrape_time]]
columns = ["buying", "selling", "avg", "scrape_time"]


# In[5]:


df= pd.DataFrame(rates,columns= columns)
print(df)

df_new = pd.DataFrame(rates, columns = columns)


# In[8]:


if os.path.exists("EURBIRR.csv"):
    df_old = pd.read_csv("EURBIRR.csv")
else:
    df_old= pd.DataFrame(columns=df_new.columns)

df_combined = pd.concat([df_old, df_new], ignore_index=True)
df_clean = df_combined.drop_duplicates(subset=["scrape_time"])


df_clean.to_csv("EURBIRR.csv", index=False) 


# In[17]:


usd_entry2 = next(item for item in data["data"] if item["currency"]["code"] == "AED")

aed_buying = float(usd_entry2["buying"])
aed_selling = float(usd_entry2["selling"])
aed_weighted = float(usd_entry2["weighted_average"])
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

