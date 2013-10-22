# Comparison of 4 KPIs among teams in 2012 season.
team_cmp= function() {
  teams = read.csv('team_season_2012.csv', header=TRUE)
  layout(matrix(1:4, 2, 2))

  radius = sqrt(teams$avg_age/pi)
  symbols(jitter(c(1:30)), teams$avg_age, circles=radius, inches=.2, fg='white', bg='skyblue',
          ylim=c(22, 33), xlim=c(1,30), xaxt='n', xlab='Team', ylab='Average team age', cex.lab=1.5)
  text(c(1:30), teams$avg_age, labels=teams$team, font=2)
  title('Comparison of average age between teams', cex.main=1.5)

  radius = sqrt(teams$fgp/pi)
  symbols(teams$fgp, circles=radius, inches=.2, fg='white', bg='skyblue',
          ylim=c(0.42, 0.52), xlim=c(1,30), xaxt='n', xlab='Team', ylab='Field goal percentage', cex.lab=1.5)
  text(c(1:30), teams$fgp, labels=teams$team, font=2)
  title('Comparison of field goal percentage between teams', cex.main=1.5)

  radius = sqrt(teams$num_allstar/pi)
  symbols(jitter(c(1:30)), teams$num_allstar, circles=radius, inches=.25, fg='white', bg='skyblue',
          ylim=c(0, 4), xlim=c(1,30), xaxt='n', xlab='Team', ylab='Number of all star', cex.lab=1.5)
  text(c(1:30), teams$num_allstar, labels=teams$team, font=2)
  title('Comparison of number of all star between teams', cex.main=1.5)

  radius = sqrt(teams$oast_dast/pi)
  symbols(teams$oast_dast, circles=radius, inches=.2, fg='white', bg='skyblue',
          ylim=c(0.7, 1.3), xlim=c(1,30), xaxt='n', xlab='Team', ylab='assists / assists by opponents', cex.lab=1.5)
  text(c(1:30), teams$oast_dast, labels=teams$team, font=2)
  title('Comparison of assists/(assists by opponents) between teams', cex.main=1.5)
}

png("../graphs/team_cmp.png", height=800, width=1200)
team_cmp()
dev.off()
