#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:49:34 2018

@author: sanjotraibagkar
"""


# coding: utf-8

# ## Import the Libraries

# In[18]:


# Data Manupulation
import numpy as np
import pandas as pd

# Techinical Indicators
import talib as ta

# Plotting graphs
import matplotlib.pyplot as plt

# Machine learning
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

# Data fetching
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf



# ## Import the data

# In[3]:


#df = pdr.get_data_yahoo('^NSEI', '2000-01-01', '2018-01-01')
#df = df.dropna()
#df = df.iloc[:,:4]
#df.head()
#df.to_csv("Nifty112000to112018.csv")
df = pd.read_csv("Nifty50.csv", index_col = 'Date')
df = df.dropna()
df = df.iloc[:,:5]


# ## Create Indicators

# In[4]:


df['S_5'] = df['Nifty 50 Close'].rolling(window=5).mean()
df['S_13'] = df['Nifty 50 Close'].rolling(window=13).mean()
df['S_21'] = df['Nifty 50 Close'].rolling(window=21).mean()
#df['Corr'] = df['Close'].rolling(window=10).corr(df['S_10'])
df['RSI'] = ta.RSI(np.array(df['Nifty 50 Close']), timeperiod =10)
df['Open-Close'] = df['Nifty 50 Open'] - df['Nifty 50 Close'].shift(1)
df['Open-Open'] = df['Nifty 50 Open'] - df['Nifty 50 Open'].shift(1)
df = df.dropna()
X = df.iloc[:,:10]


# In[5]:


y = np.where(df['Close'].shift(-1) > df['Nifty 50 Close'],1,-1)


# ## Logistic Regression

# ### Split the Dataset and Instantiate Logistic Regression

# In[6]:


split = int(0.7*len(df))
X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]


# In[7]:

1
model = LogisticRegression()
model = model.fit (X_train,y_train)


# In[8]:


pd.DataFrame(list(zip(X.columns, np.transpose(model.coef_))))


# In[9]:


probability = model.predict_proba(X_test)
print (probability)     


# In[10]:


predicted = model.predict(X_test)


# ## Evaluate the model

# In[11]:


print (metrics.confusion_matrix(y_test, predicted))


# In[12]:


print (metrics.classification_report(y_test, predicted))


# In[13]:


print (model.score(X_test,y_test)  )


# In[14]:


cross_val = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=10)
print (cross_val)
print (cross_val.mean())


# ## Create a Trading Strategy

# In[15]:


df['Predicted_Signal'] = model.predict(X)
df['Nifty_returns'] = np.log(df['Close']/df['Close'].shift(1))
Cumulative_Nifty_returns = np.cumsum(df[split:]['Nifty_returns'])


# In[16]:


df['Startegy_returns'] = df['Nifty_returns']* df['Predicted_Signal'].shift(1)
Cumulative_Strategy_returns = np.cumsum(df[split:]['Startegy_returns'])


df.dropna()

# In[17]:


plt.figure(figsize=(10,5))
plt.plot(Cumulative_Nifty_returns, color='r',label = 'Nifty Returns')
plt.plot(Cumulative_Strategy_returns, color='g', label = 'Strategy Returns')
plt.legend()
plt.show()