#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:31:44 2018

@author: sanjotraibagkar
"""

from datetime import date
from nsepy.history import get_price_list
from nsepy import get_history
from datetime import date,timedelta
import pandas as pd
from matplotlib import pyplot as plt 
import datetime
from nsepy.derivatives import get_expiry_date
import numpy as np
from utility import *

prices = get_price_list(dt=date(2018,4,27))
print(prices)


from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2018, month=3)
print(expiry)


li.get_option_chain('NIFTY',instrument= 'OPTIDX',expiry= expiry)

Option_data_NIFTY.csv









