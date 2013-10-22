#!/usr/bin/env python

"""
Load csv files as SQLite tables.
"""

import csv
import os
import sqlite3

db_path = '../db'

try:
    os.remove(os.path.join(db_path, 'nba_stats.db'))
except OSError as e:
    print "OS error({0}): {1}".format(e.errno, e.strerror)
    pass

conn = sqlite3.connect(os.path.join(db_path, 'nba_stats.db'))
cur = conn.cursor()

## Load team_season table ##

cur.execute("""CREATE TABLE team_season
(team TEXT,year INTEGER,leag TEXT,o_fgm INTEGER,o_fga INTEGER,o_ftm INTEGER,
o_fta INTEGER,o_oreb INTEGER,o_dreb INTEGER,o_reb INTEGER,o_asts INTEGER,o_pf INTEGER,
o_stl INTEGER,o_to INTEGER,o_blk INTEGER,o_3pm INTEGER,o_3pa INTEGER,o_pts INTEGER,d_fgm INTEGER,
d_fga INTEGER,d_ftm INTEGER,d_fta INTEGER,d_oreb INTEGER,d_dreb INTEGER,d_reb INTEGER,d_asts INTEGER,
d_pf INTEGER,d_stl INTEGER,d_to INTEGER,d_blk INTEGER,d_3pm INTEGER,d_3pa INTEGER,d_pts INTEGER,pace REAL,won INTEGER,lost INTEGER)""")

csv_dir = '../data_upto2009'
reader = csv.reader(open(os.path.join(csv_dir, 'team_season.csv')))
fileds = reader.next()
row_counter = 0
for row in reader:
    to_db = [unicode(elem, 'utf8') for elem in row]
    cur.execute("INSERT INTO team_season (team,year,leag,o_fgm,o_fga,o_ftm,o_fta,o_oreb,o_dreb,o_reb,o_asts,o_pf,o_stl,o_to,o_blk,o_3pm,o_3pa,o_pts,d_fgm,d_fga,d_ftm,d_fta,d_oreb,d_dreb,d_reb,d_asts,d_pf,d_stl,d_to,d_blk,d_3pm,d_3pa,d_pts,pace,won,lost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    row_counter += 1

print '%d records have been loaded into team_season table.' % row_counter

## End of loading team_season table ##

## Load nba_champs table ##

cur.execute("""CREATE TABLE nba_champs (year INTEGER,champion TEXT)""")
reader = csv.reader(open(os.path.join(csv_dir, 'nba_champs.csv')))
fileds = reader.next()
row_counter = 0
for index, row in enumerate(reader):
    to_db = [unicode(elem, 'utf8') for elem in row]
    cur.execute("INSERT INTO nba_champs VALUES (?, ?);", to_db )
    row_counter += 1

print '%d records have been loaded into nba_champs table.' % row_counter

## End of loading nba_champs table ##

## Load player_playoffs table ##

cur.execute("""CREATE TABLE player_playoffs (ilkid TEXT,year INTEGER,
firstname TEXT,lastname TEXT,team TEXT,leag TEXT,
gp INTEGER,minutes INTEGER,pts INTEGER,dreb INTEGER,oreb INTEGER,reb INTEGER,
asts INTEGER,stl INTEGER,blk INTEGER,turnover INTEGER,pf INTEGER,fga INTEGER,
fgm INTEGER,fta INTEGER,ftm INTEGER,tpa INTEGER,tpm INTEGER)""")
reader = csv.reader(open(os.path.join(csv_dir, 'player_playoffs.csv')))
fileds = reader.next()
row_counter = 0
for row in reader:
    # There is data inconsistency in the player_playoffs.csv.
    # They use SAN to represent San Antonio Spurs at year 2005 and 2008.
    # while using SAS for other years. Action pushed here to
    # clean it up.
    if row[4] == 'SAN':
        row[4] = 'SAS'
    
    # Unfortunately washington wizards was coded as 'Was' at year 2006.
    if row[4] == 'Was':
        row[4] = 'WAS'

    # Unfortunately New Orleans Hornets was coded as 'NOR' at year 2008.
    if row[4] == 'NOR':
        row[4] = 'NOH'

    to_db = [unicode(elem, 'utf8') for elem in row]
    cur.execute("""INSERT INTO player_playoffs VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""" , to_db )
    row_counter += 1

print '%d records have been loaded into player_playoffs table.' % row_counter

## End of Loading player_playoffs table ##

cur.execute("""CREATE TABLE players (ilkid TEXT,firstname TEXT,lastname TEXT,
position TEXT,firstseason INTEGER,lastseason INTEGER,h_feet INTEGER,
h_inches INTEGER,weight INTEGER,college TEXT,birthdate TEXT)""")
reader = csv.reader(open(os.path.join(csv_dir, 'players.csv')))
fileds = reader.next()
row_counter = 0
for index, row in enumerate(reader):
    to_db = [unicode(elem, 'utf8') for elem in row]
    #print row_counter
    #print to_db
    cur.execute("INSERT INTO players VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?);", to_db )
    row_counter += 1

print '%d records have been loaded into players table.' % row_counter

## End of Loading players.csv ##

## Loading player_regular_season table ##

cur.execute("""CREATE TABLE player_regular_season (ilkid TEXT,year INTEGER,firstname TEXT,lastname TEXT,
team TEXT,leag TEXT,gp INTEGER,minutes INTEGER,pts INTEGER,oreb INTEGER,dreb INTEGER,reb INTEGER,
asts INTEGER,stl INTEGER,blk INTEGER,turnover INTEGER,pf INTEGER,fga INTEGER,fgm INTEGER,
fta INTEGER,ftm INTEGER,tpa INTEGER,tpm INTEGER)""")
reader = csv.reader(open(os.path.join(csv_dir, 'player_regular_season.csv')))
fileds = reader.next()
row_counter = 0
for index, row in enumerate(reader):
    to_db = [unicode(elem, 'utf8') for elem in row]
    #print row_counter
    #print to_db
    cur.execute("INSERT INTO player_regular_season VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?);", to_db )
    row_counter += 1

print '%d records have been loaded into player_regular_season table.' % row_counter

## End of Loading players_regular_season ##

## Loading player_allstar table ##

cur.execute("""CREATE TABLE player_allstar (ilkid TEXT,year INTEGER,firstname TEXT,lastname TEXT,
conference TEXT,leag TEXT,gp INTEGER,minutes INTEGER,pts INTEGER,oreb INTEGER,dreb INTEGER,reb INTEGER,
asts INTEGER,stl INTEGER,blk INTEGER,turnover INTEGER,pf INTEGER,fga INTEGER,fgm INTEGER,
fta INTEGER,ftm INTEGER,tpa INTEGER,tpm INTEGER)""")
reader = csv.reader(open(os.path.join(csv_dir, 'player_allstar.csv')))
fileds = reader.next()
row_counter = 0
for index, row in enumerate(reader):
    to_db = [unicode(elem, 'utf8') for elem in row]
    cur.execute("INSERT INTO player_allstar VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?);", to_db )
    row_counter += 1

print '%d records have been loaded into player_allstar table.' % row_counter

## End of Loading players_regular_season ##

conn.commit()

