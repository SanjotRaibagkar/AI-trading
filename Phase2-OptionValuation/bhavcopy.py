#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:31:44 2018

@author: sanjotraibagkar
"""

from datetime import date
from nsepy.history import get_price_list
prices = get_price_list(dt=date(2018,4,27))
print(prices)


from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2018, month=3)
print(expiry)


li.get_option_chain('NIFTY',instrument= 'OPTIDX',expiry= expiry)





