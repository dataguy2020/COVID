#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

statePopulation = 6045680

CVD = pd.read_csv('https://opendata.arcgis.com/datasets/18582de727934249b92c52542395a3bf_0.csv')
counter = 7

#Adding additional columns
CVD['ndate'] = CVD['DATE'] + '00'
CVD['DailyCases'] = CVD['Count_'].diff()
CVD['7Day'] = CVD['DailyCases'].rolling(window=7).mean()
CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()
CVD['100k7DDiff'] = CVD['100k7D'].diff()
CVD['TotalNewCasesPast7Days']  = CVD['DailyCases'].rolling(window=7).sum()
CVD['TotalNewCasesPast7Days100k'] = (CVD['TotalNewCasesPast7Days'] / statePopulation) * 100000

#Convert string value of date to datetime format
CVD['ndate'] = [dt.datetime.strptime(x, '%Y/%m/%d %H:%M:%S%z')
                for x in CVD['ndate']]



#Change Column titles to something more appropriate 
CVD.columns = ['ObjectID', 'OldDate', 'Count', 'Date', 'DailyCases', '7Day', 'Daily100k', '100k7D', '100k7D_Diff',
               'TotalNewsCasesPast7Days', 'TotalCasesPast7Days100K']

print(CVD.tail(60))
CVD.to_csv('MDStateData.csv')
print (CVD.dtypes)


#print(CVD)
#=================================================================================
# 7-Day Running Average
#=================================================================================
def plot_state_7davg(df, title='7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="Date", y="7Day", data=df, color='blue', label="7-Day Case Count")
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



cvd_case_rate_aggregate = CVD.groupby(['Date']).sum().reset_index()
sevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
sevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
sevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]
plot_state_7davg(cvd_case_rate_aggregate, 'State Aggregate 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage60day, 'State Past 60 Days 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage30day, 'State Past 30 Days 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage7day, 'State Past 7 Days 7-Day Running Average', size=4)


#=================================================================================
# Aggregate Case Rate
#=================================================================================
def plot_state_case_rate(df, title='Maryland State Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="Date", y="100k7D", data=df, color='blue', label="State Case Rate")
    plt.xlabel('Date')
    plt.ylabel(' Cases per 100k ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()


cvd_case_rate_aggregate = CVD.groupby(['Date']).sum().reset_index()
cvd60d = cvd_case_rate_aggregate.iloc[-60:]
cvd45d = cvd_case_rate_aggregate.iloc[-45:]
cvd30d = cvd_case_rate_aggregate.iloc[-30:]
cvd7d = cvd_case_rate_aggregate.iloc[-7:]

plot_state_case_rate(cvd_case_rate_aggregate, 'State Case Rate', size=4)
plot_state_case_rate(cvd60d, 'State Past  60 Days State Case Rate', size=4)
plot_state_case_rate(cvd45d, 'State Past 45 Days State Case Rate', size=4)
plot_state_case_rate(cvd30d, 'State Past 30 Days  State Case Rate', size=4)
plot_state_case_rate(cvd7d, 'State Past 7 Days State Case Rate', size=4)
