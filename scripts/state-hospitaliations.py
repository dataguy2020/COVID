#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

CVD = pd.read_csv('https://opendata.arcgis.com/datasets/5804ed5beed24fc690fbf6b86711ffda_0.csv')

CVD['ndate'] = CVD['ReportDate'] + '00'
CVD['ndate'] = [dt.datetime.strptime(x, '%Y/%m/%d %H:%M:%S%z')
                for x in CVD['ndate']]
CVD.set_index('ndate', drop=True, append=False, inplace=True, verify_integrity=False)
CVD = CVD.sort_index()

CVD['ICU7D'] = CVD['ICU'].rolling(window=7).mean()
CVD['Acute7D'] = CVD['Acute'].rolling(window=7).mean()


CVD['AdultAcutePatients7D'] = CVD['AdultAcutePatients'].rolling(window=7).mean()
CVD['AdultICUPatients7D'] = CVD['AdultICUPatients'].rolling(window=7).mean()

CVD['PedsAcutePatients7D'] = CVD['PedsAcutePatients'].rolling(window=7).mean()
CVD['PedsICUPatients7D'] = CVD['PedsICUPatients'].rolling(window=7).mean()

print (CVD.dtypes)

#=================================================================================
# 7-Day Running Average Total ICU vs Acute
#=================================================================================
def plot_hospitalizations(df, title='7 Day Running Average Hospitalizations', size =2):
    f, ax= plt.subplots(1,1, figsize=(4*size,2*size))
    g = sns.lineplot(x="ndate", y="Acute", data=df, color='blue', label='Acute')
    g = sns.lineplot(x='ndate', y='ICU7D', data=df, color='green', label="ICU")

    plt.xlabel('Date')
    plt.ylabel('7-Day Average')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='red', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

hospitalizationAggregate = CVD.groupby(['ndate']).sum().reset_index()
hospitalization60d = hospitalizationAggregate.iloc[-60:]
hospitalization30d = hospitalizationAggregate.iloc[-30:]
hospitalization7d = hospitalizationAggregate.iloc[-7:]


plot_hospitalizations(hospitalizationAggregate, 'Aggregate 7-Day Running Average', size=4)
plot_hospitalizations(hospitalization60d, 'Past 60 Days 7-Day Running Average', size=4)
plot_hospitalizations(hospitalization30d, 'Past 30 Days 7-Day Running Average', size=4)
plot_hospitalizations(hospitalization7d, 'Past 7 Days 7-Day Running Average', size=4)


#=================================================================================
# 7-Day Running Average Adults vs Peds
#=================================================================================
def plot_peds (df, title='7-Day Running Average Hospitalization', size = 1):
    f, ax = plt.subplots(1,1, figsize=(4*size,2*size))
    g = sns.lineplot(x="ndate", y="PedsAcutePatients7D", data=df, color='blue', label="Peds Acute")
    g = sns.lineplot(x="ndate", y="PedsICUPatients7D", data=df, color='green', label="Peds ICU")

    plt.xlabel('Date')
    plt.ylabel('7-Day Average')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='red', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

cvd_case_rate_aggregate = CVD.groupby(['ndate']).sum().reset_index()
sevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
sevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
sevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]


plot_peds(cvd_case_rate_aggregate, 'Hospitalizations Aggregate 7-Day Running Average', size=4)
plot_peds(sevenDayAverage60day, 'Hospitalizations Past 60 Days 7-Day Running Average', size=4)
plot_peds(sevenDayAverage30day, 'Hospitalizations Past 30 Days 7-Day Running Average', size=4)
plot_peds(sevenDayAverage7day, ' Hospitalizations Past 7 Days 7-Day Running Average', size=4)
