#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import os
import time
import requests
import pandas as pd


# In[ ]:


page = requests.get('https://www.timeanddate.com/sun/netherlands/amsterdam')

soup = BeautifulSoup(page.text, 'html.parser')

sunset = soup.find_all(class_='three')[2].contents[0]
sunset


# In[3]:


sunset_datetime = pd.to_datetime(sunset)
sunset_datetime


# In[ ]:


starttime=time.time()
while True:
    now = pd.to_datetime('today')
    print(f'now is :[{now}], sunset is: [{sunset_datetime}]')
    if now > sunset_datetime:
        os.system("shutdown /s /t 1")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

