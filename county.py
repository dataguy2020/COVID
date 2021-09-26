# !/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns


# ==============================
# Below are the different regions of Maryland
# ==============================
# Western Region - Alleghany, Garrett, Washington
# Southern Region - Calvert, Charles, Somerset
# Central Region -  Baltimore County, Baltimore City, Anne Arundel, Harford, Caroll, Howard
# Capial Region - Montgomery, PG, Fredrick
# Eastern Shor Region - Cecil, Kent, Queen Anne's, Talbot, Caroline, Dorchester, Wicomico, St. Mary's, Worchester
# I-95 Corridor - Baltimore County, Baltimore City, Cecil, Harford, Howard, PG


CountyPopulation = pd.read_csv("https://opendata.maryland.gov/api/views/5zc8-s5s9/rows.csv")

AACountyPop = CountyPopulation[
    (CountyPopulation.Category == "Total") & (CountyPopulation.Year == 2020)]
print(AACountyPop.tail())
print(AACountyPop.dtypes)
AACountyPop.to_csv('CountyPopulation.csv')

# ===================================================================
# County Populations from the State of the Maryland
# Source - https://opendata.maryland.gov/api/views/5zc8-s5s9/rows.csv 2020 Total
# ===================================================================
AnneArundelPopulation = 573231
BaltimoreCountyPopulation = 847000
BaltimoreCityPopulation = 616292
HowardCountyPopulation = 336921
CalvertCountyPopulation = 94606
PGCountyPopulation = 916142
HarfordCountyPopulation = 255441
MontgomeryCountyPopulation = 1050688
alleghanyPopulation = 76403
WashingtonCountyPopulation = 156797
GarrettPopulation = 30293
SomersetPopulation = 26750
CharlesPopulation = 167042
carollPopulation = 169199
fredrickPopulation = 260780
CecilPopulation = 104601
kentpopulation = 20896
qapopulation = 50734
talbotpopulation = 38856
carolinePopulation = 34049
dorchesterPopulation = 34302
wicomicopopulation = 106202
stmaryPopulation = 120154
worchesterPopulation = 53101

# ===================================================================
# Example of Calcuation for Case Rate
# ===================================================================
# CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
# CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()


CVD = pd.read_csv('https://opendata.arcgis.com/datasets/0573e90adab5434f97b082590c503bc1_0.csv')
CVD['AACountyPop'] = AACountyPop['Total']
CVD['ndate'] = CVD['DATE'] + '00'

# Convert string value of date to datetime format
CVD['ndate'] = [dt.datetime.strptime(x, '%Y/%m/%d %H:%M:%S%z')
                for x in CVD['ndate']]

CVD['AADailyCases'] = CVD['Anne_Arundel'].diff()
CVD['AA7Day'] = CVD['AADailyCases'].rolling(window=7).mean()
CVD['AADaily100K'] = (CVD['AADailyCases'] / AnneArundelPopulation) * 100000
CVD['AA100k7D'] = CVD['AADaily100K'].rolling(window=7).mean()

CVD['BaltCountyDailyCases'] = CVD['Baltimore'].diff()
CVD['BaltimoreCounty7Day'] = CVD['BaltCountyDailyCases'].rolling(window=7).mean()
CVD['BaltimoreCountyDaily100K'] = (CVD['BaltCountyDailyCases'] / BaltimoreCountyPopulation) * 100000
CVD['BaltimoreCounty100k7D'] = CVD['BaltimoreCountyDaily100K'].rolling(window=7).mean()

CVD['BaltimoreCityDC'] = CVD['Baltimore_City'].diff()
CVD['BaltCity7Day'] = CVD['BaltimoreCityDC'].rolling(window=7).mean()
CVD['BaltCityDaily100k'] = (CVD['BaltimoreCityDC'] / BaltimoreCityPopulation) * 100000
CVD['BaltimoreCity100k7D'] = CVD['BaltCityDaily100k'].rolling(window=7).mean()

CVD['HowardDC'] = CVD['Howard'].diff()
CVD['Howard7Day'] = CVD['HowardDC'].rolling(window=7).mean()
CVD['HowardCountyDaily100K'] = (CVD['HowardDC'] / HowardCountyPopulation) * 100000
CVD['HowardCounty100k7D'] = CVD['HowardCountyDaily100K'].rolling(window=7).mean()

CVD['CalvertDC'] = CVD['Calvert'].diff()
CVD['Calvert7Day'] = CVD['CalvertDC'].rolling(window=7).mean()
CVD['CalvertDaily100k'] = (CVD['CalvertDC'] / CalvertCountyPopulation) * 100000
CVD['Calvert100k7D'] = CVD['CalvertDaily100k'].rolling(window=7).mean()

CVD['PGDC'] = CVD['Prince_Georges'].diff()
CVD['PG7Day'] = CVD['PGDC'].rolling(window=7).mean()
CVD['PGDaily100k'] = (CVD['PGDC'] / PGCountyPopulation) * 100000
CVD['PG100k7D'] = CVD['PGDaily100k'].rolling(window=7).mean()

CVD['HarfordDC'] = CVD['Harford'].diff()
CVD['Hardford7Day'] = CVD['HarfordDC'].rolling(window=7).mean()
CVD['Harford100kDaily'] = (CVD['HarfordDC'] / HarfordCountyPopulation) * 100000
CVD['Hardford100k7D'] = CVD['Harford100kDaily'].rolling(window=7).mean()

CVD['MontgomeryDC'] = CVD['Montgomery'].diff()
CVD['Montgomery7Day'] = CVD['MontgomeryDC'].rolling(window=7).mean()
CVD['Montgomery100kDaily'] = (CVD['MontgomeryDC'] / MontgomeryCountyPopulation) * 100000
CVD['Montgomery100k7D'] = CVD['Montgomery100kDaily'].rolling(window=7).mean()

print(CVD.tail())
print(CVD.dtypes)
CVD.to_csv('MDCountyData.csv')


# =================================================================================
# 7-Day Running Average
# =================================================================================
def plot_state_7davg(df, title='7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ndate", y="AA7Day", data=df, color='blue', label="Anne Arundel")
    g = sns.lineplot(x="ndate", y="BaltimoreCounty7Day", data=df, color='green', label="Baltimore County")
    g = sns.lineplot(x="ndate", y="BaltCity7Day", data=df, color='black', label="Baltimore City")
    g = sns.lineplot(x="ndate", y="Howard7Day", data=df, color='red', label="Howard County")
    g = sns.lineplot(x="ndate", y="Calvert7Day", data=df, color='cyan', label="Calvert County")
    g = sns.lineplot(x="ndate", y="PG7Day", data=df, color='purple', label="Prince Greorge's County")

    plt.xlabel('Date')
    plt.ylabel(' 7-Day Average ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()


cvd_case_rate_aggregate = CVD.groupby(['ndate']).sum().reset_index()
sevenDayAverage60day = cvd_case_rate_aggregate.iloc[-60:]
sevenDayAverage45day = cvd_case_rate_aggregate.iloc[-45:]
sevenDayAverage30day = cvd_case_rate_aggregate.iloc[-30:]
sevenDayAverage7day = cvd_case_rate_aggregate.iloc[-7:]

plot_state_7davg(cvd_case_rate_aggregate, 'Case Count for Counties Aggregate 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage60day, 'Case Count for Counties previous 60 Days 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage45day, 'Case Count for Counties previous 45 Days 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage30day, 'Case Count for Counties previous 30 Days 7-Day Running Average', size=4)
plot_state_7davg(sevenDayAverage7day, 'Case Count for Counties previous 7 Days 7-Day Running Average', size=4)


# =================================================================================
# Aggregate Case Rate
# =================================================================================
def plot_state_case_rate(df, title='County Case Rate', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ndate", y="AA100k7D", data=df, color='blue', label="Anne Arundel County Case Rate")
    g = sns.lineplot(x="ndate", y="BaltimoreCounty100k7D", data=df, color='green', label="Baltimore County Case Rate")
    g = sns.lineplot(x="ndate", y="BaltimoreCity100k7D", data=df, color='black', label="Baltimore City Case Rate")
    g = sns.lineplot(x="ndate", y="HowardCounty100k7D", data=df, color='red', label="Howard County Case Rate")
    g = sns.lineplot(x="ndate", y="Calvert100k7D", data=df, color='cyan', label="Calvert County Case Rate")
    g = sns.lineplot(x="ndate", y="PG100k7D", data=df, color='purple', label="Prince George's County Case Rate")

    plt.xlabel('Date')
    plt.ylabel(' Cases per 100k ')
    plt.xticks(rotation=90)
    plt.title(f' {title} ')
    ax.grid(color='black', linestyle='dotted', linewidth=0.75)
    plt.savefig(f'{title}.png')
    plt.show()


cvd_case_rate_aggregate = CVD.groupby(['ndate']).sum().reset_index()
cvd60d = cvd_case_rate_aggregate.iloc[-60:]
cvd30d = cvd_case_rate_aggregate.iloc[-30:]
cvd45d = cvd_case_rate_aggregate.iloc[-45:]
cvd7d = cvd_case_rate_aggregate.iloc[-7:]

plot_state_case_rate(cvd_case_rate_aggregate, 'Aggregate Counties Case Rate', size=4)

plot_state_case_rate(cvd60d, 'Counties Case Rate Previous 60 Days', size=4)
plot_state_case_rate(cvd45d, 'Counties Case Rate Previous 30 Days', size=4)
plot_state_case_rate(cvd30d, 'Counties Case Rate Previous 30 Days', size=4)
plot_state_case_rate(cvd7d, 'Counties Case Rate Previous 7 Days', size=4)