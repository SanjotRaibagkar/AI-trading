#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:41:30 2018

@author: sanjotraibagkar
"""

#The formula for IV rank is simple, really. It is:

#100 x (the current IV level - the 52 week IV low) / (the 52 week IV high - 52 week IV low) = IV Rank

import mibian

from nsepy import get_history
from datetime import date
import pandas as pd
from matplotlib import pyplot as plt 
import datetime


c = mibian.Me([10692, 10700, 7, 0, 30], callPrice=153)

print(c.impliedVolatility)



c = mibian.Me([10692, 10600, 7, 0, 21], volatility=13)

print(c.callPrice)

from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2018, month=5)
print(expiry)

stock = 'SBIN'
start =date(2017,3,25)
end = date (2018,4,26)
end2 = date(2018,4,27)
data_fut = get_history(symbol=stock,start=start, end=end,option_type='CE',
strike_price=270, expiry_date=expiry)

print(data_fut)

data_fut['optcalldetails'] = data_fut.apply(lambda row: mibian.Me([row['Underlying'], row['Strike Price'],7,0,30],callPrice=row['Close']).impliedVolatility, axis=1)
    
print(data_fut['optcalldetails'].max() )  
print(data_fut['optcalldetails'].min() )  

c = mibian.Me([10692,10700,  7, 0, 31], callPrice=153)

print(c.impliedVolatility)



def numberofDaysToExpiery (year ,month):
    today = datetime.date.today()
    expiry = get_expiry_date(year=year, month=month)
    someday = expiry
    diff = someday - today
    return diff.days

noofdays = numberofDaysToExpiery(2018,5)






