#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 07:45:01 2018

@author: sanjotraibagkar
"""

"""
Created on Tue May  1 22:33:21 2018

@author: sanjotraibagkar
"""
from nsepy import get_history
from datetime import date
import pandas as pd
from matplotlib import pyplot as plt 
import datetime
from nsepy.derivatives import get_expiry_date
import numpy as np


start =date(2018,5,1)
end = date (2018,5,2)
end2 = date(2018,4,27)
symbol='NIFTY' 

optionChain = pd.read_csv("Option_Chain_Table.csv")




def get_optionDataFromChain1(optionChain2, startDate, endDate,symbol,year,month, index):
    
    call_data_list = []
    put_data_list =[]
    l =[]
    
    expiry = get_expiry_date(year=year, month=month) 
    print(optionChain2)
    for val in optionChain2:
        print("Val", val)
        calldata=  get_history(symbol=symbol,start=start, end=end,option_type='CE',
                                    strike_price=val, expiry_date=expiry, index =index)
        putdata=  get_history(symbol=symbol,start=start, end=end,option_type='PE',
                                    strike_price=val, expiry_date=expiry, index =index)
        
        call_data_list.append(calldata)
        put_data_list.append(putdata)
        l.append(calldata)
        l.append(putdata)
    
    
    result = pd.concat(l)
    return call_data_list, put_data_list,result


optionseries = optionChain['Strike Price']


calldatalist, putdatalist,calldataframe  = get_optionDataFromChain1(optionseries,start,end,symbol,2018,5,True)
calldataframe.to_csv("merge.csv")


def maxpain(c):
    
    for _, row in c.iterrows():
    #strike_price = 8900.0
        strike_price = row.name    
        d = c.index.get_loc(strike_price)
        print("d is ",d)
        val1 = ((strike_price-c.index[:d].values)*c.iloc[:d]['Open Interest']['CE']).sum()
        val2 = ((c.index[d:].values-strike_price)*c.iloc[d:]['Open Interest']['PE']).sum()
        #print("calc",strike_price,'--',val2)
        c.set_value(strike_price,'callsum',val1)
        c.set_value(strike_price,'putsum',val2)

#        v1 = c.iloc[:d]['Open Interest']['CE'].sum()
#        v2= c.iloc[:d]['Open Interest']['PE'].sum()
    
    return c



date1= datetime.date(2018, 5, 2)

a = calldataframe.groupby(calldataframe.index)
b = a.get_group(date1)[['Strike Price','Option Type','Open Interest']]
c = b.groupby(['Strike Price','Option Type'])[['Open Interest']].sum().unstack()
c['callsum'] =0
c['putsum'] =0
r1 = maxpain(c)
r1["totalpain"] = c['callsum']+c['putsum']

print(r1.loc[r1["totalpain"].idxmin()])

