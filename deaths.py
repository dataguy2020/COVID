
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

deaths.to_csv(r'DeathsbyDay.csv')

#======== Combining two Data Sets ========#
CVD['deathsbyDay'] = deaths['Count_']
CVD['deathsbyDay7Day'] = deaths['deaths7D']
print (CVD.dtypes)
print(CVD.tail())

CVD.to_csv('DeathData.csv')
print (CVD.dtypes)

#=================================================================================
# 7-Day Running Average
#=================================================================================
def plot_state_deaths (df, title='7-Day Case Count', size = 1):
    f, ax = plt.subplots(1,1, figsize=(4*size,2*size))
    g = sns.lineplot(x="DATE", y="DailyDeaths7D", data=df, color='blue', label="Daily Reported Deaths")
    g = sns.lineplot(x="DATE", y="deathsbyDay7Day", data=df, color='green', label="Deaths by Day")

    
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

cvd_case_rate_aggregate = CVD.groupby(['DATE']).sum().reset_index()
sevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
sevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
sevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]


plot_state_deaths(cvd_case_rate_aggregate, 'Aggregate 7-Day Running Average', size=4)
plot_state_deaths(sevenDayAverage60day, 'Past 60 Days 7-Day Running Average', size=4)
plot_state_deaths(sevenDayAverage30day, 'Past 30 Days 7-Day Running Average', size=4)
plot_state_deaths(sevenDayAverage7day, 'Past 7 Days 7-Day Running Average', size=4)
