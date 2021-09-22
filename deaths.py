
#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

#======== Deaths Reports Daily ========#
CVD = pd.read_csv('https://opendata.arcgis.com/datasets/096cca5f77404a06babb9367530136b9_0.csv')

CVD['DATE'] = CVD['DATE']+'00'


#Convert string value of date to datetime format
CVD['DATE'] = [dt.datetime.strptime(x,'%Y/%m/%d %H:%M:%S%z') 
               for x in CVD['DATE']] 

CVD['DailyDeathsReported'] = CVD['Count_'].diff()
CVD['DailyDeaths7D'] = CVD['DailyDeathsReported'].rolling(window=7).mean()

CVD.set_index('DATE', drop=True, append=False, inplace=True, verify_integrity=False)
CVD = CVD.sort_index()

print (CVD.dtypes)
print(CVD.tail())

CVD.to_csv('ReportedDeaths.csv')

#======== Deaths by Day ========#
deaths = pd.read_csv('https://opendata.arcgis.com/datasets/ecce72a93ca24096a4463aac1e1bf771_0.csv')

deaths['DATE'] = deaths['DATE']+'00'

#Convert string value of date to datetime format
deaths['DATE'] = [dt.datetime.strptime(x,'%Y/%m/%d %H:%M:%S%z') 
               for x in deaths['DATE']] 
deaths['DailyDeathsDiff'] = deaths['Count_'].diff()
deaths['deaths7D']  = deaths['Count_'].rolling(window=7).mean()
deaths.set_index('DATE', drop=True, append=False, inplace=True, verify_integrity=False)
deaths = deaths.sort_index()

print (deaths.dtypes)
print(deaths.tail())

deaths.to_csv('DeathsbyDay.csv')

#======== Combining two Data Sets ========#
CVD['deathsbyDay'] = deaths['Count_']
CVD['deathsbyDay7Day'] = deaths['deaths7D']
print (CVD.dtypes)
print(CVD.tail())

CVD.to_csv('DeathData.csv')
