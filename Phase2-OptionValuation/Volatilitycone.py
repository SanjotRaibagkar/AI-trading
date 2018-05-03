#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 08:02:02 2018

@author: sanjotraibagkar
"""

from nsepy import get_history
from datetime import date
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np

#month range 1-12
months_range = list(range(1,13))

#year raange
year_range = list (range(2015,2018))

#get expiry for year and month combination
expiery_list = []
from nsepy.derivatives import get_expiry_date
for year in year_range:
    for mths in months_range:
        expiry = get_expiry_date(year=year, month=mths)
        expiery_list.append(expiry)
        
volatility_cone_days = [10,30,45, 60,90]   

expdate =expiery_list[1]


print(str(expdate.month)+'-'+str(expdate.month))
stock = 'NIFTY'
start =date(2010,1,1)
end = date (2018,4,27)

##Nifty.index.get_loc(str(expiery_list[1]))
Nifty = get_history(symbol = stock, futures= False, 
                       start = start,end= end,  index= True)

Nifty.index = pd.to_datetime(Nifty.index)
Nifty['log_ret'] = np.log(Nifty['Close']/Nifty['Close'].shift(1))


volatility_cone_days1 = [{
                         'vol_10' :10,
                         'vol_30':30,
                         'vol_45':45, 
                         'vol_60':60,
                         'vol_90':90}] 

cone_df = pd.DataFrame(volatility_cone_days1)

#def calculate_historicalVolatility(grouped):
#    for log_ret in grouped:
#        print(log_ret)
##try :
count=0
#for i in range(0,len(expiery_list)):
#    indexnumber = Nifty.index .get_loc(str(expiery_list[i]))  
#    rangenumber=0
#    if indexnumber !=0:
#        for cone_days in volatility_cone_days :
#            count= count+1
#            rangenumber = indexnumber-cone_days+1
#            #print(cone_days,rangenumber,expiery_list[i])   
#            #print(Nifty.iloc[rangenumber:indexnumber-1] )
#            co_df = Nifty.iloc[rangenumber:indexnumber+1]
#            co_df['Expiery_date'] = expiery_list[i]
#            co_df['cone_days'] = cone_days
#            cone_df  =cone_df.append( co_df )
# 
#grouped = cone_df.groupby(['cone_days','Expiery_date']) 
#calculate_historicalVolatility(grouped) 
#print(count)           #cone_df[str(cone_days)+'d']= Nifty.iloc[rangenumber:indexnumber-1]['Close'].max()    
#except :
 #   count = count+1
  #  print ("error",count)  

#cone_df = cone_df[0:0]
    
for i in range(0,len(expiery_list)):
    indexnumber = Nifty.index .get_loc(str(expiery_list[i]))  
    rangenumber=0
    if indexnumber !=0:
        for cone_days in volatility_cone_days :
            count= count+1
            rangenumber = indexnumber-cone_days+1
            print(cone_days,rangenumber,expiery_list[i])   
           # print(Nifty.iloc[rangenumber:indexnumber-1] )
            co_df =cNifty.iloc[rangenumber:indexnumber+1].log_ret
            #d_std = np.std(Nifty.iloc[rangenumber:indexnumber+1].log_ret)
            cone_df ['Expiery_date'] = expiery_list[i] 
            cone_df ['vol_'+str(cone_days) ] = d_std
            cone_df ['cone_days'] = cone_days
           

#Nifty['Volatility'] = pd.rolling_std(Nifty['log_ret'], window=252) * np.sqrt(252)*100
#Nifty['30dVol'] = pd.rolling_std(Nifty['log_ret'], window=30) * np.sqrt(252)*100
#Nifty['Daily_Volatility'] = pd.rolling_std(Nifty['log_ret'], window=252) *100
#Nifty['30dDaily_Volatility'] = pd.rolling_std(Nifty['log_ret'], window=30) *100






