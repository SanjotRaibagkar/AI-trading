from datetime import date
from nsepy import *
import pandas as pd

sbin=get_history(symbol='TATASTEEL',start=date(2018,1,1),end=date(2019,1,1))
#print(sbin)
sbin.to_csv('tatasteel.csv')