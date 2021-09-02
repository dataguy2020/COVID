#!/bin/bash

cd /home/michael/script
today=`date +%m%d%Y`
mkdir data/$today
python3 StateData.py
python3 USA.py
mv *.png data/$today
mv *.csv data/$today
git add *
git commit -m "`date +%m%d%Y` updates"

