#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:35:55 2018

@author: sanjotraibagkar
"""


from nsepy import get_history
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt



stock="SBIN"
start=start=date(2017,12,26)
end=date(2018,1,25)
end2=date(2018,2,6)
data_fut = get_history(symbol=stock,start=start, end=end,futures=True,expiry_date=date(2018,1,25))
data_fut2 = get_history(symbol=stock,start=start, end=end2,futures=True, 
                        expiry_date=date(2018,2,22))

OI_combined= pd.concat([data_fut2['Open Interest'],data_fut['Open Interest']],
                       axis=1)
OI_combined['OI_Combined']=OI_combined.sum(axis=1)


plt.figure(1,figsize=(10,9))
plt.subplot(211)
plt.title('Open Interest')
plt.plot(OI_combined.OI_Combined)
plt.plot(OI_combined.OI_Combined.rolling(5).mean())
plt.legend(['OI','OI_mean'])

C_combined= pd.concat([data_fut2['Close'],data_fut['Close']],axis=1)
C_combined['Continous_Close']=C_combined.iloc[:,1].fillna(C_combined.iloc[:,0])

O_combined= pd.concat([data_fut2['Open'],data_fut['Open']],axis=1)
O_combined['Continous_Open']=O_combined.iloc[:,1].fillna(O_combined.iloc[:,0])

plt.subplot(212)
plt.title('Close')
plt.plot(C_combined.Continous_Close)
plt.plot(O_combined.Continous_Open)
plt.plot(C_combined.Continous_Close.rolling(5).mean())
plt.legend(['Close','Open','Close_mean'])

plt.show()