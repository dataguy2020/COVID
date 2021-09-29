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

AACountyPop = CountyPopulation[
    (CountyPopulation.Category == "Total") & (CountyPopulation.Year == 2020)]

AnneArundelCountyPopulation = AACountyPop["Total"][(AACountyPop.Category == "Total") & (AACountyPop.Jurisdiction == "Anne Arundel County")].iat[0]
print("County Population selected is: ", AnneArundelCountyPopulation)
