#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 13:44:00 2018

@author: sanjotraibagkar
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 13:00:43 2017

@author: academy
"""
# Importing libraries
from mibian import BS
import pandas as pd
import matplotlib.pyplot as plt

# Fetching data and initializing the IV column
nifty_data = pd.read_csv("Option_data_NIFTY.csv")
nifty_data['IV'] = 0
print (nifty_data.head())

# Computing implied volatilities
for row in range(0,len(nifty_data)):       
    underlyingPrice = nifty_data.iloc[row]['Underlying Value']
    strikePrice = nifty_data.iloc[row]['Strike Price']
    interestRate = 0
    daysToExpiration = nifty_data.iloc[row]['Time to Expiry']
    
    callPrice = nifty_data.iloc[row]['LTP']
    
    result = BS([underlyingPrice, strikePrice, interestRate, daysToExpiration],
                callPrice = callPrice)
    
    nifty_data.iloc[row,nifty_data.columns.get_loc('IV')] = result.impliedVolatility

# Plotting the volatility smile
def Plot_smile(date):
    option_data = nifty_data[nifty_data['Date'] == date]
    plt.plot(option_data['Strike Price'],option_data['IV'])
    plt.legend(option_data['Date'])
    plt.ylabel('Implied Volatility')
    plt.xlabel('Strike Price')           
    plt.show()

# Taking input date and calling the Plot_smile() function
def Take_input():
    smile_date = input("Enter the date for plotting Volatility Smile in the format dd-mm-yyyy: ")
    date_check = 0
    for date in nifty_data['Date']:
        if date == smile_date:
            Plot_smile(smile_date)
            break
    else:
        print ("\nKindly enter a valid date.\n")
        Take_input()

# Calling the Take_input() function
Take_input()