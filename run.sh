#!/bin/bash

cd /home/michael/script
today=`date +%m%d%Y`
dir="data/$today"
if [[ ! -e $dir ]]; then
    mkdir $dir
fi

python3 StateData.py
python3 USA.py
mv *.png data/$today
mv *.csv data/$today
git add *
git commit -m "`date +%m%d%Y` updates"

