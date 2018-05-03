#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:28:29 2018

@author: sanjotraibagkar
"""

from nsepy import get_history
from datetime import date
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np



stock = 'ACC'
start =date(2011,4,27)
end = date (2018,4,27)


Nifty = get_history(symbol = stock, futures= False, 
                       start = start,end= end,  index= False)

Nifty['log_ret'] = np.log(Nifty['Close']/Nifty['Close'].shift(1))

Nifty['Volatility'] = pd.rolling_std(Nifty['log_ret'], window=252) * np.sqrt(252)*100
Nifty['30dVol'] = pd.rolling_std(Nifty['log_ret'], window=30) * np.sqrt(252)*100
Nifty['Daily_Volatility'] = pd.rolling_std(Nifty['log_ret'], window=252) *100
Nifty['30dDaily_Volatility'] = pd.rolling_std(Nifty['log_ret'], window=30) *100

## Nifty.loc[Nifty['Volatility'].idxmin()]
## val = Nifty[Nifty.Volatility >Nifty.Volatility.mean()]
##Nifty.index = pd.to_datetime(Nifty.index)

plt.figure(1,figsize=(10,9))
plt.subplot(211)
plt.title("Historical Volatility")

plt.plot(Nifty['Volatility'] , label= 'HV')
plt.plot(Nifty['30dVol'] , label= 'HV1')
#plt.plot(Nifty['Daily_Volatility'] , label= 'HV')
#plt.plot(Nifty['30dDaily_Volatility'] , label= 'HV')
plt.show()



plt.clf()
plt.cla()
plt.close()