#!/bin/sh

cd code

echo "Start normalizing source dataset......\n"
python normalize.py
echo "End normalizing source dataset.\n"

echo "Start converting csv files to sqlite database......\n"
python csv2sqlite.py
echo "End converting csv files to sqlite database. Database is now available under db directory.\n"

echo "Start extracting data from sqlite database......\n"
python sqlite2csv_team_season.py
echo "End extracting data from sqlite database and target file team_season_1980_2009.csv has been generated.\n"

echo "Start generating graphs......\n"
Rfiles=$(find *.R)
for file in $Rfiles
do
    Rscript $file
done
echo "Done generating graphs. Graphs now available under graph directory.\n"
