import datetime

#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"
 
import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
import os


USAPopulation=328239523

#Pulling Data Frame
USACOVID=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv")

#Formatting Date
USACOVID['date'] = [dt.datetime.strptime(x,'%Y-%m-%d') for x in USACOVID['date']] 

#Adding Additional columns
USACOVID['CasesDaily'] = USACOVID['cases'].diff()
USACOVID['Cases7D'] = USACOVID['CasesDaily'].rolling(window=7).mean()
USACOVID['DailyCases100k'] = (USACOVID['CasesDaily'] / USAPopulation) * 100000
USACOVID['Cases100k7D'] = USACOVID['DailyCases100k'].rolling(window=7).mean()
USACOVID['TotalCasesPast7Days'] = USACOVID['CasesDaily'].rolling(window=7).sum()

USACOVID['DailyDeaths'] = USACOVID['deaths'].diff()
USACOVID['Deaths7D'] = USACOVID['DailyDeaths'].rolling(window=7).mean()
USACOVID['DailyDeaths100k'] = (USACOVID['DailyDeaths'] / USAPopulation) * 100000
USACOVID['Deaths100k7D'] = USACOVID['DailyDeaths100k'].rolling(window=7).mean()

USACOVID['Cases100k7DDiff'] = USACOVID['Cases100k7D'].diff()
USACOVID['TotalCasesPast7Days'] = USACOVID['CasesDaily'].rolling(window=7).sum()
USACOVID['TotalCasespast7days100k'] = (USACOVID['TotalCasesPast7Days'] / USAPopulation) * 100000

print (USACOVID.dtypes)
print(USACOVID.tail(60))

USACOVID.to_csv('USA_Data.csv')



#=================================================================================
# 7-Day Running Average
#=================================================================================
def plot_USA_7davg (df, title='7-Day Case Count', size = 1):
    f, ax = plt.subplots(1,1, figsize=(4*size,2*size))
    g = sns.lineplot(x="date", y="Cases7D", data=df, color='blue', label="United States")
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

USACOVID_case_rate_aggregate = USACOVID.groupby(['date']).sum().reset_index()
USAsevenDayAverage60day = USACOVID_case_rate_aggregate.iloc[-60:]
USAsevenDayAverage30day = USACOVID_case_rate_aggregate.iloc[-30:]
USAsevenDayAverage7day = USACOVID_case_rate_aggregate.iloc[-7:]

plot_USA_7davg(USACOVID_case_rate_aggregate, 'USA Aggregate 7-Day Running Average', size=4)
plot_USA_7davg(USAsevenDayAverage60day, 'USA Past 60 Days 7-Day Running Average', size=4)
plot_USA_7davg(USAsevenDayAverage30day, 'USA Past 30 Days 7-Day Running Average', size=4)
plot_USA_7davg(USAsevenDayAverage7day, 'USA Past 7 Days 7-Day Running Average', size=4)

#=================================================================================
# Aggregate Case Rate
#=================================================================================
def plot_USA_case_rate(df, title='County Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="date", y="Cases100k7D", data=df, color='blue', label="USA Case Rate")

    plt.xlabel('Date')
    plt.ylabel(' Cases per 100k ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='solid', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

USA_case_rate_aggregate = USACOVID.groupby(['date']).sum().reset_index()
USAcvd60d = USA_case_rate_aggregate.iloc[-60:]
USAcvd30d = USA_case_rate_aggregate.iloc[-30:]
USAcvd7d = USA_case_rate_aggregate.iloc[-7:]

plot_USA_case_rate(USA_case_rate_aggregate, 'Aggregate USA Case Rate', size=4)
plot_USA_case_rate(USAcvd60d, 'USA Case Rate Past 60 Days', size=4)
plot_USA_case_rate(USAcvd30d, 'USA Case Rate Past 30 Days', size=4)
plot_USA_case_rate(USAcvd7d, 'USA Case Rate Past 7 Days', size=4)
