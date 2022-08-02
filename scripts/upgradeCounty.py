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

#getting the date portion of the string
county['ReportDate'] = county.ReportDate.str.slice(0,10)

#converting string to date format
county['ReportDate'] = [dt.datetime.strptime(x, '%m/%d/%Y')
                for x in county['ReportDate']]

#adding new column for data date vs reported date - data date is 1 day prior to report date
county['DataDate'] = county['ReportDate'] - timedelta(days=1)


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

#converting Report Date to string
county['ReportDate'] = county['ReportDate'].astype('str')

#getting the date portion of the string
county['ReportDate'] = county.ReportDate.str.slice(0,10)

#converting string to date format
county['ReportDate'] = [dt.datetime.strptime(x, '%m/%d/%Y')
                for x in county['ReportDate']]

#adding new column for data date vs reported date - data date is 1 day prior to report date
county['DataDate'] = county['ReportDate'] - timedelta(days=1)

print (county.dtypes)
print(county.tail())

county.to_csv('CountyTest.csv')
