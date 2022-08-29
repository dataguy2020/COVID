#!/bin/bash

#Original File
cd /home/`whoami`/script
today=`date +%m%d%Y`
dir="data/$today"
if [[ ! -e $dir ]]; then
    mkdir $dir
fi

git pull
#python3 scripts/StateData.py
#python3 scripts/USA.py
#python3 scripts/county.py
#python3 scripts/vaccines.py
#python3 scripts/covidbyage.py
#python3 scripts/deaths.py

#Added on 12/23/2021
#python3 scripts/state-hospitaliations.py

#Added as backup on 12/2021
#python3 scripts/state-case-backup.py

#Added on 1/12/22
#python3 scripts/aacounty.py

#Added 1/17/22
#python3 scripts/county2020.py

#Added 8/2/2022
#python3 scripts/upgradeCounty.py

#Original File
#mv *.png data/$today
#mv *.csv data/$today

dir1="data/County/$today"
if [[ ! -e $dir ]]; then
    mkdir $dir1
fi
python3 scripts/County/cases.py
python3 scripts/County/hospital.py
echo "Moving PNG files to data dir"
mv *.png $dir1
echo "Moving CSV files to data dir"
mv *.csv $dir1

git add *
git commit -m "`date +%m%d%Y` updates"
git push COVID master
