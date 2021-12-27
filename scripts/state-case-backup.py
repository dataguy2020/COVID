#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

statePopulation = 6045680

CVD = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/COVID/master/datasets/MarylandState/MDCOVID19_TotalCasesStatewide.csv')

CVD['DATE'] = [dt.datetime.strptime(x,'%m/%d/%Y') for x in CVD['DATE']] 

statepopulation = 6045680

CVD['Daily100k'] = (CVD['Daily Reported'] / statePopulation) * 100000
CVD['7Day'] = CVD['Daily Reported'].rolling(window=7).mean()
CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()
CVD['100k7DDiff'] = CVD['100k7D'].diff()
CVD['TotalNewCasesPast7Days']  = CVD['Daily Reported'].rolling(window=7).sum()
CVD['TotalNewCasesPast7Days100k'] = (CVD['TotalNewCasesPast7Days'] / statepopulation) * 100000


print (CVD.dtypes)

CVD.to_csv('MDStateData-backup.csv')

#=================================================================================
# 7-Day Running Average
#=================================================================================
def plot_state_casesper100k (df, title='State 7-Day Avg Case Count', size = 1):
    f, ax = plt.subplots(1,1, figsize=(4*size,2*size))
    g = sns.lineplot(x="DATE", y="100k7D", data=df, color='blue', label="United States")
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

MDcaserateaggregate = CVD.groupby(['DATE']).sum().reset_index()
MDsevenDayAverage60day = MDcaserateaggregate.iloc[-60:]
MDsevenDayAverage30day = MDcaserateaggregate.iloc[-30:]
MDsevenDayAverage7day = MDcaserateaggregate.iloc[-7:]

plot_state_casesper100k(MDcaserateaggregate, 'Maryland Aggregate 7-Day Running Average', size=4)
plot_state_casesper100k(MDsevenDayAverage60day, 'Maryland Past 60 Days 7-Day Running Average', size=4)
plot_state_casesper100k(MDsevenDayAverage30day, 'Maryland Past 30 Days 7-Day Running Average', size=4)
plot_state_casesper100k(MDsevenDayAverage7day, 'Maryland Past 7 Days 7-Day Running Average', size=4)

