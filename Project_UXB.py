#!/usr/bin/env python
# coding: utf-8

# In[55]:


from bs4 import BeautifulSoup
import requests
import datetime
import os
import pandas as pd


# In[32]:


url = "https://api.nbe.gov.et/api/get-selected-exchange-rates"


# In[56]:


page = requests.get(url)

data = page.json()

usd_entry = next(item for item in data["data"] if item["currency"]["code"] == "USD")

usd_buying = float(usd_entry["buying"])
usd_selling = float(usd_entry["selling"])
usd_weighted = float(usd_entry["weighted_average"])
scrape_time = datetime.date.today()

print( usd_buying)
print( usd_selling)
print( usd_weighted)
print(scrape_time)

rates= [[usd_buying, usd_selling, usd_weighted, scrape_time]]
columns = ["buying", "selling", "avg", "scrape_time"]


# In[57]:


df= pd.DataFrame(rates,columns= columns)
print(df)

df_new = pd.DataFrame(rates, columns = columns)


# In[65]:


if os.path.exists("USDBIRR.csv"):
    df_old = pd.read_csv("USDBIRR.csv")
else:
    df_old= pd.DataFrame(columns=df_new.columns)

df_combined = pd.concat([df_old, df_new], ignore_index=True)
df_clean = df_combined.drop_duplicates(subset=["scrape_time"])


df_clean.to_csv("USDBIRR.csv", index=False) 


# In[ ]:




