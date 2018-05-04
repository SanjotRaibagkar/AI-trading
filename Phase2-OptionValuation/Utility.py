#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:36:01 2018

@author: sanjotraibagkar
"""

from nsepy import get_history
from datetime import date,timedelta
import pandas as pd
from matplotlib import pyplot as plt 
import datetime
from nsepy.derivatives import get_expiry_date
import numpy as np



def getStartandEndDate(startdate,enddate,today = True,startbeforday =2):
    
    if today:
        end = date.today()
    else:
        end = enddate
    if startbeforday ==0:
        start = startdate
    else:
        start =date.today()+ timedelta(days =-startbeforday)
    return start , end   




def getExpirydate(year,month, week,weekly, symbol):
    
    if symbol =='BANKNIFTY' and weekly:
        expiry = date(year,month,17)
    else :
        expiry = get_expiry_date(year=year, month=month)
    return expiry 



## Get Data from nse if not avialalbe at local
import os.path
def getData(Symbol,startdate, enddate,index= True,futures=True,):
    
    fname = Symbol+ "_symbolData.csv"
    if os.path.exists(fname) :       
        data = pd.read_csv(fname,index_col ='Date')
        print("got it")
    else :  
        data = get_history(symbol=Symbol,
                            start=startdate,
                            end=enddate,
                            index=index,
                            futures=futures,)
        data.to_csv(Symbol+ "_symbolData.csv")
        
    return data   
        

   