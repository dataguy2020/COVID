# !/usr/bin/env python
author = "Michael Brown"
license = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from datetime import timedelta
import seaborn as sns


from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# ===================================================================
# Example of Calcuation for Case Rate
# ===================================================================
# CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
# CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()



CVD = pd.read_csv('https://opendata.maryland.gov/api/views/mgd3-qk8t/rows.csv?accessType=DOWNLOAD')

#Creating new data frame 
AACounty = pd.DataFrame()
AACounty['ReportDate'] = CVD['ReportDate']
AACounty['DataDate'] = CVD['ReportDate']

#converting Report Date to string
AACounty['ReportDate'] = AACounty['ReportDate'].astype('str')
AACounty['DataDate'] = AACounty['DataDate'].astype('str')


#getting the date portion of the string
AACounty['ReportDate'] = AACounty.ReportDate.str.slice(0,10)
AACounty['DataDate'] = AACounty.DataDate.str.slice(0,10)
AACounty['Year'] = AACounty.DataDate.str.slice(6,10)
#AACounty['Year'] = pd.to_numeric(AACounty['Year'],errors = 'coerce')
AACounty['Year'] = AACounty['Year'].astype(float, errors = 'raise')
      
#converting string to date format
AACounty['ReportDate'] = [dt.datetime.strptime(x, '%m/%d/%Y')
                for x in AACounty['ReportDate']]

AACounty['DataDate'] = [dt.datetime.strptime(x, '%m/%d/%Y')
                for x in AACounty['DataDate']]

#adding new column for data date vs reported date - data date is 1 day prior to report date
AACounty['DataDate'] = AACounty['DataDate'] - timedelta(days=1)  


AnneArundelPopulationDecennial2020 =588261
AnneArundelPOpulationACS2020 = 575421
AnneArundelPopulationACS2019 = 571275
AnneArundelPopulationPEP2019 = 579234
AnneArundelPopulationCounty = 579630




def yearcondition(x):
    if x == 2019:
        return "579234."
    elif x == 2020:
        return " 588769 "
    elif x == 2021:
        return "590336"
    elif x == 2022:
        return "590336"
    else:
        return "0"
    
AACounty['Pop1'] = AACounty['Year'].apply(yearcondition)
AACounty['Pop1'] = AACounty['Pop1'].astype(float, errors = 'raise')



#Anne Arundel
AACounty['AnneArundel'] = CVD['ANNE']
AACounty['AADailyCases'] = AACounty['AnneArundel'].diff()
AACounty['AAWeeklyCases'] = AACounty['AADailyCases'].rolling(window=7).sum()
AACounty['AA7Day'] = AACounty['AADailyCases'].rolling(window=7).mean()
AACounty['AAWeekly100k'] = (AACounty['AAWeeklyCases'] / AACounty['Pop1']) * 100000
AACounty['AAWeekly100k1'] = (AACounty['AAWeeklyCases'] /AnneArundelPopulationCounty) * 100000


AACounty['AADaily100k2020Census'] = (AACounty['AADailyCases'] / AnneArundelPopulationDecennial2020) * 100000
AACounty['AA100k7D-2020Census'] = AACounty['AADaily100k2020Census'].rolling(window=7).mean()

AACounty['AACounty100k2020ACS'] = (AACounty['AADailyCases'] / AnneArundelPOpulationACS2020) * 100000
AACounty['AA100k7D-2020ACS'] = AACounty['AACounty100k2020ACS'].rolling(window=7).mean()


AACounty['AADaily100k2019ACS'] = (AACounty['AADailyCases'] / AnneArundelPopulationACS2019) * 100000
AACounty['AA100k7D-2019ACS'] = AACounty['AADaily100k2019ACS'].rolling(window=7).mean()

AACounty['AADaily100k2019PEP'] = (AACounty['AADailyCases'] / AnneArundelPopulationPEP2019) * 100000
AACounty['AA100k7D-2019PEP'] = AACounty['AADaily100k2019PEP'].rolling(window=7).mean()

AACounty['AADaily100kCounty'] = (AACounty['AADailyCases'] / AnneArundelPopulationCounty) * 100000
AACounty['AA100k7D-County'] = AACounty['AADaily100kCounty'].rolling(window=7).mean()

AACounty['AADaily100kCalc'] = (AACounty['AADailyCases'] / AACounty['Pop1']) * 100000
AACounty['AA100k7D-Calc'] = AACounty['AADaily100kCalc'].rolling(window=7).mean()

# Saving Data to CSV
print(AACounty.dtypes)
AACounty.to_csv('AnneArundel.csv')

print(AACounty.tail())

#=================================================================================
# 7-Day Running Average - Daily Cases
#=================================================================================

def plot_county_7DAvg(df, title='7-Day Case Count', size=1):
    #=================================================================================
    # 7-Day Running Average - Daily Cases - All Counties
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="DataDate", y="AA7Day", data=df, color='red', label="Anne Arundel")
    plt.legend(loc='upper left')
    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



cvd_case_rate_aggregate = AACounty.groupby(['DataDate']).sum().reset_index()
sevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
sevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
sevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]
print ("Priot to first plot")
plot_county_7DAvg(cvd_case_rate_aggregate, 'County Aggregate 7-Day Running Average', size=4)
print ("After first plot")
plot_county_7DAvg(sevenDayAverage60day, 'County Past 60 Days 7-Day Running Average', size=4)
plot_county_7DAvg(sevenDayAverage30day, 'County Past 30 Days 7-Day Running Average', size=4)
plot_county_7DAvg(sevenDayAverage7day, 'County Past 7 Days 7-Day Running Average', size=4)


def plot_aacounty_7D100kAvg(df, title='Aggregate Anne Arundel County Case Rate', size=1):

    #=================================================================================
    # 7-Day Running Average - Case Rate - Anne Arundel County
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(5 * size, 3 * size))
    g = sns.lineplot(x="DataDate", y="AA100k7D-2020Census", data=df, color='black', linewidth=3.0, label="Anne Arundel Decennial 2020")
    g = sns.lineplot(x="DataDate", y="AA100k7D-2020ACS", data=df, color = 'darkgreen', linewidth=2.0, label="Anne Arundel ACS 2020")
    g = sns.lineplot(x="DataDate", y="AA100k7D-2019PEP", data=df, color='darkblue', linewidth=3.0, label="Anne Arundel PEP 2019 Estimate")
    g = sns.lineplot(x="DataDate", y="AA100k7D-2019ACS", data=df, color='darkmagenta', linewidth=2.0, label="Anne Arundel ACS 2019 Estimate")
    g = sns.lineplot(x="DataDate", y="AA100k7D-County", data=df, color='red', linewidth=2.0, label="Anne Arundel County Reported Estimate")
    g = sns.lineplot(x="DataDate", y="AA100k7D-Calc", data=df, color='coral', linewidth=2.0, label="Anne Arundel Calcualation - Census")



    #g = sns.lineplot(x="ReportDate", y="AA100k7D", data=df, color='green', label="Anne Arundel")
    plt.rcParams["figure.figsize"] = (200,100)    
    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    ax.tick_params(labelsize = 12)
    ax.annotate('Arundel Arundel Estimate - What the county utilizes \n Anne Arundel Calc - utilizes PEP data for 2019-2021. 2022 utilizes the same data as 2021',
            xy = (1.0, -0.2),
            xycoords='axes fraction',
            ha='right',
            va="center",
            fontsize=13)
    plt.savefig(f'{title}.png')
    plt.show()

aasevenday100kcvd_case_rate_aggregate = AACounty.groupby(['DataDate']).sum().reset_index()
aasevenday100ksevenDayAverage60day = aasevenday100kcvd_case_rate_aggregate.iloc[-60:]
aasevenday100ksevenDayAverage30day = aasevenday100kcvd_case_rate_aggregate.iloc[-30:]
aasevenday100ksevenDayAverage7day = aasevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_aacounty_7D100kAvg(aasevenday100kcvd_case_rate_aggregate, 'County Case Rate Aggregate 7-Day Running Average', size=4)
plot_aacounty_7D100kAvg(aasevenday100ksevenDayAverage60day, 'County Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_aacounty_7D100kAvg(aasevenday100ksevenDayAverage30day, 'County Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_aacounty_7D100kAvg(aasevenday100ksevenDayAverage7day, 'County Case Rate  Past 7 Days 7-Day Running Average', size=4)

####################

def plot_aacounty1_7D100kAvg(df, title='Aggregate Anne Arundel County Case Rate', size=1):

    #=================================================================================
    # 7-Day Running Average - Case Rate - Anne Arundel County
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(5 * size, 3 * size))
    g = sns.lineplot(x="DataDate", y="AA100k7D-County", data=df, color='red', linewidth=2.0, label="Anne Arundel Estimate")
    g = sns.lineplot(x="DataDate", y="AA100k7D-Calc", data=df, color='black', linewidth=1.0, label="Anne Arundel Calculation")



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

aa1sevenday100kcvd_case_rate_aggregate = AACounty.groupby(['DataDate']).sum().reset_index()
aa1sevenday100ksevenDayAverage60day = aa1sevenday100kcvd_case_rate_aggregate.iloc[-60:]
aa1sevenday100ksevenDayAverage30day = aa1sevenday100kcvd_case_rate_aggregate.iloc[-30:]
aa1sevenday100ksevenDayAverage7day = aa1sevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_aacounty1_7D100kAvg(aasevenday100kcvd_case_rate_aggregate, 'County1 Case Rate Aggregate 7-Day Running Average', size=4)
plot_aacounty1_7D100kAvg(aasevenday100ksevenDayAverage60day, 'County1 Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_aacounty1_7D100kAvg(aasevenday100ksevenDayAverage30day, 'County1 Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_aacounty1_7D100kAvg(aasevenday100ksevenDayAverage7day, 'County1 Case Rate  Past 7 Days 7-Day Running Average', size=4)

######

def plot_aacounty_weekly7D100kAvg(df, title='Aggregate Anne Arundel County Case Rate', size=1):

    #=================================================================================
    # 7-Day Running Average - Case Rate - Anne Arundel County
    #=================================================================================
    f, ax = plt.subplots(1, 1, figsize=(5 * size, 3 * size))
    g = sns.lineplot(x="DataDate", y="AAWeekly100k", data=df, color='purple', linewidth=3.0, label="Anne Arundel Weekly Cases Case Rate - Calculated")
    g = sns.lineplot(x="DataDate", y="AAWeekly100k1", data=df, color='red', linewidth=3.0, label="Anne Arundel Weekly Cases Case Rate - County Data")

    plt.rcParams["figure.figsize"] = (200,100)    
    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    ax.tick_params(labelsize = 12)
    plt.savefig(f'{title}.png')
    plt.show()

weeklyaa100kcvd_case_rate_aggregate = AACounty.groupby(['DataDate']).sum().reset_index()
weeklyaa100ksevenDayAverage60day = weeklyaa100kcvd_case_rate_aggregate.iloc[-60:]
weeklyaa100ksevenDayAverage30day = weeklyaa100kcvd_case_rate_aggregate.iloc[-30:]
weeklyaa100ksevenDayAverage7day = weeklyaa100kcvd_case_rate_aggregate.iloc[-7:]
plot_aacounty_weekly7D100kAvg(weeklyaa100kcvd_case_rate_aggregate, 'Weekly County Case Rate Aggregate 7-Day Running Average', size=4)
plot_aacounty_weekly7D100kAvg(weeklyaa100ksevenDayAverage60day, 'Weekly County Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_aacounty_weekly7D100kAvg(weeklyaa100ksevenDayAverage30day, 'Weekly County Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_aacounty_weekly7D100kAvg(weeklyaa100ksevenDayAverage7day, 'Weekly County Case Rate  Past 7 Days 7-Day Running Average', size=4)
