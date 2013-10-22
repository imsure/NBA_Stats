# Apply linear regression model to predicate 2012 season regular season
# winning percentage.
logreg = function() {
  teams.t = read.csv('team_season_1980-2009.csv', header=TRUE)
  tt.logm = glm(is_champ~fgp+num_allstar+avg_age+oast_dast, data=teams.t, family=binomial)
  print("Summary of logistic regression model:")
  print(summary(tt.logm))
  teams.p = read.csv('team_season_2012.csv', header=TRUE)
  p = predict(tt.logm, type="response", newdata=teams.p)
  #print("Probability of winning a championship for teams in 2012 season:")
  #print(p)

  png('../graphs/logreg.png', width=1000, height=600)
  layout(matrix(1:4,2,2))
  plot(tt.logm)
  dev.off()

  png('../graphs/champ_prob.png', width=1000, height=600)
  radius = sqrt(p/pi)
  symbols(p, circles=radius, inches=1.2, fg='white', bg='skyblue',
          ylim=c(0,0.7), xlim=c(1,30), xaxt='n', ylab='Probability of Winning a Championship', xlab='Team',
	  cex.lab=1.5)
  #axis(side=1, at=seq(1, 30, by=1), labels=as.character(teams.p$team))
  text(c(1:30), p, labels=teams.p$team, font=2)
  title('2012~2013 Season NBA Championship Prediction', cex.main=2)
  dev.off()
}

#pdf("tpp.pdf", height=8, width=15)
logreg()
