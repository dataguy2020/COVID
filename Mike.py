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

# Pulling data from source regarding population throughout Maryland
CountyPopulation = pd.read_csv("https://opendata.maryland.gov/api/views/5zc8-s5s9/rows.csv")

CountiesPop = CountyPopulation[
    (CountyPopulation.Category == "Total") & (CountyPopulation.Year == 2020)]

# Various State Populations
AlleganyCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Allegany County")].iat[0]
AnneArundelCountyPopulation = CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Anne Arundel County")].iat[0]
BaltimoreCityPopulation =     CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Baltimore City")].iat[0]
BaltimoreCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Baltimore County")].iat[0]
CalvertCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Calvert County")].iat[0]
CarolineCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Caroline County")].iat[0]
CarrollCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Carroll County")].iat[0]
CecilCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Cecil County")].iat[0]
CharlesCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Charles County")].iat[0]
DorchestserCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Dorchester Co")].iat[0]
FrederickCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Frederick County")].iat[0]
GarrettCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Garrett County")].iat[0]
HarfordCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Harford County")].iat[0]
HowardCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Howard County")].iat[0]
KentCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Kent County")].iat[0]
MontgomeryCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Montgomery County")].iat[0]
PGCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Prince George's County")].iat[0]
QACountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Queen Anne's County")].iat[0]
SomersetCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Somerset County")].iat[0]
StMaryCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "St. Mary's County")].iat[0]
StatePopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "State of Maryland")].iat[0]
TalbotCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Talbot County")].iat[0]
WashingtonCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Washington County")].iat[0]
WicomicoCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Wicomico County")].iat[0]
WorcesterCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Worcester County")].iat[0]
# Pulling Main COVID Data related to Cases per County
CVD = pd.read_csv('https://opendata.arcgis.com/datasets/0573e90adab5434f97b082590c503bc1_0.csv')
CVD['ndate'] = CVD['DATE'] + '00'

# Convert string value of date to datetime format
CVD['ndate'] = [dt.datetime.strptime(x, '%Y/%m/%d %H:%M:%S%z')
                for x in CVD['ndate']]

# calculating data for various County data pieces
CVD['AADailyCases'] = CVD['Anne_Arundel'].diff()
CVD['AA7Day'] = CVD['AADailyCases'].rolling(window=7).mean()
CVD['AADaily100K'] = (CVD['AADailyCases'] / AnneArundelCountyPopulation) * 100000
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

CVD['AlleganyDC'] = CVD['Allegany'].diff()
CVD['Allegany7Day'] = CVD['AlleganyDC'].rolling(window=7).mean()
CVD['Allegany100kDaily'] = (CVD['AlleganyDC'] / AlleganyCountyPopulation) * 100000
CVD['Allegany100k7D'] = CVD['Allegany100kDaily'].rolling(window=7).mean()

CVD['WashingtonDC'] = CVD['Washington'].diff()
CVD['Washington7Day'] = CVD['WashingtonDC'].rolling(window=7).mean()
CVD['Washington100kDaily'] = (CVD['WashingtonDC'] / WashingtonCountyPopulation) * 100000
CVD['Washington100k7D'] = CVD['Washington100kDaily'].rolling(window=7).mean()

CVD['GarrettDC'] = CVD['Garrett'].diff()
CVD['Garrett7Day'] = CVD['GarrettDC'].rolling(window=7).mean()
CVD['Garrett100kDay'] = (CVD['GarrettDC'] / GarrettCountyPopulation) * 100000
CVD['Garrett100k7D'] = CVD['Garrett100kDay'].rolling(window=7).mean()

CVD['SomersetDC'] = CVD['Somerset'].diff()
CVD['Somerset7Day'] = CVD['SomersetDC'].rolling(window=7).mean()
CVD['Somerset100kDay'] = (CVD['SomersetDC'] / SomersetCountyPopulation) * 100000
CVD['Somerset100k7D'] = CVD['Somerset100kDay'].rolling(window=7).mean()

CVD['CharlesDC'] = CVD['Charles'].diff()
CVD['Charles7Day'] = CVD['CharlesDC'].rolling(window=7).mean()
CVD['Charles100kDay'] = (CVD['CharlesDC'] / CharlesCountyPopulation) * 100000
CVD['Charles100k7D'] = CVD['Charles100kDay'].rolling(window=7).mean()

CVD['CarrollDC'] = CVD['Carroll'].diff()
CVD['Carroll7Day'] = CVD['CarrollDC'].rolling(window=7).mean()
CVD['Carroll100kDay'] = (CVD['CarrollDC'] / CarrollCountyPopulation) * 100000
CVD['Carroll100k7D'] = CVD['Carroll100kDay'].rolling(window=7).mean()

CVD['FrederickDC'] = CVD['Frederick'].diff()
CVD['Frederick7Day'] = CVD['FrederickDC'].rolling(window=7).mean()
CVD['Frederick100kDay'] = (CVD['FrederickDC'] / FrederickCountyPopulation) * 100000
CVD['Frederick100k7Day'] = CVD['Frederick100kDay'].rolling(window=7).mean()

CVD['CecilDC'] = CVD['Cecil'].diff()
CVD['Cecil7Day'] = CVD['CecilDC'].rolling(window=7).mean()
CVD['Cecil100kDay'] = (CVD['CecilDC'] / CecilCountyPopulation) * 100000
CVD['Cecil100k7Day'] = CVD['Cecil100kDay'].rolling(window=7).mean()

CVD['KentDC'] = CVD['Kent'].diff()
CVD['Kent7Day'] = CVD['KentDC'].rolling(window=7).mean()
CVD['Kent100kDay'] = (CVD['KentDC'] / KentCountyPopulation) * 100000
CVD['Kent100k7Day'] = CVD['Kent100kDay'].rolling(window=7).mean()

CVD['QADC'] = CVD['Queen_Annes'].diff()
CVD['QA7Day'] = CVD['QADC'].rolling(window=7).mean()
CVD['QA100kDay'] = (CVD['QADC'] / QACountyPopulation) * 100000
CVD['QA100k7Day'] = CVD['QA100kDay'].rolling(window=7).mean()

CVD['TalbotDC'] = CVD['Talbot'].diff()
CVD['Talbot7Day'] = CVD['Talbot'].rolling(window=7).mean()
CVD['Talbot100kDay'] = (CVD['TalbotDC'] / TalbotCountyPopulation) * 100000
CVD['Talbot100k7Day'] = CVD['Talbot100kDay'].rolling(window=7).mean()

CVD['CarolineDC'] = CVD['Caroline'].diff()
CVD['Caroline7Day'] = CVD['CarolineDC'].rolling(window=7).mean()
CVD['Caroline100kDay'] = (CVD['CarolineDC'] / CarolineCountyPopulation) * 100000
CVD['Caroline100k7Day'] = CVD['Caroline100kDay'].rolling(window=7).mean()

CVD['DorchesterDC'] = CVD['Dorchester'].diff()
CVD['Dorchester7Day'] = CVD['DorchesterDC'].rolling(window=7).mean()
CVD['Dorchester100kDay'] = (CVD['DorchesterDC'] / DorchestserCountyPopulation) * 100000
CVD['Dorchester100k7Day'] = CVD['Dorchester100kDay'].rolling(window=7).mean()

CVD['WicomicoDC'] = CVD['Wicomico'].diff()
CVD['Wicomico7Day'] = CVD['WicomicoDC'].rolling(window=7).mean()
CVD['Wicomico100kDay'] = (CVD['WicomicoDC'] / WicomicoCountyPopulation) * 100000
CVD['Wicomico100k7Day'] = CVD['Wicomico100kDay'].rolling(window=7).mean()

CVD['St_MarysDC'] = CVD['St_Marys'].diff()
CVD['St_Marys7Day'] = CVD['St_MarysDC'].rolling(window=7).mean()
CVD['St_Marys100kDay'] = (CVD['St_MarysDC'] / StMaryCountyPopulation) * 100000
CVD['St_Marys100k7Day'] = CVD['St_Marys100kDay'].rolling(window=7).mean()

CVD['WorcesterDC'] = CVD['Worcester'].diff()
CVD['Worcester7Day'] = CVD['WorcesterDC'].rolling(window=7).mean()
CVD['Worcester100kDay'] = (CVD['WorcesterDC'] / WorcesterCountyPopulation) * 100000
CVD['Worcester100k7Day'] = CVD['Worcester100kDay'].rolling(window=7).mean()


# Graphing Daily Cases
# ====================


# Graphing Case Rate
# ====================
