#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:39:44 2018

@author: sanjotraibagkar
"""

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
from datetime import date,timedelta
import pandas as pd
from matplotlib import pyplot as plt 
import datetime
from nsepy.derivatives import get_expiry_date
import numpy as np


symbollist =['BANKNIFTY','NIFTY'] 
symbol = symbollist[0]



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
        
call_data_list = []
put_data_list =[]
l =[]    

def get_optionDataFromChain(optionChain2, startDate, endDate,symbol,year,month, index,weekly= False):
    

    
#    expiry = get_expiry_date(year=year, month=month) 
    expiry = getExpirydate(year,month,1,weekly,symbol)
   # print(optionChain2)
    print(expiry)
    
    for val in optionChain2:
       
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





def maxpain(c):
    
    for _, row in c.iterrows():
    #strike_price = 8900.0
        strike_price = row.name    
        d = c.index.get_loc(strike_price)
        
        val1 = ((strike_price-c.index[:d].values)*c.iloc[:d]['Open Interest']['CE']).sum()
        val2 = ((c.index[d:].values-strike_price)*c.iloc[d:]['Open Interest']['PE']).sum()
        #print("calc",strike_price,'--',val2)
        c.set_value(strike_price,'callsum',val1)
        c.set_value(strike_price,'putsum',val2)

#        v1 = c.iloc[:d]['Open Interest']['CE'].sum()
#        v2= c.iloc[:d]['Open Interest']['PE'].sum()
    
    return c

start,end = getStartandEndDate (date (2017,12,1),date(2018,4,30) ,today=True,startbeforday=0)
date1= end +timedelta(days =-1)

#def findmaxpain(symbol):
#    
#    optionChain = pd.read_csv(symbol +"_Option_Chain_Table.csv")
#    optionseries = optionChain['Strike Price']    
#    calldatalist, putdatalist,calldataframe  = get_optionDataFromChain(optionseries,start,end,symbol,2018,5,True, weekly =False)
#    calldataframe.to_csv("1-YR-Data.csv")       
#    print(date1)    
#    a = calldataframe.groupby(calldataframe.index)
#    b = a.get_group(date1)[['Strike Price','Option Type','Open Interest']]
#    c = b.groupby(['Strike Price','Option Type'])[['Open Interest']].sum().unstack()
#    c['callsum'] =0
#    c['putsum'] =0
#    r1 = maxpain(c)
#    r1["totalpain"] = c['callsum']+c['putsum']
#    
#   # print(r1.loc[r1["totalpain"].idxmin()])
#    return r1.loc[r1["totalpain"].idxmin()],r1,calldataframe

def buildDataSet(symbol):
    import os.path
    fname = "1-YR-Data.csv"
    if path.exists(fame) :       
        oneyrData = pd.read_csv(fname)
    else :    

        optionChain = pd.read_csv(symbol +"_Option_Chain_Table.csv")
        optionseries = optionChain['Strike Price'] 
        for i in range(1,7):
            calldatalist, putdatalist,calldataframe = get_optionDataFromChain(optionseries,start,end,symbol,2018,i,True, weekly =False)
for symbol in symbollist:
    buildDataSet(symbol)
    
resultData = pd.concat(l)
resultData.to_csv("1-YR-Data.csv") 



def analysisData(resultData):
    maxpainlist= {}
    maxpain1 =[]
    
    a = resultData.groupby([resultData['Symbol'],resultData["Expiry"],resultData.index])    
    for name,group in a:
        c =group.groupby(['Strike Price','Option Type'])[['Open Interest']].sum().unstack()
        c['callsum'] =0
        c['putsum'] =0
        r1 = maxpain(c)
        r1["totalpain"] = c['callsum']+c['putsum']
        maxpainlist.update({name:r1})
        maxpain1.append([name[0],name[1],name[2],(r1.loc[r1["totalpain"].idxmin()]).name,
                         r1.loc[r1['Open Interest']["CE"].idxmax()].name,
                         r1.loc[r1['Open Interest']["CE"].idxmin()].name,
                         r1.loc[r1['Open Interest']["PE"].idxmax()].name,
                         r1.loc[r1['Open Interest']["PE"].idxmin()].name ])               
    maxPainFrame = pd.DataFrame(painlist, columns=["Symbol","Expiry",'Date','maxpain','OI_CE_MAX','OI_CE_MIN','OI_PE_MAX','OI_PE_MIN'])        
    return maxpainlist,maxPainFrame 
         
maxpainList, painFrame = analysisData(resultData)  

k#ey = ("BANKNIFTY",datetime.date(2018, 4, 26),datetime.date(2018, 4, 25))



print(r1)






#maximum = "MAX"
#minimum = "MIN"
#pe = "PE"
#ce = "CE"
#
#for symbol in symbollist:
#    val,r1 , calldataform = findmaxpain(symbol)    
#    maxpainTabel = {symbol:val.name}
#    openintrestTabel = {symbol+maximum+ce :r1.loc[r1['Open Interest'][ce].idxmax()].name,
#                        symbol+minimum+ce :r1.loc[r1['Open Interest'][ce].idxmin()].name , 
#                        symbol+maximum+pe :r1.loc[r1['Open Interest'][pe].idxmax()].name,
#                        symbol+minimum+pe :r1.loc[r1['Open Interest'][pe].idxmin()].name                        }
#    #print(r1)
#    
#
#print("maxpainTabel",maxpainTabel)
#print("openIntrest" ,openintrestTabel)
    
 for name,group in a:
     tub = name
     break
        


