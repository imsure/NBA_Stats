-- Select all the teams that made into playoffs
-- from 1980 to 2008. 2009 is not given in player_playoffs table.

SELECT ts.year, ts.team
FROM team_season ts
WHERE ts.year >= 1980 and ts.year < 2009 and ts.team in
(SELECT team FROM player_playoffs pp
WHERE pp.year = ts.year);


-- Select number of teams by made into playoffs from 1980 ~ 2008

SELECT ts.year, count(ts.team)
FROM team_season ts
WHERE ts.year >= 1980 and ts.year < 2009 and ts.team in
(SELECT team FROM player_playoffs pp
WHERE pp.year = ts.year)
group by ts.year;

-- Number of team each season

select year, count(team) from team_season where year >= 1980 group by year;


-- Find number the records grouped by year
-- where San Antonio Spurs is encoded as 'SAN' instead of 'SAS'.

select year, count(team) from player_playoffs pp where pp.team='SAN' group by year;


-- Find all teams made into playoffs in year 2006.

SELECT distinct team FROM player_playoffs where year=2008 order by team;

-- Find teams made into playoffs in year 2006,
-- maybe partial due to naming differences.
-- By comparing with the results of above query, we'd be able to
-- identify the difference.

SELECT team
FROM team_season ts
WHERE year = 2008 and team in
(SELECT team FROM player_playoffs pp
WHERE year = 2008) order by team;

-- Compute sum of total assists by year.

SELECT year, sum(o_asts), sum(d_asts)
FROM team_season
WHERE year >= 1980 GROUP BY year;

-- Select number of allstars of each teams by years.

SELECT distinct ts.year, ts.team
FROM team_season ts, player_regular_season prs
WHERE ts.leag = 'N' and ts.year >= 1980 and ts.year = prs.year
and ts.team = prs.team order by ts.year;

SELECT distinct ts.year, ts.team, count(prs.firstname)
FROM team_season ts, player_regular_season prs
WHERE ts.leag = 'N' and ts.year = 2009 and ts.year = prs.year
and ts.team = prs.team GROUP BY ts.team;

SELECT ts.year, ts.team, count(prs.firstname)
FROM team_season ts, player_regular_season prs
WHERE ts.leag = 'N' and ts.year = 2009 and ts.year = prs.year
and ts.team = prs.team
and prs.firstname in
(SELECT firstname FROM player_allstar pa
WHERE pa.year = prs.year and leag = 'N' and upper(prs.ilkid) = upper(pa.ilkid))
GROUP BY ts.team;

SELECT ts.year, ts.team, prs.firstname
FROM team_season ts, player_regular_season prs
WHERE ts.leag = 'N' and ts.year = 2009 and ts.year = prs.year
and ts.team = prs.team
and prs.firstname in
(SELECT firstname FROM player_allstar pa
WHERE pa.year = prs.year and leag = 'N' and upper(prs.ilkid) = upper(pa.ilkid));


select firstname, lastname from player_allstar
where year=2009 and leag = 'N' order by firstname;

select count(firstname) from player_allstar
where year=2009 and leag = 'N';

-- Select average age of players per team by year.

SELECT distinct team FROM player_regular_season
WHERE leag='N' and team != 'TOT' and year = 1980;

SELECT prs.team, p.firstname, p.lastname, p.birthdate, prs.minutes
FROM player_regular_season prs, players p
WHERE prs.year=2008 and prs.leag='N'
and prs.firstname = p.firstname and prs.team != 'TOT'
and lower(prs.ilkid) = lower(p.ilkid)
order by prs.team;

SELECT prs.team, sum(prs.minutes)
FROM player_regular_season prs, players p
WHERE prs.year=2008 and prs.leag='N'
and prs.firstname = p.firstname and prs.team != 'TOT'
and lower(prs.ilkid) = lower(p.ilkid)
group by prs.team order by prs.team;

SELECT prs.team, p.firstname, p.lastname, p.birthdate, prs.minutes
FROM player_regular_season prs, players p
WHERE prs.year=2008 and prs.leag='N'
and prs.firstname = p.firstname and prs.team != 'TOT' and prs.team='LAL'
and lower(prs.ilkid) = lower(p.ilkid)
order by prs.team;

SELECT prs.team, count(p.lastname)
FROM player_regular_season prs, players p
WHERE prs.year=2009 and prs.leag='N' and prs.team != 'TOT'
and prs.firstname = p.firstname and prs.lastname = p.lastname
and lower(prs.ilkid) = lower(p.ilkid)
group by prs.team
order by prs.team;

SELECT team, year, o_asts, d_asts, o_fgm, o_fga,
o_ftm, o_fta, o_reb, o_to, o_3pm, o_3pa, won, lost
FROM team_season WHERE leag='N' and year = 2009;
