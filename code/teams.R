teams <- read.csv('team_season_1980-2009.csv', header=TRUE)

#boxplot(split(teams$o_asts, teams$year), main='Total Assists by Year', col='green')
#with(teams, plot(year, oast_dast, ylim=c(0.5, 1.5)))
#with(teams, identify(year, oast_dast, label=team))

# red: champion; blue: playoff teams; green: regular
mycolors = c('red', 'blue', 'green')
#with(teams, plot(year, oast_dast, col=mycolors[result], ylim=c(0.6, 1.5)))
png('../graphs/orignal_scatterplot.png', width=850, height=500)
with(teams, plot(year, avg_age, col=mycolors[result], ylim=c(20, 35)))
with(teams, legend('topleft', legend=levels(result), col=mycolors, pch=1))
dev.off()

#circles = c(0.7, 0.1, 0.25)
#radius = sqrt(circles[teams$result] / pi)
#with(teams, symbols(year, avg_age, circles=circles[result]))
#symbols(teams$year, teams$avg_age, circles=radius, inches=0.25, fg='white', bg='red', xlim=c(1980, 2009))

#boxplot(split(teams$fgp, teams$year), main='Regular season field goal percentage', col='green')
#fgp_year = tapply(teams$fgp, teams$year, mean)
#lines(fgp_year, col='red')

# How lockout impact the overall performance.
