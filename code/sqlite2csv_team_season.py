#!/usr/bin/env python

"""
Convert result of SQL queries into csv file for python
to process.
"""

import csv
import os
import sqlite3
import sys

db_path = '../db'
con = sqlite3.connect(os.path.join(db_path, 'nba_stats.db'))

# sqlite3.Row provides both index-based and case-insensitive
# name-based access to columns with almost no memory overhead.
con.row_factory = sqlite3.Row
cur = con.cursor()

## Select all teams that made into playoffs from 1980 to 2009

sql = """
SELECT DISTINCT year, team FROM player_playoffs
WHERE year >= 1980
"""
poffs = cur.execute(sql)
playoffs = {}
for row in poffs:
    year = row['year']
    if not playoffs.has_key(year):
        playoffs[year] = []
        playoffs[year].append(row['team'])
    else:    
        playoffs[year].append(row['team'])

print 'Done fetching all playoff teams from 1980 to 2009.'

# Since table player_playoffs does not have data for 2009~2010 season,
# I need to hardcode data for that season.
playoffs[2009] = [u'ATL', u'BOS', u'CHI', u'DAL', u'LAL', u'MIA', u'ORL', u'SAS',
                  u'MIL', u'CLE', u'CHR', u'OKC', u'PHO', u'UTA', u'DEN', u'POR']

## Get championship from 1980 to 2009

champs = {}
for row in cur.execute('SELECT year, champion FROM nba_champs'):
    champs[row['year']] = row['champion']

print 'Done fetching all championship teams from 1980 to 2009.'

## Get number of allstar of each team by year.

allstar = {}
sql = """
SELECT ts.team, count(prs.firstname) as cnt
FROM team_season ts, player_regular_season prs
WHERE ts.leag = 'N' and ts.year = ? and prs.year = ts.year
and ts.team = prs.team
and prs.firstname in
(SELECT firstname FROM player_allstar pa
WHERE pa.year = prs.year and leag = 'N'
and upper(prs.ilkid) = upper(pa.ilkid))
GROUP BY ts.team
"""
for year in range(1980, 2010):
    param = (year,)
    res = cur.execute(sql, param)
    allstar[year] = {}
    for row in res:
        allstar[year][row['team']] = row['cnt']

print 'Done fetching number of allstar of each team by year from 1980 to 2009.'

## Calculate the average age per team weighted by minutes played.
avgages = {}
for year in range(1980, 2010):
    avgages[year] = {}
    sql = """
SELECT distinct team FROM player_regular_season
WHERE leag='N' and team != 'TOT' and year = ?
"""
    param = (year,)
    res = cur.execute(sql, param)
    teams = []
    for row in res:
        teams.append(row['team'])
        
    for team in teams:
        sql = """
SELECT sum(prs.minutes) as total
FROM player_regular_season prs, players p
WHERE prs.year=? and prs.leag='N' and prs.team=?
and prs.firstname = p.firstname
and lower(prs.ilkid) = lower(p.ilkid)
"""
        param = (year, team,)
        res = cur.execute(sql, param)
        total = 0
        for row in res:
            total = row['total']

        sql = """
SELECT prs.team, p.firstname, p.lastname, p.birthdate, prs.minutes
FROM player_regular_season prs, players p
WHERE prs.year=? and prs.leag='N'
and prs.firstname = p.firstname and prs.team = ?
and lower(prs.ilkid) = lower(p.ilkid)
order by prs.team
"""
        res = cur.execute(sql, param)

        avg = 0.0
        for row in res:
            birth = int(row['birthdate'].split('-')[0])
            age = year - birth
            avg += float(age)*float(row['minutes'])/total

        avgages[year][team] = avg
        #print year, team, total, avg

print 'Done calculating the average age per team weighted by minutes played.'

#print avgages[2008]
    
sql = """
SELECT team, year, o_asts, d_asts, o_fgm, o_fga, o_to,
o_ftm, o_fta, o_3pm, o_3pa, won, lost
FROM team_season WHERE leag='N' and year >= 1980 order by year
"""
teams = cur.execute(sql)
rows = []
for row in teams:

    new_row = []
    new_row.append(row['team']) # team
    new_row.append(row['year']) # year
    oast2dast = float(row['o_asts'])/row['d_asts']
    new_row.append(oast2dast) # assists / assists made by opponents
    new_row.append(float(row['o_fgm'])/row['o_fga']) # field goal percentage
    new_row.append(float(row['o_ftm'])/row['o_fta']) # free throw percentage
    new_row.append(float(row['o_3pm'])/row['o_3pa']) # three point percentage
    #new_row.append(float(row['o_asts'])/row['o_to']) # assists / turnovers
    new_row.append(float(row['won'])/(row['won']+row['lost'])) # winning ratio

    if allstar[row['year']].has_key(row['team']):
        new_row.append(allstar[row['year']][row['team']]) # number of allstar
    else:
        new_row.append(0) # number of allstar

    new_row.append(avgages[row['year']][row['team']]) # average team age

    if row['team'] == champs[row['year']]:
        new_row.append('Champion') # a NBA Champion
        new_row.append('Y') # a NBA Champion
    elif row['team'] in playoffs[row['year']]:
        new_row.append('Playoff Team') # a Playoff team other than champion
        new_row.append('N') # not a NBA Champion
    else:
        new_row.append('Non-Playoff Team') # Not a playoff team
        new_row.append('N') # not a NBA Champion

    rows.append(new_row)


writer = csv.writer(open('team_season_1980-2009.csv', 'w'))
metadata = ['team','year','oast_dast','fgp','ftp','tpp','win_ratio','num_allstar','avg_age','result', 'is_champ']
writer.writerow(metadata)
writer.writerows(rows)

print 'Done generating the target csv file: team_season_1980-2009.csv.'

