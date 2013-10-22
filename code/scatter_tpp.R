scatter_tpp = function() {
teams <- read.csv('team_season_1980-2009.csv', header=TRUE)

teams1 = subset(teams, result=='Non-Playoff Team')
plot(teams1$year, teams1$tpp, pch=21, bg='skyblue', col='skyblue', ylim=c(0.1, 0.45),
     xlab='Year', ylab='Three-point percentage', cex.lab=1.5, cex.axis=1.5)
abline(h=(seq(0.1,0.45,0.02)), col="tan", lty="dotted", lwd=2)
#rect(par("usr")[1], par("usr")[3], par("usr")[2], par("usr")[4], col="tan")

teams2 = subset(teams, result=='Playoff Team')
points(teams2$year, teams2$tpp, pch=21, col='orange', fg='white', bg='orange')

teams3 = subset(teams, result=='Champion')
points(teams3$year, teams3$tpp, pch=21, col='tomato', fg='white', bg='violet', cex=4.5)
text(teams3$year, teams3$tpp, labels=teams3$team, cex=.8, font=2)

# Get a list of league average age by year.
ms = tapply(teams$tpp, teams$year, mean)
# Add points showing moving average
points(c(1980:2009), ms, pch=21, col='red', fg='white', bg='red', cex=2)

title('Regular Season Three-point Percentage', cex.main=2)
legend('topleft', legend=c('Champion', 'Playoff team', 'Non-playoff team', 'League average'),
        col=c('violet','orange','lightblue', 'red'), pch=19, cex=1.2)
}

png('../graphs/scatter_tpp.png', width=800, height=500)
#pdf("tpp.pdf", height=8, width=15)
scatter_tpp()
dev.off()
