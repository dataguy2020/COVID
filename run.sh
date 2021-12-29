#!/bin/bash

#Original File
cd /home/`whoami`/script
today=`date +%m%d%Y`
dir="data/$today"
if [[ ! -e $dir ]]; then
    mkdir $dir
fi

git pull
python3 scripts/StateData.py
python3 scripts/USA.py
python3 scripts/county.py
python3 scripts/vaccines.py
python3 scripts/covidbyage.py
python3 scripts/deaths.py

#Added on 12/23/2021
python3 scripts/state-hospitaliations.py

#Added as backup on 12/2021
#python3 scripts/state-case-backup.py

/#Original File
mv *.png data/$today
mv *.csv data/$today
git add *
git commit -m "`date +%m%d%Y` updates"
git push COVID master
