#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import os
import time
import requests
import pandas as pd


# In[29]:


page = requests.get('https://www.timeanddate.com/sun/netherlands/amsterdam')

soup = BeautifulSoup(page.text, 'html.parser')

sunset = soup.find_all('p', class_ = 'dn-mob')[0].text.split()[2][:5]
sunset


# In[30]:


sunset_datetime = pd.to_datetime(sunset)
sunset_datetime


# In[33]:


starttime=time.time()
while True:
    now = pd.to_datetime('today')
    print(f"now is :[{now}], sunset is: [{sunset_datetime}]")
    if now > sunset_datetime:
        os.system("shutdown /s /t 1")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))


# In[ ]:




