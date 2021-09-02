
#!/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns


CVD = pd.read_csv('https://opendata.arcgis.com/datasets/68fbe34617cd450aa423e27692f503b0_0.csv')

CVD['DATE'] = CVD['DATE']+'00'


#Convert string value of date to datetime format
CVD['DATE'] = [dt.datetime.strptime(x,'%Y/%m/%d %H:%M:%S%z') 
               for x in CVD['DATE']] 

CVD.set_index('DATE', drop=True, append=False, inplace=True, verify_integrity=False)
CVD = CVD.sort_index()

#Data from https://opendata.maryland.gov/Demographic/Total-Population-Projections-by-Age-Sex-and-Race/5zc8-s5s9/data
tenderAgePopulation = 727307
teenagers = 778417
twentys = 800843
thirties = 844607
fourties = 754794
fifties = 851548
sixtes = 726078 
seventies = 427998
eightyplus = 230216

totalPopulation = 6141808
Under40Population = 3151174
Over40Population = 2990634
k12population = 1505724 #0-19
collegePopulation = 800843 #20s and #30s

CVD['schoolKids'] = CVD['Age_0_to_9'] + CVD['Age_10_to_19']

#daily cases
CVD['Age_0_to_9_daily'] = CVD['Age_0_to_9'].diff()
CVD['Age_10_to_19_daily'] = CVD['Age_10_to_19'].diff()
CVD['Age_20_to_29_daily'] = CVD['Age_20_to_29'].diff()
CVD['Age_30_to_39_daily'] = CVD['Age_30_to_39'].diff()
CVD['Age_40_to_49_daily'] = CVD['Age_40_to_49'].diff()
CVD['Age_50_to_59_daily'] = CVD['Age_50_to_59'].diff()
CVD['Age_60_to_69_daily'] = CVD['Age_60_to_69'].diff()
CVD['Age_70_to_79_daily'] = CVD['Age_70_to_79'].diff()
CVD['Age_80plus_daily'] = CVD['Age_80plus'].diff()
CVD['schoolKidsDaily'] = CVD['schoolKids'].diff()

#Creating 7Day 
CVD['tenderAge'] = CVD['Age_0_to_9_daily'].rolling(window=7).mean()
CVD['teenagers'] = CVD['Age_10_to_19_daily'].rolling(window=7).mean()
CVD['20s'] = CVD['Age_20_to_29_daily'].rolling(window=7).mean()
CVD['30s'] = CVD['Age_30_to_39_daily'].rolling(window=7).mean()
CVD['40s'] = CVD['Age_40_to_49_daily'].rolling(window=7).mean()
CVD['50s'] = CVD['Age_50_to_59_daily'].rolling(window=7).mean()
CVD['60s'] = CVD['Age_60_to_69_daily'].rolling(window=7).mean()
CVD['70s'] = CVD['Age_70_to_79_daily'].rolling(window=7).mean()
CVD['80Plus'] = CVD['Age_80plus_daily'].rolling(window=7).mean()
CVD['schoolKids7D'] = CVD['schoolKidsDaily'].rolling(window=7).mean()

#Daily per Capita
#CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
CVD['0_9daily100k'] = (CVD['Age_0_to_9_daily'] /tenderAgePopulation ) * 100000
CVD['10_19daily100k'] = (CVD['Age_10_to_19_daily'] /teenagers ) * 100000
CVD['20_29daily100k'] = (CVD['Age_20_to_29_daily'] /twentys ) * 100000
CVD['30_39daily100k'] = (CVD['Age_30_to_39_daily'] /thirties ) * 100000
CVD['40_49daily100k'] = (CVD['Age_40_to_49_daily'] /fourties ) * 100000
CVD['50_59daily100k'] = (CVD['Age_50_to_59_daily'] /fifties ) * 100000
CVD['60_69daily100k'] = (CVD['Age_60_to_69_daily'] /sixtes ) * 100000
CVD['70_79daily100k'] = (CVD['Age_70_to_79_daily'] /seventies ) * 100000
CVD['80plusdaily100k'] = (CVD['Age_80plus_daily'] /eightyplus ) * 100000
CVD['schoolKidsdaily100K'] = (CVD['schoolKidsDaily'] /k12population ) * 100000

#7DayPerCapita
CVD['0_97D100k'] = CVD['0_9daily100k'].rolling(window=7).mean()
CVD['10_197D100k'] = CVD['10_19daily100k'].rolling(window=7).mean()
CVD['20_297D100k'] = CVD['20_29daily100k'].rolling(window=7).mean()
CVD['30_397D100k'] = CVD['30_39daily100k'].rolling(window=7).mean()
CVD['40_497D100k'] = CVD['40_49daily100k'].rolling(window=7).mean()
CVD['50_597D100k'] = CVD['50_59daily100k'].rolling(window=7).mean()
CVD['60_697D100k'] = CVD['60_69daily100k'].rolling(window=7).mean()
CVD['70_797D100k'] = CVD['70_79daily100k'].rolling(window=7).mean()
CVD['80plus7D100k'] = CVD['80plusdaily100k'].rolling(window=7).mean()
CVD['schoolKids7D100K'] = CVD['schoolKidsdaily100K'].rolling(window=7).mean()
print (CVD.dtypes)

print(CVD.tail())


CVD.to_csv(r'COVIDbyAge.csv')


def plot_cases_by_age(df, title='7-Day COVID Cases by Age', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="DATE", y="tenderAge", data=df, color='blue', label="0-10")
    g = sns.lineplot(x="DATE", y="teenagers", data=df, color='orange', label="10-19")
    g = sns.lineplot(x="DATE", y="20s", data=df, color='green', label="20-29")
    g = sns.lineplot(x="DATE", y="30s", data=df, color='red', label="30-39")
    g = sns.lineplot(x="DATE", y="40s", data=df, color='purple', label="40-49")
    g = sns.lineplot(x="DATE", y="50s", data=df, color='brown', label="50-59")
    g = sns.lineplot(x="DATE", y="60s", data=df, color='pink', label="60-69")
    g = sns.lineplot(x="DATE", y="70s", data=df, color='olive', label="70-79")
    g = sns.lineplot(x="DATE", y="80Plus", data=df, color='cyan', label="80 & Older")
    g = sns.lineplot(x="DATE", y="schoolKids7D", data=df, color='black', label="0-19")



    plt.xlabel('DATE')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=45)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

    
casesByAge_aggregate = CVD.groupby(['DATE']).sum().reset_index()
casesByAge_aggregate_60days = casesByAge_aggregate.iloc[-60:]
casesByAge_aggregate_30days = casesByAge_aggregate.iloc[-30:]
casesByAge_aggregate_7days = casesByAge_aggregate.iloc[-7:]

plot_cases_by_age(casesByAge_aggregate, 'State Aggregate 7-Day Running Average', size=4)
plot_cases_by_age(casesByAge_aggregate_60days, 'State 7-Day Average Past 60 Days', size=4)
plot_cases_by_age(casesByAge_aggregate_30days, 'State 7-Day Average Past 30 Days', size=4)
plot_cases_by_age(casesByAge_aggregate_7days, 'State 7-Day Average Past 7 Days', size=4)

#Cases per Age per capita
def plot_casesbyage_percapita(df, title='Maryland State Cases by Age per Capita', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="DATE", y="0_97D100k", data=df, color='blue', label="0-10")
    g = sns.lineplot(x="DATE", y="10_197D100k", data=df, color='orange', label="10-19")
    g = sns.lineplot(x="DATE", y="20_297D100k", data=df, color='green', label="20-29")
    g = sns.lineplot(x="DATE", y="30_397D100k", data=df, color='red', label="30-39")
    g = sns.lineplot(x="DATE", y="40_497D100k", data=df, color='purple', label="40-49")
    g = sns.lineplot(x="DATE", y="50_597D100k", data=df, color='brown', label="50-59")
    g = sns.lineplot(x="DATE", y="60_697D100k", data=df, color='pink', label="60-69")
    g = sns.lineplot(x="DATE", y="70_797D100k", data=df, color='olive', label="70-79")
    g = sns.lineplot(x="DATE", y="80plus7D100k", data=df, color='cyan', label="80 & Older")
    g = sns.lineplot(x="DATE", y="schoolKids7D100K", data=df, color='black', label="0-19")

    
    plt.xlabel('DATE')
    plt.ylabel(' Cases per 100k ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()


casesbyage_rate_aggregate = CVD.groupby(['DATE']).sum().reset_index()
cvd60d = casesbyage_rate_aggregate.iloc[-60:]
cvd30d = casesbyage_rate_aggregate.iloc[-30:]
cvd7d = casesbyage_rate_aggregate.iloc[-7:]

plot_casesbyage_percapita(casesbyage_rate_aggregate, 'Cases per Age Case Rate', size=4)
plot_casesbyage_percapita(cvd60d, 'Cases per Age Past  60 Days State Case Rate', size=4)
plot_casesbyage_percapita(cvd30d, 'Cases per Age Past 30 Days  State Case Rate', size=4)
plot_casesbyage_percapita(cvd7d, 'Cases per Age Past 7 Days State Case Rate', size=4)
