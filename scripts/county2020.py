# !/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
import seaborn as sns

#CountyPopulation = pd.read_csv("https://opendata.arcgis.com/datasets/0573e90adab5434f97b082590c503bc1_0.csv")

# ===================================================================
# County Populations from the State of the Maryland
# Source - https://opendata.maryland.gov/api/views/5zc8-s5s9/rows.csv 2020 Total
# ===================================================================
AnneArundelPopulation2020Census = 588261


# ===================================================================
# Example of Calcuation for Case Rate
# ===================================================================
# CVD['Daily100k'] = (CVD['DailyCases'] / statePopulation) * 100000
# CVD['100k7D'] = CVD['Daily100k'].rolling(window=7).mean()


CVD = pd.read_csv('https://opendata.maryland.gov/api/views/mgd3-qk8t/rows.csv?accessType=DOWNLOAD')
#CVD['ndate'] = CVD['DATE'] + '00'

# Convert string value of date to datetime format
#CVD['ndate'] = [dt.datetime.strptime(x, '%Y/%m/%d %H:%M:%S%z')
#                for x in CVD['ndate']]

CVD['AADailyCases'] = CVD['ANNE'].diff()
CVD['AA7Day'] = CVD['AADailyCases'].rolling(window=7).mean()

#2020 Census
CVD['AADaily100k3'] = (CVD['AADailyCases'] / AnneArundelPopulation2020Census) * 100000
CVD['AA100k7D-2020Census'] = CVD['AADaily100k3'].rolling(window=7).mean()

#print(CVD.tail())
#print(CVD.dtypes)
#CVD.to_csv('MDCountyData.csv')

#Creating new data frame 
county = pd.DataFrame()
county['ReportDate'] = CVD['ReportDate']
county['Allegany'] = CVD['ALLE']
county['AnneArundel'] = CVD['ANNE']
county['Baltimore'] = CVD['BALT']
county['BaltimoreCity'] = CVD['BCITY']
county['Calvert'] = CVD['CALV']
county['Caroline'] = CVD['CARO']
county['Carroll'] = CVD['CARR']
county['Cecil'] = CVD['CECI']
county['Charles'] = CVD['CHAR']
county['Dorchester'] = CVD['DORC']
county['Fredrick'] = CVD['FRED']
county['Garrett'] = CVD['GARR']
county['Harford'] = CVD['HARF']
county['Howard'] = CVD['HOWA']
county['Kent'] = CVD['KENT']
county['Montgomery'] = CVD['MONT']
county['PrinceGeorges'] = CVD['PRIN']
county['QueenAnnes'] = CVD['QUEE']
county['Somerset'] = CVD['SOME']
county['StMarys'] = CVD['STMA']
county['Talbot'] = CVD['TALB']
county['Washington'] = CVD['WASH']
county['Wicomico'] = CVD['WICO']
county['Worcester'] = CVD['WORC']

#Debugging
print(county.dtypes)
