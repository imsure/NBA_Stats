# Apply linear regression model to predicate 2012 season regular season
# winning percentage.
lnreg = function() {
  teams.t = read.csv('team_season_1980-2009.csv', header=TRUE)
  tt.lm = lm(win_ratio ~ oast_dast+fgp+tpp+num_allstar+avg_age, data=teams.t)
  print("Summary of linear regression model:")
  print(summary(tt.lm))
  png('../graphs/lnreg.png', width=1050, height=600)
  layout(matrix(1:4,2,2))
  plot(tt.lm)
  dev.off()

  teams.p = read.csv('team_season_2012.csv', header=TRUE)
  p = predict(tt.lm, newdata=teams.p)
  teams.p$predication = p
  teams.p$diff = teams.p$win_ratio - teams.p$predication
  print(sum(abs(teams.p$diff)/30))
  r = rbind(teams.p$win_ratio, teams.p$predication)
  png('../graphs/winpred.png', width=1050, height=600)
  barplot(r, beside=T, names.arg=teams.p$team, cex.names=.8, col=c('skyblue','green'),
          ylab='Winning Percentage', cex.lab=1.5)
  legend('topleft', legend=c('Real Outcome', 'Prediction'),
         col=c('skyblue','green'), pch=15, cex=1.1)
  title('2012~2013 Regular Season Winning Percentage Prediction', cex.main=2)
  dev.off()
}

#pdf("win.pdf", height=8, width=15)
lnreg()
