# A wrapper function used to plot boxplot of regular season
# field goal percentage by year and a moving average.
boxplot_year = function(x, y, ylab='', main='') {
  # Boxplot of to observe distribution and moving trend
  # of average team age by year.
  boxplot(split(x, y), main=main, col='green', xlab='Year', ylab=ylab,
  cex.main=2, cex.lab=1.5, cex.axis=1.5)
  # Get a list of league average age by year.
  ms = tapply(x, y, mean)
  # Add a line showing moving average
  lines(ms, col='red', lwd=2, type='o', pch=16)
  # Add points showing moving average
  # points(ms, col='blue')
}

png('../graphs/boxplot_fgp.png', width=800)
teams <- read.csv('team_season_1980-2009.csv', header=TRUE)
boxplot_year(teams$fgp, teams$year, ylab = 'Field goal percentage',
	     main='Boxplot of Regular Season Field Goal Percentage by Year
	     (Red line shows moving average)')
dev.off()
