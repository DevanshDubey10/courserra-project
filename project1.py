#!/usr/bin/env python
# coding: utf-8

# In[4]:


import yfinance as yf
import pandas as pd
import requests


# In[5]:


tesla= yf.Ticker("TSLA")
tesla_info=tesla.info


# In[6]:


tesla_info


# In[7]:


tesla_data=tesla.history(period="max")


# In[8]:


tesla_data.reset_index(inplace= True)


# In[9]:


tesla_data.head()


# In[10]:


tesla


# In[11]:


tesla_data.head()


# In[12]:


#Question 2: Use Webscraping to Extract Tesla Revenue Data


# In[13]:


import requests
import pandas as pd
from bs4 import BeautifulSoup 


# In[14]:


url =" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data= requests.get(url).text


# In[15]:


tesla_revenue=pd.read_html(html_data)
print(tesla_revenue[1])


# In[16]:


tesla_rev=pd.DataFrame(tesla_revenue[1])
tesla_rev


# In[17]:


tesla_rev.columns


# In[43]:


tesla_rev.rename(columns={"Tesla Quarterly Revenue(Millions of US $)":"Date","Tesla Quarterly Revenue(Millions of US $).1":"Revenue"})


# In[ ]:


columns


# In[ ]:


#Question 3: Use yfinance to Extract Stock Data¶


# In[ ]:


import yfinance as yf


# In[21]:


GameStop=yf.Ticker("GME")
GameStop_info=GameStop.info


# In[22]:


GameStop_info


# In[24]:


gme_Data=GameStop.history(period="max")
gme_Data.reset_index(inplace=True)


# In[25]:


gme_Data.head()


# In[26]:


#Question 4: Use Webscraping to Extract GME Revenue Data¶


# In[27]:


url1= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
gmedata=requests.get(url1).text


# In[28]:


gme_revenue=pd.read_html(gmedata, flavor="bs4")


# In[29]:


print(gme_revenue[1])


# In[30]:


gme_rev= pd.DataFrame(gme_revenue[1])


# In[31]:


gme_rev


# In[32]:


gme_rev.columns


# In[33]:


gme_rev.rename(columns={"GameStop Quarterly Revenue(Millions of US $)":"Date","GameStop Quarterly Revenue(Millions of US $).1":"Revenue"})


# In[34]:


#Question 5: Plot Tesla Stock Graph


# In[47]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[48]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[50]:


make_graph(tesla_data,tesla_rev,"Tesla")


# In[52]:


make_graph(gmedata, gme_revenue, 'GameStop')


# In[ ]:




