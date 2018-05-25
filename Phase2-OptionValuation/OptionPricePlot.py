#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 07:12:48 2018

@author: sanjotraibagkar
"""

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



stock="BANKNIFTY"
start=start=date(2018,4,26)
end=date(2018,5,3)

callData = get_history(symbol=stock,start=start, end=end,option_type='CE',
                                    strike_price=25700, expiry_date=date(2018,5,3), index =True)
data_fut = get_history(symbol=stock,start=start, end=end,futures=True,expiry_date=date(2018,5,31),index= True)
print(callData)
print(data_fut)

plt.figure(1,figsize=(10,9))
plt.subplot(211)
plt.title('option Price')
plt.plot(callData.Close)
plt.plot(callData.Close.rolling(5).mean())





plt.subplot(212)
plt.figure(1,figsize=(10,9))
plt.title('Close')
plt.plot(data_fut.Close)
plt.plot(data_fut.Close.rolling(5).mean())
#plt.legend(['mean','Close_mean'])

plt.show()