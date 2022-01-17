# !/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

CountyPopulation = pd.read_csv("https://opendata.arcgis.com/datasets/0573e90adab5434f97b082590c503bc1_0.csv")

# ===================================================================
# County Populations from the State of the Maryland
# Source - https://opendata.maryland.gov/api/views/5zc8-s5s9/rows.csv 2020 Total
# ===================================================================
AnneArundelPopulationMike = 573231
AnneArundelPopulationCounty = 579630
AnneArundelPopulation2019Census = 579234
AnneArundelPopulation2020Census = 588261


# ===================================================================
# Example of Calcuation for Case Rate
# ===================================================================
# CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
# CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()


CVD = pd.read_csv('https://opendata.arcgis.com/datasets/0573e90adab5434f97b082590c503bc1_0.csv')
CVD['ndate'] = CVD['DATE'] + '00'

# Convert string value of date to datetime format
CVD['ndate'] = [dt.datetime.strptime(x, '%Y/%m/%d %H:%M:%S%z')
                for x in CVD['ndate']]

CVD['AADailyCases'] = CVD['Anne_Arundel'].diff()
CVD['AA7Day'] = CVD['AADailyCases'].rolling(window=7).mean()

#Mikes
CVD['AADaily100K'] = (CVD['AADailyCases'] / AnneArundelPopulationMike) * 100000
CVD['AA100k7D-MikeInitial'] = CVD['AADaily100K'].rolling(window=7).mean()

#County 2019 Estimates
CVD['AADaily100k1'] = (CVD['AADailyCases'] / AnneArundelPopulationCounty) * 100000
CVD['AA100k7D-County_2019'] = CVD['AADaily100k1'].rolling(window=7).mean()

#2019 Census
CVD['AADaily100k2'] = (CVD['AADailyCases'] / AnneArundelPopulation2019Census) * 100000
CVD['AA100k7D-2019Census'] = CVD['AADaily100k2'].rolling(window=7).mean()

#2020 Census
CVD['AADaily100k3'] = (CVD['AADailyCases'] / AnneArundelPopulation2020Census) * 100000
CVD['AA100k7D-2020Census'] = CVD['AADaily100k3'].rolling(window=7).mean()

print(CVD.tail())
print(CVD.dtypes)
CVD.to_csv('AnneArundelMDCountyData.csv')


# =================================================================================
# 7-Day Running Average
# =================================================================================
def plot_state_7davg(df, title='7-Day Case Count', size=1):
    f, ax = plt.subplots(1, 1, figsize=(4 * size, 2 * size))
    g = sns.lineplot(x="ndate", y="AA7Day", data=df, color='blue', label="Anne Arundel")

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
    g = sns.lineplot(x="ndate", y="AA100k7D-MikeInitial", data=df, color='blue', label="AA County Case Rate - Mike Initial")
    g = sns.lineplot(x="ndate", y="AA100k7D-County_2019", data=df, color='green', label="AA County Case Rate - County")
    g = sns.lineplot(x="ndate", y="AA100k7D-2019Census", data=df, color='black', label="AA County Case Rate - 2019 Census")
    g = sns.lineplot(x="ndate", y="AA100k7D-2020Census", data=df, color='red', label="AA County Case Rate - 2020 Census")



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

plot_state_case_rate(cvd60d, 'Anne Arundel Case Rate Previous 60 Days', size=4)
plot_state_case_rate(cvd45d, 'Anne Arundel Case Rate Previous 45 Days', size=4)
plot_state_case_rate(cvd30d, 'Anne Arundel Case Rate Previous 30 Days', size=4)
plot_state_case_rate(cvd7d, 'Anne Arundel Case Rate Previous 7 Days', size=4)
