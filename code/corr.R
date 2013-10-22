
teams.t = read.csv('team_season_1980-2009.csv', header=TRUE)
tt.lm = lm(win_ratio ~ oast_dast+fgp+tpp+num_allstar+avg_age, data=teams.t)
  #layout(matrix(1:4,2,2))
  #plot(tt.lm)

png('../graphs/corr.png', width=1600, height=1200)
pairs(teams.t[,3:9], panel=panel.smooth, cex.labels=2)
#title('Correlation Matrix', cex.main=2)
#pdf("win.pdf", height=8, width=15)
dev.off()
