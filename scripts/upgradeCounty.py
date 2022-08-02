# !/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import timedelta

from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

# ===================================================================
# County Populations from the State of the Maryland
# Source - https://opendata.maryland.gov/api/views/5zc8-s5s9/rows.csv 2020 Total
# ===================================================================

# ==============================
# Below are the different regions of Maryland
# ==============================
# Western Region - Alleghany, Garrett, Washington
# Southern Region - Calvert, Charles, Somerset
# Central Region - Baltimore County, Baltimore City, Anne Arundel, Harford, Caroll, Howard
# Capital Region - Montgomery, Prince George's, Fredrick
# Eastern Shore Region - Cecil, Kent, Queen Anne's, Talbot, Caroline, Dorchester, Wicomico, St. Mary's, Worchester
# I-95 Corridor - Baltimore County, Baltimore City, Cecil, Harford, Howard, Prince George's


# ===================================================================
# Example of Calcuation for Case Rate
# ===================================================================
# CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
# CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()


CVD = pd.read_csv('https://opendata.maryland.gov/api/views/mgd3-qk8t/rows.csv?accessType=DOWNLOAD')

#Creating new data frame 
county = pd.DataFrame()
county['ReportDate'] = CVD['ReportDate']

#converting Report Date to string
county['ReportDate'] = county['ReportDate'].astype('str')

#getting the date portion of the string
county['ReportDate'] = county.ReportDate.str.slice(0,10)

#converting string to date format
county['ReportDate'] = [dt.datetime.strptime(x, '%m/%d/%Y')
                for x in county['ReportDate']]

#adding new column for data date vs reported date - data date is 1 day prior to report date
county['DataDate'] = county['ReportDate'] - timedelta(days=1)

#Allegany County
county['Allegany'] = CVD['ALLE']
county['AlleganyDailyCases'] = county['Allegany'].diff()
county['AlleganyDailyCases7Day'] = county['AlleganyDailyCases'].rolling(window=7).mean()
county['AlleganyDaily100K'] = (county['AlleganyDailyCases'] / AlleganyPopulation) * 100000
county['AlleganyDailyCases100k7D'] = county['AlleganyDaily100K'].rolling(window=7).mean()

#Anne Arundel
county['AnneArundel'] = CVD['ANNE']
county['AADailyCases'] = county['AnneArundel'].diff()
county['AA7Day'] = county['AADailyCases'].rolling(window=7).mean()
county['AADaily100k3'] = (county['AADailyCases'] / AnneArundelPopulation) * 100000
county['AA100k7D-2020Census'] = county['AADaily100k3'].rolling(window=7).mean()

#Baltimore County
county['Baltimore'] = CVD['BALT']

#Baltimore City
county['BaltimoreCity'] = CVD['BCITY']

#Calvert County
county['Calvert'] = CVD['CALV']

#Caroline County
county['Caroline'] = CVD['CARO']

#Carroll County
county['Carroll'] = CVD['CARR']

#Cecil County
county['Cecil'] = CVD['CECI']

#Charles County
county['Charles'] = CVD['CHAR']

#Dorchester County
county['Dorchester'] = CVD['DORC']

#Fredrick County
county['Fredrick'] = CVD['FRED']

#Garrett County
county['Garrett'] = CVD['GARR']

#Harford County
county['Harford'] = CVD['HARF']

#Howard County
county['Howard'] = CVD['HOWA']

#Kent County
county['Kent'] = CVD['KENT']

#Montgomery County
county['Montgomery'] = CVD['MONT']

#Prince George's County
county['PrinceGeorges'] = CVD['PRIN']

#QueenAnnes County
county['QueenAnnes'] = CVD['QUEE']

#Somserset County
county['Somerset'] = CVD['SOME']

#St. Marys County
county['StMarys'] = CVD['STMA']

#Talbot County
county['Talbot'] = CVD['TALB']

#Washington County
county['Washington'] = CVD['WASH']

#WIcomico County
county['Wicomico'] = CVD['WICO']

#Worcester County
county['Worcester'] = CVD['WORC']



#print (county.dtypes)
#print(county.tail())

county.to_csv('CountyTest.csv')


#Anne Arundel


#Baltimore
county['BaltimoreDailyCases'] = county['Baltimore'].diff()
county['Baltimore7Day'] = county['BaltimoreDailyCases'].rolling(window=7).mean()
county['BaltimoreDaily100k'] = (county['BaltimoreDailyCases'] / BaltimorePopulation) * 100000
county['Baltimore7D100k'] = county['BaltimoreDaily100k'].rolling(window=7).mean()

#Baltimore City
county['BaltCityDailyCases'] = county['BaltimoreCity'].diff()
county['BaltCity7Day'] = county['BaltCityDailyCases'].rolling(window=7).mean()
county['BaltCityeDaily100k'] = (county['BaltCityDailyCases'] / BaltimoreCityPopulation) * 100000
county['BaltCity7D100k'] = county['BaltCityeDaily100k'].rolling(window=7).mean()

#Calvert
county['CalvertDailyCase'] = county['Calvert'].diff()
county['Calvert7Day'] = county['CalvertDailyCase'].rolling(window=7).mean()
county['CalverteDaily100k'] = (county['CalvertDailyCase'] / CalvertPopulation) * 100000
county['Calvert7D100k'] = county['CalverteDaily100k'].rolling(window=7).mean()

#Caroline
county['CarolineDailyCases'] = county['Caroline'].diff()
county['Caroline7Day'] = county['CarolineDailyCases'].rolling(window=7).mean()
county['CarolineDaily100k'] = (county['CarolineDailyCases'] / CarolinePopulation) * 100000
county['Caroline7D100k'] = county['CarolineDaily100k'].rolling(window=7).mean()

#Carroll
county['CarrollDaily'] = county['Carroll'].diff()
county['Carroll7Day'] = county['CarrollDaily'].rolling(window=7).mean()
county['CarrollDaily100k'] = (county['CarrollDaily'] / CarrollPopulation) * 100000
county['Carroll7D100k'] = county['CarrollDaily100k'].rolling(window=7).mean()

#Cecil
county['CecilDaily'] = county['Cecil'].diff()
county['Cecil7Day'] = county['CecilDaily'].rolling(window=7).mean()
county['CecilDaily100k'] = (county['CecilDaily'] / CecilPopulation) * 100000
county['Cecil7D100k'] = county['CecilDaily100k'].rolling(window=7).mean()

#Charles
county['CharlesDaily'] = county['Charles'].diff()
county['Charles7Day'] = county['CharlesDaily'].rolling(window=7).mean()
county['CharlesDaily100K'] = (county['CharlesDaily'] / CharlesPopulation) * 100000
county['Charles7D100k'] = county['CharlesDaily100K'].rolling(window=7).mean()

#Dorchester
county['DorchesterDaily'] = county['Dorchester'].diff()
county['Dorchester7Day'] = county['DorchesterDaily'].rolling(window=7).mean()
county['DorchesterDaily100K'] = (county['DorchesterDaily'] / DorchesterPopulation) * 100000
county['Dorchester7D100k'] = county['DorchesterDaily100K'].rolling(window=7).mean()

#Frederick
county['FrederickDaily'] = county['Fredrick'].diff()
county['Frederick7Day'] = county['FrederickDaily'].rolling(window=7).mean()
county['FrederrickDaily100K'] = (county['FrederickDaily'] / FredrickPopulation) * 100000
county['Frederick7D100k'] = county['FrederrickDaily100K'].rolling(window=7).mean()

#Garrett
county['GarrettDaily'] = county['Garrett'].diff()
county['Garrett7Day'] = county['GarrettDaily'].rolling(window=7).mean()
county['GarrettDaily100k'] = (county['GarrettDaily'] / GarrettPopulation) * 100000
county['Garrett7D100k'] = county['GarrettDaily100k'].rolling(window=7).mean()

#Harford
county['HarfordDaily'] = county['Harford'].diff()
county['Harford7Day'] = county['HarfordDaily'].rolling(window=7).mean()
county['HarfordDaily100k'] = (county['HarfordDaily'] / HarfordPopulation) * 100000
county['Harford7D100k'] = county['HarfordDaily100k'].rolling(window=7).mean()

#Howard
county['HowardDaily'] = county['Howard'].diff()
county['Howard7Day'] = county['HowardDaily'].rolling(window=7).mean()
county['HowardDaily100k'] = (county['HowardDaily'] / HowardPopulation) * 100000
county['Howard7D100k'] = county['HowardDaily100k'].rolling(window=7).mean()

#Kent
county['KentDaily'] = county['Kent'].diff()
county['Kent7Day'] = county['KentDaily'].rolling(window=7).mean()
county['KentDaily100k'] = (county['KentDaily'] / KentPopulation) * 100000
county['Kent7D100k'] = county['KentDaily100k'].rolling(window=7).mean()

#Montgomery 
county['MontgomeryDaily'] = county['Montgomery'].diff()
county['Montgomery7Day'] = county['MontgomeryDaily'].rolling(window=7).mean()
county['MontgomeryDaily100k'] = (county['MontgomeryDaily'] / MontgomeryPopulation) * 100000
county['Montgomery7D100k'] = county['HowardDaily100k'].rolling(window=7).mean()

#PG
county['PGDaily'] = county['PrinceGeorges'].diff()
county['PG7Day'] = county['PGDaily'].rolling(window=7).mean()
county['PGDaily100k'] = (county['PGDaily'] / PGPopulation) * 100000
county['PG7D100k'] = county['PGDaily100k'].rolling(window=7).mean()

#QA
county['QADaily'] = county['QueenAnnes'].diff()
county['QA7Day'] = county['QADaily'].rolling(window=7).mean()
county['QADaily100k'] = (county['QADaily'] / QAPopulation) * 100000
county['QA7D100k'] = county['QADaily100k'].rolling(window=7).mean()

#St Mary 
county['StMarysDaily'] = county['StMarys'].diff()
county['StMarys7Day'] = county['StMarysDaily'].rolling(window=7).mean()
county['StMarysDaily100k'] = (county['StMarysDaily'] / StMaryPopulation) * 100000
county['StMarys7D100k'] = county['StMarysDaily100k'].rolling(window=7).mean()

#Somerset
county['SomersetDaily'] = county['Somerset'].diff()
county['Somerset7Day'] = county['SomersetDaily'].rolling(window=7).mean()
county['SomersetDaily100k'] = (county['SomersetDaily'] / SomersetPopulation) * 100000
county['Somerset7D100k'] = county['SomersetDaily100k'].rolling(window=7).mean()

#Tablot
county['TalbotDaily'] = county['Talbot'].diff()
county['Talbot7Day'] = county['TalbotDaily'].rolling(window=7).mean()
county['TalbotDaily100k'] = (county['TalbotDaily'] / TalbotPopulation) * 100000
county['Talbot7D100k'] = county['TalbotDaily100k'].rolling(window=7).mean()

#Washington 
county['WashingtonDaily'] = county['Washington'].diff()
county['Washington7Day'] = county['WashingtonDaily'].rolling(window=7).mean()
county['WashingtonDaily100k'] = (county['WashingtonDaily'] / WashingtonPopulation) * 100000
county['Washington7D100k'] = county['WashingtonDaily100k'].rolling(window=7).mean()

#Wicomico
county['WicomicoDaily'] = county['Wicomico'].diff()
county['Wicomico7Day'] = county['WicomicoDaily'].rolling(window=7).mean()
county['WicomicoDaily100k'] = (county['WicomicoDaily'] / WicomicoPopulation) * 100000
county['Wicomico7D100k'] = county['WicomicoDaily100k'].rolling(window=7).mean()

#Worcester
county['WorcesterDaily'] = county['Worcester'].diff()
county['Worcester7Day'] = county['WorcesterDaily'].rolling(window=7).mean()
county['WorcesterDaily100k'] = (county['WorcesterDaily'] / WorcesterPopulation) * 100000
county['Worcester7D100k'] = county['WorcesterDaily100k'].rolling(window=7).mean()

#Regional
county['Western'] = county['Allegany'] + county['Garrett'] + county['Washington']
county['southern'] = county['Calvert'] + county['Charles'] + county['Somerset']
county['central'] = county['Baltimore'] + county['BaltimoreCity'] + county['AnneArundel'] + county['Harford'] + county['Carroll'] + county['Howard']
county['capital'] = county['Montgomery'] + county['PrinceGeorges'] + county['Fredrick']
county['Eastern'] = county['Cecil'] + county['Kent'] + county['QueenAnnes'] + county['Talbot'] + county['Caroline'] + county['Dorchester'] + county['Wicomico'] + county['StMarys'] + county['Worcester']
county['I95'] = county['Baltimore'] + county['BaltimoreCity'] + county['Cecil'] + county['Harford'] + county['Howard'] + county['PrinceGeorges']

#Western
county['WesternDaily'] = county['Western'].diff()
county['Western7Day'] = county['WesternDaily'].rolling(window=7).mean()
county['WesternDaily100k'] = (county['WesternDaily'] / WesternPopulation) * 100000
county['Western7D100k'] = county['WesternDaily100k'].rolling(window=7).mean()

#Southern
county['SouthernDaily'] = county['southern'].diff()
county['Southern7Day'] = county['SouthernDaily'].rolling(window=7).mean()
county['SouthernDaily100k'] = (county['SouthernDaily'] / SouthernPopulation) * 100000
county['Southern7D100k'] = county['SouthernDaily100k'].rolling(window=7).mean()

#Central
county['CentralDaily'] = county['central'].diff()
county['Central7Day'] = county['CentralDaily'].rolling(window=7).mean()
county['CentralDaily100k'] = (county['CentralDaily'] / CentralPopulation) * 100000
county['Central7D100k'] = county['CentralDaily100k'].rolling(window=7).mean()

#Capital
county['CapitalDaily'] = county['capital'].diff()
county['Capital7Day'] = county['CapitalDaily'].rolling(window=7).mean()
county['CapitalDaily100k'] = (county['CapitalDaily'] / CapitalPopulation) * 100000
county['Capital7D100k'] = county['CapitalDaily100k'].rolling(window=7).mean()

#Eastern
county['EasternDaily'] = county['Eastern'].diff()
county['Eastern7Day'] = county['EasternDaily'].rolling(window=7).mean()
county['EasternDaily100k'] = (county['EasternDaily'] / EasternShorePopulation) * 100000
county['Eastern7D100k'] = county['EasternDaily100k'].rolling(window=7).mean()

#I95
county['I95Daily'] = county['I95'].diff()
county['I957Day'] = county['I95Daily'].rolling(window=7).mean()
county['I95Daily100k'] = (county['I95Daily'] / I95Population) * 100000
county['I957D100k'] = county['I95Daily100k'].rolling(window=7).mean()

# Saving Data to CSV
print(county.dtypes)
county.to_csv('MDCountyData-Census2020.csv')

#=================================================================================
# 7-Day Running Average - Daily Cases
#=================================================================================
def plot_county_7DAvg(df, title='7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AlleganyDailyCases7Day", data=df, color='black', label="Allegany")
    g = sns.lineplot(x="ReportDate", y="AA7Day", data=df, color='red', label="Anne Arundel")
    g = sns.lineplot(x="ReportDate", y="Baltimore7Day", data=df, color='blue', label="Baltimore County")
    g = sns.lineplot(x="ReportDate", y="BaltCity7Day", data=df, color='salmon', label="Baltimore City")
    g = sns.lineplot(x="ReportDate", y="Calvert7Day", data=df, color='saddlebrown', label="Calvert")
    g = sns.lineplot(x="ReportDate", y="Caroline7Day", data=df, color='orange', label="Caroline")
    g = sns.lineplot(x="ReportDate", y="Carroll7Day", data=df, color='olive', label="Caroll")
    g = sns.lineplot(x="ReportDate", y="Cecil7Day", data=df, color='crimson', label="Cecil")  
    g = sns.lineplot(x="ReportDate", y="Charles7Day", data=df, color='dodgerblue', label="Charles")  
    g = sns.lineplot(x="ReportDate", y="Dorchester7Day", data=df, color='plum', label="Dorchester")
    g = sns.lineplot(x="ReportDate", y="Frederick7Day", data=df, color='darkgreen', label="Frederick")
    g = sns.lineplot(x="ReportDate", y="Garrett7Day", data=df, color='hotpink', label="Garrett")
    g = sns.lineplot(x="ReportDate", y="Harford7Day", data=df, color='blueviolet', label="Harford")
    g = sns.lineplot(x="ReportDate", y="Howard7Day", data=df, color='gray', label="Howard")
    g = sns.lineplot(x="ReportDate", y="Kent7Day", data=df, color='purple', label="Kent")
    g = sns.lineplot(x="ReportDate", y="Montgomery7Day", data=df, color='limegreen', label="Montgomery")
    g = sns.lineplot(x="ReportDate", y="PG7Day", data=df, color='cyan', label="Prince George's")
    g = sns.lineplot(x="ReportDate", y="QA7Day", data=df, color='khaki', label="Queen Anne's")
    g = sns.lineplot(x="ReportDate", y="StMarys7Day", data=df, color='darkorange', label="St. Mary's")
    g = sns.lineplot(x="ReportDate", y="Somerset7Day", data=df, color='indianred', label="Somerset")
    g = sns.lineplot(x="ReportDate", y="Talbot7Day", data=df, color='maroon', label="Talbot")
    g = sns.lineplot(x="ReportDate", y="Washington7Day", data=df, color='steelblue', label="Washington")
    g = sns.lineplot(x="ReportDate", y="Wicomico7Day", data=df, color='navy', label="Wicomico")
    g = sns.lineplot(x="ReportDate", y="Worcester7Day", data=df, color='teal', label="Worcester")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



cvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
sevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
sevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
sevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]
plot_county_7DAvg(cvd_case_rate_aggregate, 'County Aggregate 7-Day Running Average', size=4)
plot_county_7DAvg(sevenDayAverage60day, 'County Past 60 Days 7-Day Running Average', size=4)
plot_county_7DAvg(sevenDayAverage30day, 'County Past 30 Days 7-Day Running Average', size=4)
plot_county_7DAvg(sevenDayAverage7day, 'County Past 7 Days 7-Day Running Average', size=4)

def plot_Western_7DAvg(df, title='Western Region 7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AlleganyDailyCases7Day", data=df, color='black', label="Allegany")
    g = sns.lineplot(x="ReportDate", y="Garrett7Day", data=df, color='hotpink', label="Garrett")
    g = sns.lineplot(x="ReportDate", y="Washington7Day", data=df, color='steelblue', label="Washington")
 
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



westerncvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
westernsevenDayAverage60day = westerncvd_case_rate_aggregate.iloc[-60:]
westernsevenDayAverage30day = westerncvd_case_rate_aggregate.iloc[-30:]
westernsevenDayAverage7day = westerncvd_case_rate_aggregate.iloc[-7:]
plot_Western_7DAvg(cvd_case_rate_aggregate, 'Western Region Aggregate 7-Day Running Average', size=4)
plot_Western_7DAvg(westernsevenDayAverage60day, 'Western Region Past 60 Days 7-Day Running Average', size=4)
plot_Western_7DAvg(westernsevenDayAverage30day, 'Western Region Past 30 Days 7-Day Running Average', size=4)
plot_Western_7DAvg(westernsevenDayAverage7day, 'Western Region Past 7 Days 7-Day Running Average', size=4)

def plot_southern_7DAvg(df, title='Southern Region 7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Calvert7Day", data=df, color='saddlebrown', label="Calvert")
    g = sns.lineplot(x="ReportDate", y="Charles7Day", data=df, color='dodgerblue', label="Charles")  
    g = sns.lineplot(x="ReportDate", y="Somerset7Day", data=df, color='indianred', label="Somerset")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



southerncvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
southernsevenDayAverage60day = southerncvd_case_rate_aggregate[-60:]
southernsevenDayAverage30day = southerncvd_case_rate_aggregate.iloc[-30:]
southernsevenDayAverage7day = southerncvd_case_rate_aggregate.iloc[-7:]
plot_southern_7DAvg(southernsevenDayAverage60day, 'Southern Region Aggregate 7-Day Running Average', size=4)
plot_southern_7DAvg(southernsevenDayAverage60day, 'Southern Region Past 60 Days 7-Day Running Average', size=4)
plot_southern_7DAvg(southernsevenDayAverage30day, 'Southern Region Past 30 Days 7-Day Running Average', size=4)
plot_southern_7DAvg(southernsevenDayAverage7day, 'Southern Region Past 7 Days 7-Day Running Average', size=4)

def plot_central_7DAvg(df, title='Central 7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AA7Day", data=df, color='red', label="Anne Arundel")
    g = sns.lineplot(x="ReportDate", y="Baltimore7Day", data=df, color='blue', label="Baltimore County")
    g = sns.lineplot(x="ReportDate", y="BaltCity7Day", data=df, color='salmon', label="Baltimore City")
    g = sns.lineplot(x="ReportDate", y="Carroll7Day", data=df, color='olive', label="Caroll")
    g = sns.lineplot(x="ReportDate", y="Harford7Day", data=df, color='blueviolet', label="Harford")
    g = sns.lineplot(x="ReportDate", y="Howard7Day", data=df, color='gray', label="Howard")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

centralcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
centralsevenDayAverage60day = centralcvd_case_rate_aggregate.iloc[-60:]
centralsevenDayAverage30day = centralcvd_case_rate_aggregate.iloc[-30:]
centralsevenDayAverage7day = centralcvd_case_rate_aggregate.iloc[-7:]
plot_central_7DAvg(centralcvd_case_rate_aggregate, 'Central Region Aggregate 7-Day Running Average', size=4)
plot_central_7DAvg(centralsevenDayAverage60day, 'Central Region Past 60 Days 7-Day Running Average', size=4)
plot_central_7DAvg(centralsevenDayAverage30day, 'Central Region Past 30 Days 7-Day Running Average', size=4)
plot_central_7DAvg(centralsevenDayAverage7day, 'Central Region Past 7 Days 7-Day Running Average', size=4)


def plot_capital_7DAvg(df, title='Capital 7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Frederick7Day", data=df, color='darkgreen', label="Frederick")
    g = sns.lineplot(x="ReportDate", y="Montgomery7Day", data=df, color='limegreen', label="Montgomery")
    g = sns.lineplot(x="ReportDate", y="PG7Day", data=df, color='cyan', label="Prince George's")

    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



capitalcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
capitalsevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
capitalsevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
capitalsevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]
plot_capital_7DAvg(cvd_case_rate_aggregate, 'Capital Region Aggregate 7-Day Running Average', size=4)
plot_capital_7DAvg(capitalsevenDayAverage60day, 'Capital Region Past 60 Days 7-Day Running Average', size=4)
plot_capital_7DAvg(capitalsevenDayAverage30day, 'Capital Region Past 30 Days 7-Day Running Average', size=4)
plot_capital_7DAvg(capitalsevenDayAverage7day, 'Capital Region Past 7 Days 7-Day Running Average', size=4)

def plot_eastern_7DAvg(df, title='Eastern Region 7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Caroline7Day", data=df, color='orange', label="Caroline")
    g = sns.lineplot(x="ReportDate", y="Cecil7Day", data=df, color='crimson', label="Cecil")  
    g = sns.lineplot(x="ReportDate", y="Dorchester7Day", data=df, color='plum', label="Dorchester")
    g = sns.lineplot(x="ReportDate", y="Kent7Day", data=df, color='purple', label="Kent")
    g = sns.lineplot(x="ReportDate", y="QA7Day", data=df, color='khaki', label="Queen Anne's")
    g = sns.lineplot(x="ReportDate", y="StMarys7Day", data=df, color='darkorange', label="St. Mary's")
    g = sns.lineplot(x="ReportDate", y="Talbot7Day", data=df, color='maroon', label="Talbot")
    g = sns.lineplot(x="ReportDate", y="Wicomico7Day", data=df, color='navy', label="Wicomico")
    g = sns.lineplot(x="ReportDate", y="Worcester7Day", data=df, color='teal', label="Worcester")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



easterncvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
easternsevenDayAverage60day = easterncvd_case_rate_aggregate.iloc[-60:]
easternsevenDayAverage30day = easterncvd_case_rate_aggregate.iloc[-30:]
easternsevenDayAverage7day = easterncvd_case_rate_aggregate.iloc[-7:]
plot_eastern_7DAvg(easterncvd_case_rate_aggregate, 'Eastern Shore Region Aggregate 7-Day Running Average', size=4)
plot_eastern_7DAvg(easternsevenDayAverage60day, 'Eastern Shore Region Past 60 Days 7-Day Running Average', size=4)
plot_eastern_7DAvg(easternsevenDayAverage30day, 'Eastern Shore Region Past 30 Days 7-Day Running Average', size=4)
plot_eastern_7DAvg(easternsevenDayAverage7day, 'Eastern Shore Region Past 7 Days 7-Day Running Average', size=4)


def plot_I95_7DAvg(df, title='I-95 Region 7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Baltimore7Day", data=df, color='blue', label="Baltimore County")
    g = sns.lineplot(x="ReportDate", y="BaltCity7Day", data=df, color='salmon', label="Baltimore City")
    g = sns.lineplot(x="ReportDate", y="Cecil7Day", data=df, color='crimson', label="Cecil")  
    g = sns.lineplot(x="ReportDate", y="Harford7Day", data=df, color='blueviolet', label="Harford")
    g = sns.lineplot(x="ReportDate", y="Howard7Day", data=df, color='gray', label="Howard")
    g = sns.lineplot(x="ReportDate", y="PG7Day", data=df, color='cyan', label="Prince George's")
    plt.legend(loc='upper left')



    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



i95cvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
i95sevenDayAverage60day = i95cvd_case_rate_aggregate.iloc[-60:]
i95sevenDayAverage30day = i95cvd_case_rate_aggregate.iloc[-30:]
i95sevenDayAverage7day = i95cvd_case_rate_aggregate.iloc[-7:]
plot_I95_7DAvg(i95cvd_case_rate_aggregate, 'I-95 Region Aggregate 7-Day Running Average', size=4)
plot_I95_7DAvg(i95sevenDayAverage60day, 'I-95 Region Past 60 Days 7-Day Running Average', size=4)
plot_I95_7DAvg(i95sevenDayAverage30day, 'I-95 Region Past 30 Days 7-Day Running Average', size=4)
plot_I95_7DAvg(i95sevenDayAverage7day, 'I-95 Region Past 7 Days 7-Day Running Average', size=4)

def plot_county_7D100kAvg(df, title='Aggregate Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AlleganyDailyCases100k7D", data=df, color='black', label="Allegany")
    g = sns.lineplot(x="ReportDate", y="AA100k7D-2020Census", data=df, color='red', label="Anne Arundel")
    g = sns.lineplot(x="ReportDate", y="Baltimore7D100k", data=df, color='blue', label="Baltimore County")
    g = sns.lineplot(x="ReportDate", y="BaltCity7D100k", data=df, color='salmon', label="Baltimore City")
    g = sns.lineplot(x="ReportDate", y="Calvert7D100k", data=df, color='saddlebrown', label="Calvert")
    g = sns.lineplot(x="ReportDate", y="Caroline7D100k", data=df, color='orange', label="Caroline")
    g = sns.lineplot(x="ReportDate", y="Carroll7D100k", data=df, color='olive', label="Caroll")
    g = sns.lineplot(x="ReportDate", y="Cecil7D100k", data=df, color='crimson', label="Cecil")  
    g = sns.lineplot(x="ReportDate", y="Charles7D100k", data=df, color='dodgerblue', label="Charles")  
    g = sns.lineplot(x="ReportDate", y="Dorchester7D100k", data=df, color='plum', label="Dorchester")
    g = sns.lineplot(x="ReportDate", y="Frederick7D100k", data=df, color='darkgreen', label="Frederick")
    g = sns.lineplot(x="ReportDate", y="Garrett7D100k", data=df, color='hotpink', label="Garrett")
    g = sns.lineplot(x="ReportDate", y="Harford7D100k", data=df, color='blueviolet', label="Harford")
    g = sns.lineplot(x="ReportDate", y="Howard7D100k", data=df, color='gray', label="Howard")
    g = sns.lineplot(x="ReportDate", y="Kent7D100k", data=df, color='purple', label="Kent")
    g = sns.lineplot(x="ReportDate", y="Montgomery7D100k", data=df, color='limegreen', label="Montgomery")
    g = sns.lineplot(x="ReportDate", y="PG7D100k", data=df, color='cyan', label="Prince George's")
    g = sns.lineplot(x="ReportDate", y="QA7D100k", data=df, color='khaki', label="Queen Anne's")
    g = sns.lineplot(x="ReportDate", y="StMarys7D100k", data=df, color='darkorange', label="St. Mary's")
    g = sns.lineplot(x="ReportDate", y="Somerset7D100k", data=df, color='indianred', label="Somerset")
    g = sns.lineplot(x="ReportDate", y="Talbot7D100k", data=df, color='maroon', label="Talbot")
    g = sns.lineplot(x="ReportDate", y="Washington7D100k", data=df, color='steelblue', label="Washington")
    g = sns.lineplot(x="ReportDate", y="Wicomico7D100k", data=df, color='navy', label="Wicomico")
    g = sns.lineplot(x="ReportDate", y="Worcester7D100k", data=df, color='teal', label="Worcester")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



sevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
sevenday100ksevenDayAverage60day = sevenday100kcvd_case_rate_aggregate.iloc[-60:]
sevenday100ksevenDayAverage30day = sevenday100kcvd_case_rate_aggregate.iloc[-30:]
sevenday100ksevenDayAverage7day = sevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_county_7D100kAvg(sevenday100kcvd_case_rate_aggregate, '2020 County Case Rate Aggregate 7-Day Running Average', size=4)
plot_county_7D100kAvg(sevenday100ksevenDayAverage60day, '2020 County Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_county_7D100kAvg(sevenday100ksevenDayAverage30day, '2020 County Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_county_7D100kAvg(sevenday100ksevenDayAverage7day, '2020 County Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_aacounty_7D100kAvg(df, title='Aggregate Anne Arundel County Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AA100k7D-2020Census", data=df, color='red', label="Anne Arundel")
    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



aasevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
aasevenday100ksevenDayAverage60day = aasevenday100kcvd_case_rate_aggregate.iloc[-60:]
aasevenday100ksevenDayAverage30day = aasevenday100kcvd_case_rate_aggregate.iloc[-30:]
aasevenday100ksevenDayAverage7day = aasevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_aacounty_7D100kAvg(aasevenday100kcvd_case_rate_aggregate, 'County Case Rate Aggregate 7-Day Running Average', size=4)
plot_aacounty_7D100kAvg(aasevenday100ksevenDayAverage60day, 'County Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_aacounty_7D100kAvg(aasevenday100ksevenDayAverage30day, 'County Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_aacounty_7D100kAvg(aasevenday100ksevenDayAverage7day, 'County Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_westerncounty_7D100kAvg(df, title='Aggregate Western Region Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AlleganyDailyCases100k7D", data=df, color='black', label="Allegany")
    g = sns.lineplot(x="ReportDate", y="Garrett7D100k", data=df, color='hotpink', label="Garrett")
    g = sns.lineplot(x="ReportDate", y="Washington7D100k", data=df, color='steelblue', label="Washington")
    plt.legend(loc='upper left')

    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()

westernsevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
westernsevenday100ksevenDayAverage60day = westernsevenday100kcvd_case_rate_aggregate.iloc[-60:]
westernsevenday100ksevenDayAverage30day = westernsevenday100kcvd_case_rate_aggregate.iloc[-30:]
westernsevenday100ksevenDayAverage7day = westernsevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_westerncounty_7D100kAvg(westernsevenday100kcvd_case_rate_aggregate, 'Western Region Case Rate Aggregate 7-Day Running Average', size=4)
plot_westerncounty_7D100kAvg(westernsevenday100ksevenDayAverage60day, 'Western Region Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_westerncounty_7D100kAvg(westernsevenday100ksevenDayAverage30day, 'Western Region Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_westerncounty_7D100kAvg(westernsevenday100ksevenDayAverage7day, 'Western Region Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_southerncounty_7D100kAvg(df, title='Aggregate Southern Region Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Calvert7D100k", data=df, color='saddlebrown', label="Calvert")
    g = sns.lineplot(x="ReportDate", y="Charles7D100k", data=df, color='dodgerblue', label="Charles")  
    g = sns.lineplot(x="ReportDate", y="Somerset7D100k", data=df, color='indianred', label="Somerset")


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



southernsevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
southernsevenday100ksevenDayAverage60day = southernsevenday100kcvd_case_rate_aggregate.iloc[-60:]
southernsevenday100ksevenDayAverage30day = southernsevenday100kcvd_case_rate_aggregate.iloc[-30:]
southernsevenday100ksevenDayAverage7day = southernsevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_southerncounty_7D100kAvg(southernsevenday100kcvd_case_rate_aggregate, 'Southern Region Case Rate Aggregate 7-Day Running Average', size=4)
plot_southerncounty_7D100kAvg(southernsevenday100ksevenDayAverage60day, 'Southern Region Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_southerncounty_7D100kAvg(southernsevenday100ksevenDayAverage30day, 'Southern Region Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_southerncounty_7D100kAvg(southernsevenday100ksevenDayAverage7day, 'Southern Region Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_centralcounty_7D100kAvg(df, title='Aggregate Central Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="AA100k7D-2020Census", data=df, color='red', label="Anne Arundel")
    g = sns.lineplot(x="ReportDate", y="Baltimore7D100k", data=df, color='blue', label="Baltimore County")
    g = sns.lineplot(x="ReportDate", y="BaltCity7D100k", data=df, color='salmon', label="Baltimore City")
    g = sns.lineplot(x="ReportDate", y="Carroll7D100k", data=df, color='olive', label="Caroll")
    g = sns.lineplot(x="ReportDate", y="Harford7D100k", data=df, color='blueviolet', label="Harford")
    g = sns.lineplot(x="ReportDate", y="Howard7D100k", data=df, color='gray', label="Howard")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



centralsevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
centralsevenday100ksevenDayAverage60day = centralsevenday100kcvd_case_rate_aggregate.iloc[-60:]
centralsevenday100ksevenDayAverage30day = centralsevenday100kcvd_case_rate_aggregate.iloc[-30:]
centralsevenday100ksevenDayAverage7day = centralsevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_centralcounty_7D100kAvg(centralsevenday100kcvd_case_rate_aggregate, 'Central Region Case Rate Aggregate 7-Day Running Average', size=4)
plot_centralcounty_7D100kAvg(centralsevenday100ksevenDayAverage60day, 'Central Region Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_centralcounty_7D100kAvg(centralsevenday100ksevenDayAverage30day, 'Central Region Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_centralcounty_7D100kAvg(centralsevenday100ksevenDayAverage7day, 'Central Region Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_capitalcounty_7D100kAvg(df, title='Aggregate Capital Region Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Frederick7D100k", data=df, color='darkgreen', label="Frederick")
    g = sns.lineplot(x="ReportDate", y="Montgomery7D100k", data=df, color='limegreen', label="Montgomery")
    g = sns.lineplot(x="ReportDate", y="PG7D100k", data=df, color='cyan', label="Prince George's")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



capitalsevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
capitalsevenday100ksevenDayAverage60day = capitalsevenday100kcvd_case_rate_aggregate.iloc[-60:]
capitalsevenday100ksevenDayAverage30day = capitalsevenday100kcvd_case_rate_aggregate.iloc[-30:]
capitalsevenday100ksevenDayAverage7day = capitalsevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_capitalcounty_7D100kAvg(capitalsevenday100kcvd_case_rate_aggregate, 'Capital Region Case Rate Aggregate 7-Day Running Average', size=4)
plot_capitalcounty_7D100kAvg(capitalsevenday100ksevenDayAverage60day, 'Capital Region Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_capitalcounty_7D100kAvg(capitalsevenday100ksevenDayAverage30day, 'Capital Region Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_capitalcounty_7D100kAvg(capitalsevenday100ksevenDayAverage7day, 'Capital Region Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_easterncounty_7D100kAvg(df, title='Eastern Shore Aggregate Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))

    g = sns.lineplot(x="ReportDate", y="Caroline7D100k", data=df, color='orange', label="Caroline")
    g = sns.lineplot(x="ReportDate", y="Cecil7D100k", data=df, color='crimson', label="Cecil")  
    g = sns.lineplot(x="ReportDate", y="Dorchester7D100k", data=df, color='plum', label="Dorchester")
    g = sns.lineplot(x="ReportDate", y="Kent7D100k", data=df, color='purple', label="Kent")
    g = sns.lineplot(x="ReportDate", y="QA7D100k", data=df, color='khaki', label="Queen Anne's")
    g = sns.lineplot(x="ReportDate", y="StMarys7D100k", data=df, color='darkorange', label="St. Mary's")
    g = sns.lineplot(x="ReportDate", y="Talbot7D100k", data=df, color='maroon', label="Talbot")
    g = sns.lineplot(x="ReportDate", y="Wicomico7D100k", data=df, color='navy', label="Wicomico")
    g = sns.lineplot(x="ReportDate", y="Worcester7D100k", data=df, color='teal', label="Worcester")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



easternsevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
easternsevenday100ksevenDayAverage60day = easternsevenday100kcvd_case_rate_aggregate.iloc[-60:]
easternsevenday100ksevenDayAverage30day = easternsevenday100kcvd_case_rate_aggregate.iloc[-30:]
easternsevenday100ksevenDayAverage7day = easternsevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_easterncounty_7D100kAvg(easternsevenday100kcvd_case_rate_aggregate, 'Eastern Shore Region Case Rate Aggregate 7-Day Running Average', size=4)
plot_easterncounty_7D100kAvg(easternsevenday100ksevenDayAverage60day, 'Eastern Shore Region Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_easterncounty_7D100kAvg(easternsevenday100ksevenDayAverage30day, 'Eastern Shore Region Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_easterncounty_7D100kAvg(easternsevenday100ksevenDayAverage7day, 'Eastern Shore Region Case Rate  Past 7 Days 7-Day Running Average', size=4)

def plot_I95county_7D100kAvg(df, title='Aggregate Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Baltimore7D100k", data=df, color='blue', label="Baltimore County")
    g = sns.lineplot(x="ReportDate", y="BaltCity7D100k", data=df, color='salmon', label="Baltimore City")
    g = sns.lineplot(x="ReportDate", y="Cecil7D100k", data=df, color='crimson', label="Cecil")  
    g = sns.lineplot(x="ReportDate", y="Harford7D100k", data=df, color='blueviolet', label="Harford")
    g = sns.lineplot(x="ReportDate", y="Howard7D100k", data=df, color='gray', label="Howard")
    g = sns.lineplot(x="ReportDate", y="PG7D100k", data=df, color='cyan', label="Prince George's")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



i95sevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
i95sevenday100ksevenDayAverage60day = i95sevenday100kcvd_case_rate_aggregate.iloc[-60:]
i95sevenday100ksevenDayAverage30day = i95sevenday100kcvd_case_rate_aggregate.iloc[-30:]
i95sevenday100ksevenDayAverage7day = i95sevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_I95county_7D100kAvg(i95sevenday100kcvd_case_rate_aggregate, 'I-95 Region Case Rate Aggregate 7-Day Running Average', size=4)
plot_I95county_7D100kAvg(i95sevenday100ksevenDayAverage60day, 'I-95 Region Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_I95county_7D100kAvg(i95sevenday100ksevenDayAverage30day, 'I-95 Region Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_I95county_7D100kAvg(i95sevenday100ksevenDayAverage7day, 'I-95 Region Case Rate  Past 7 Days 7-Day Running Average', size=4)


###REGIONAL####
def plot_regional_7D100kAvg(df, title='Regional Zones Aggregate Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ReportDate", y="Western7D100k", data=df, color='blue', label="Western Region")
    g = sns.lineplot(x="ReportDate", y="Southern7D100k", data=df, color='salmon', label="Southern Region")
    g = sns.lineplot(x="ReportDate", y="Central7D100k", data=df, color='crimson', label="Central Region")  
    g = sns.lineplot(x="ReportDate", y="Capital7D100k", data=df, color='blueviolet', label="Capital Region")
    g = sns.lineplot(x="ReportDate", y="Eastern7D100k", data=df, color='gray', label="Eastern Shore Region")
    g = sns.lineplot(x="ReportDate", y="I957D100k", data=df, color='cyan', label="I-95 Corridor")
    plt.legend(loc='upper left')


    plt.xlabel('Date')
    plt.ylabel('Cases per 100k')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()



regionalsevenday100kcvd_case_rate_aggregate = county.groupby(['ReportDate']).sum().reset_index()
regionalsevenday100ksevenDayAverage60day = regionalsevenday100kcvd_case_rate_aggregate.iloc[-60:]
regionalsevenday100ksevenDayAverage30day = regionalsevenday100kcvd_case_rate_aggregate.iloc[-30:]
regionalsevenday100ksevenDayAverage7day = regionalsevenday100kcvd_case_rate_aggregate.iloc[-7:]
plot_regional_7D100kAvg(regionalsevenday100kcvd_case_rate_aggregate, 'Regional Aggregate 7-Day Running Average', size=4)
plot_regional_7D100kAvg(regionalsevenday100ksevenDayAverage60day, 'Regional Case Rate  Past 60 Days 7-Day Running Average', size=4)
plot_regional_7D100kAvg(regionalsevenday100ksevenDayAverage30day, 'Regional Case Rate  Past 30 Days 7-Day Running Average', size=4)
plot_regional_7D100kAvg(regionalsevenday100ksevenDayAverage7day, 'Regional Case Rate  Past 7 Days 7-Day Running Average', size=4)
