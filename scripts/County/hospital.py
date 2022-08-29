#!/usr/bin/python

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from datetime import timedelta
import seaborn as sns
from warnings import simplefilter


hospital = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/COVID/master/datasets/Maryland/AnneArundel/hospitalizations.csv')

#print(hospital.dtypes)
#print(hospital.head(5))
hospital['Year'] = hospital.Date.str.slice(6,10)
hospital['Acute'] = hospital['Acute'].astype(float, errors='raise')
hospital['Total'] = hospital['Acute'] + hospital['ICU']
hospital['Date'] = [dt.datetime.strptime(x, '%m/%d/%Y')
                    for x in hospital['Date']]
hospital['Year'] = hospital['Year'].astype(float, errors='raise')
#print(hospital.dtypes)


def yearcondition(x):
    if x == 19:
        return "579234"
    elif x == 20:
        return "588769"
    elif x == 21:
        return "590336"
    elif x == 22:
        return "590336"
    else:
        return "0"
    
hospital['Population'] = hospital['Year'].apply(yearcondition)
hospital['Population'] = hospital['Population'].astype(float, errors='raise')


#ACUTE BEDS
hospital['AcuteDaily'] = hospital['Acute']
hospital['Acute7Day'] = hospital['AcuteDaily'].rolling(window=7).mean()
hospital['AcuteDaily100k'] = (hospital['AcuteDaily'] / hospital['Population']) * 100000
hospital['Acute100k7D'] = hospital['AcuteDaily100k'].rolling(window=7).mean()

#ICU BEDS
hospital['ICUDaily'] = hospital['ICU']
hospital['ICU7Day'] = hospital['ICUDaily'].rolling(window=7).mean()
hospital['ICUDaily100K'] = (hospital['ICUDaily'] / hospital['Population']) * 100000
hospital['ICU100k7D'] = hospital['AcuteDaily100k'].rolling(window=7).mean()

#TOTAL BEDS
hospital['TotalDaily'] = hospital['Total']
hospital['Total7Day'] = hospital['TotalDaily'].rolling(window=7).mean()
hospital['TotalDaily100k'] = (hospital['TotalDaily'] / hospital['Population']) * 100000
hospital['Total100k7D'] = hospital['TotalDaily100k'].rolling(window=7).mean()


print(hospital.dtypes)
hospital.to_csv('AnneArundel-Hospital.csv')


#7Day Averages
def plot_acute_7DAvg(df, title='7-Day Case Count', size=1):
    #=================================================================================
    # 7-Day Running Average - Daily Cases - All Counties
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="Date", y="Acute7Day", data=df, color='blue', label="Acute")
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



cvd_hospital_aggregate = hospital.groupby(['Date']).sum().reset_index()
acutesevenDayAverage60day = cvd_hospital_aggregate.iloc[-60:]
acutesevenDayAverage30day = cvd_hospital_aggregate.iloc[-30:]
acutesevenDayAverage7day = cvd_hospital_aggregate.iloc[-7:]
plot_acute_7DAvg(cvd_hospital_aggregate, 'Acute Aggregate 7-Day Running Average', size=4)
plot_acute_7DAvg(acutesevenDayAverage60day, 'Acute Past 60 Days 7-Day Running Average', size=4)
plot_acute_7DAvg(acutesevenDayAverage30day, 'Acute Past 30 Days 7-Day Running Average', size=4)
plot_acute_7DAvg(acutesevenDayAverage7day, 'Acute Past 7 Days 7-Day Running Average', size=4)

def plot_icu_7DAvg(df, title='7-Day Case Count', size=1):
    #=================================================================================
    # 7-Day Running Average - Daily Cases - All Counties
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="Date", y="ICU7Day", data=df, color='red', label="ICU")
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



cvd_hospital_aggregate = hospital.groupby(['Date']).sum().reset_index()
icusevenDayAverage60day = cvd_hospital_aggregate.iloc[-60:]
icusevenDayAverage30day = cvd_hospital_aggregate.iloc[-30:]
icusevenDayAverage7day = cvd_hospital_aggregate.iloc[-7:]
plot_icu_7DAvg(cvd_hospital_aggregate, 'ICU Aggregate 7-Day Running Average', size=4)
plot_icu_7DAvg(icusevenDayAverage60day, 'ICU Past 60 Days 7-Day Running Average', size=4)
plot_icu_7DAvg(icusevenDayAverage30day, 'ICU Past 30 Days 7-Day Running Average', size=4)
plot_icu_7DAvg(icusevenDayAverage7day, 'ICU Past 7 Days 7-Day Running Average', size=4)

def plot_total_7DAvg(df, title='7-Day Case Count', size=1):
    #=================================================================================
    # 7-Day Running Average - Daily Cases - All Counties
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="Date", y="Total7Day", data=df, color='black', label="Total")
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



cvd_hospital_aggregate = hospital.groupby(['Date']).sum().reset_index()
totalsevenDayAverage60day = cvd_hospital_aggregate.iloc[-60:]
totalsevenDayAverage30day = cvd_hospital_aggregate.iloc[-30:]
totalsevenDayAverage7day = cvd_hospital_aggregate.iloc[-7:]
plot_total_7DAvg(cvd_hospital_aggregate, 'Total Aggregate 7-Day Running Average', size=4)
plot_total_7DAvg(totalsevenDayAverage60day, 'Total Past 60 Days 7-Day Running Average', size=4)
plot_total_7DAvg(totalsevenDayAverage30day, 'Total Past 30 Days 7-Day Running Average', size=4)
plot_total_7DAvg(totalsevenDayAverage7day, 'Total Past 7 Days 7-Day Running Average', size=4)

def plot_hospitaltotal_7d100k(df, title='Aggregate Anne Arundel County Case Rate', size=1):

    #=================================================================================
    # 7-Day Running Average - Case Rate - Anne Arundel County
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(5 * size, 3 * size))
    g = sns.lineplot(x="Date", y="Total100k7D", data=df, color='red', linewidth=2.0, label="Total Hospitalization Case Rate")


    #g = sns.lineplot(x="ReportDate", y="AA100k7D", data=df, color='green', label="Anne Arundel")
    plt.rcParams["figure.figsize"] = (200,100)    
    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    ax.tick_params(labelsize = 14)
    #ax.tick_params(labelsize = 14)
    #ax.annotate('Footnote added below the chart with a smaller font',
    #        xy = (1.0, -0.2),
    #        xycoords='axes fraction',
    #        ha='right',
    #        va="center",
    #        fontsize=10)
    plt.savefig(f'{title}.png')
    plt.show()

hosptialtotal100kcvd_case_rate_aggregate = hospital.groupby(['Date']).sum().reset_index()
hospitaltotalsevenday100ksevenDayAverage60day = hosptialtotal100kcvd_case_rate_aggregate.iloc[-60:]
hospitaltotalsevenday100ksevenDayAverage30day = hosptialtotal100kcvd_case_rate_aggregate.iloc[-30:]
hospitaltotalsevenday100ksevenDayAverage7day = hosptialtotal100kcvd_case_rate_aggregate.iloc[-7:]
plot_hospitaltotal_7d100k(hosptialtotal100kcvd_case_rate_aggregate, 'Total Hospitalizations Case Rate Aggregate 7-Day Running Average', size=4)
plot_hospitaltotal_7d100k(hospitaltotalsevenday100ksevenDayAverage60day, 'Total Hospitalizations Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_hospitaltotal_7d100k(hospitaltotalsevenday100ksevenDayAverage30day, 'Total Hospitalizations Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_hospitaltotal_7d100k(hospitaltotalsevenday100ksevenDayAverage7day, 'Total Hospitalizations Case Rate  Past 7 Days 7-Day Running Average', size=4)
