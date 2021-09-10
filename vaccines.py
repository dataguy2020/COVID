#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

statePopulation = 6045680

CVD = pd.read_csv('https://opendata.arcgis.com/datasets/41a6599ef5ab42d09d69a479dfebf6d3_0.csv')

CVD['ReportDate'] = CVD['ReportDate']+'00'


#Convert string value of date to datetime format
CVD['ReportDate'] = [dt.datetime.strptime(x,'%Y/%m/%d %H:%M:%S%z') 
               for x in CVD['ReportDate']] 


#Creating a new index and sorting by that index
CVD.set_index('ReportDate', drop=True, append=False, inplace=True, verify_integrity=False)
CVD = CVD.sort_index()

CVD['FirstDose_7Day'] = CVD['FirstDose_AdminDaily'].rolling(window=7).mean()
CVD['SecondDose_7Day'] = CVD['SecDose_AdminDaily'].rolling(window=7).mean()
CVD['SingleDose_7Day'] = CVD['SingleDose_AdminDaily'].rolling(window=7).mean()
CVD['TotalDoses_7Day'] = CVD['Total_AdminDaily'].rolling(window=7).mean()

print (CVD.dtypes)
print(CVD.tail())

def plot_state_vaccines(df, title='7-Day Vaccine Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="FirstDose_7Day", data=df, color='blue', label="First Dose")
    g = sns.lineplot(x="ReportDate", y="SecondDose_7Day", data=df, color='red', label="Second Dose")
    g = sns.lineplot(x="ReportDate", y="SingleDose_7Day", data=df, color='green', label="Single Dose")
    #g = sns.lineplot(x="ReportDate", y="TotalDoses_7Day", data=df, color='orange', label="Total Dose")


    plt.xlabel('ReportDate')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=45)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()


cvd_vacine_aggregate = CVD.groupby(['ReportDate']).sum().reset_index()
cvd_vaccine_60days = cvd_vacine_aggregate.iloc[-60:]
cvd_vaccine_30days = cvd_vacine_aggregate.iloc[-30:]
cvd_vaccine_45days = cvd_vacine_aggregate.iloc[-45:]
cvd_vaccine_7days = cvd_vacine_aggregate.iloc[-7:]

plot_state_vaccines(cvd_vacine_aggregate, 'VACCINE - Maryland Aggregate 7-Day Running Average', size=4)
plot_state_vaccines(cvd_vaccine_60days, 'VACCINE - Maryland 7-Day Average Past 60 Days', size=4)
plot_state_vaccines(cvd_vaccine_30days, 'VACCINE - Maryland 7-Day Average Past 30 Days', size=4)
plot_state_vaccines(cvd_vaccine_45days, 'VACCINE - Maryland 7-Day Average Past 45 Days', size=4)
plot_state_vaccines(cvd_vaccine_7days, 'VACCINE - Maryland 7-Day Average Past 7 Days', size=4)

    
