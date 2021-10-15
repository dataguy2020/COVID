#!/bin/bash

cd /home/`whoami`/script
today=`date +%m%d%Y`
dir="data/$today"
if [[ ! -e $dir ]]; then
    mkdir $dir
fi

git pull
python3 StateData.py
python3 USA.py
python3 county.py
python3 vaccines.py
python3 covidbyage.py
python3 deaths.py
mv *.png data/$today
mv *.csv data/$today
git add *
git commit -m "`date +%m%d%Y` updates"
git push COVID master
