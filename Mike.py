# !/usr/bin/env python
__author__ = "Michael Brown"
__license__ = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd


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

CountiesPop = CountyPopulation[
    (CountyPopulation.Category == "Total") & (CountyPopulation.Year == 2020)]

AlleghanyCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Allegany County")].iat[0]
AnneArundelCountyPopulation = CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Anne Arundel County")].iat[0]
BaltimoreCityPopulation =     CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Baltimore City")].iat[0]
BaltimoreCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Baltimore County")].iat[0]
CalvertCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Calvert County")].iat[0]
CarolineCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Caroline County")].iat[0]
CarollCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Carroll County")].iat[0]
CecilCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Cecil County")].iat[0]
CharlesCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Charles County")].iat[0]
DorchestserCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Dorchester Co")].iat[0]
FredrickCountyPopulation =   CountiesPop["Total"][(CountiesPop.Category == "Total") & (CountiesPop.Jurisdiction == "Frederick County")].iat[0]
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