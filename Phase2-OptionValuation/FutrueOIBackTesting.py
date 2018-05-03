#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:35:09 2018

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