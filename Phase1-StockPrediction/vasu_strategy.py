import datetime

import math
import numpy as np
import pandas as pd
import random

import vasu

def detect_bearish_continuation(train_data,test_data):
    recco_dict = {}
    medium_term_trend = vasu.get_medium_trend(train_data)
    
    peak_info =  vasu.get_latest_peak_info(train_data)
    peak_type = peak_info['peak_type']
    peak_data = peak_info['peak_data']
    
    peak_date = peak_data.index.to_pydatetime()[0]
    peak_high_slope = peak_data['high_slope'].values[0]
   
    if medium_term_trend != 'bullish' or medium_term_trend != 'indeterminate':
        if peak_type == 'high' and peak_high_slope >= 0.0:
            recco_dict['medium_trend'] = medium_term_trend
            recco_dict['latest_peak'] = peak_type
            recco_dict['peak_slope'] = peak_high_slope
            recco_dict['trade'] = 'sell'
            recco_dict['benchmark_date'] = peak_date
            benchmark_price =  peak_data['Low Price'].values[0]
            
            recco_dict['benchmark_price'] = benchmark_price
            
            signal_data = test_data[test_data['Close Price'] < benchmark_price][:1].copy()
            if len(signal_data) > 0:
                recco_dict['entry_date'] = signal_data.index.to_pydatetime()[0]
            
    return recco_dict