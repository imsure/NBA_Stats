scatter_avgage = function() {
teams <- read.csv('team_season_1980-2009.csv', header=TRUE)

teams1 = subset(teams, result=='Non-Playoff Team')
plot(teams1$year, teams1$avg_age, pch=21, bg='skyblue', col='skyblue',
     xlim=c(1980, 2009), ylim=c(22, 32),
     xlab='Year', ylab='Average Team Age', cex.lab=1.5, cex.axis=1.5)
abline(h=(seq(22,33,1)), col="tan", lty="dotted", lwd=2)
#rect(par("usr")[1], par("usr")[3], par("usr")[2], par("usr")[4], col="tan")

teams2 = subset(teams, result=='Playoff Team')
points(teams2$year, teams2$avg_age, pch=21, col='orange', fg='white', bg='orange')

teams3 = subset(teams, result=='Champion')
points(teams3$year, teams3$avg_age, pch=21, col='tomato', fg='white', bg='violet', cex=4.5)
text(teams3$year, teams3$avg_age, labels=teams3$team, cex=.8, font=2)

# Get a list of league average age by year.
ms = tapply(teams$avg_age, teams$year, mean)
# Add points showing moving average
points(c(1980:2009), ms, pch=21, col='red', fg='white', bg='red', cex=2)

title('Average Team Age (Weighted by Minutes Played)', cex.main=2)
legend('topleft', legend=c('Champion', 'Playoff team', 'Non-playoff team', 'League average'),
        col=c('violet','orange','lightblue', 'red'), pch=19, cex=1.2)
}

png('../graphs/scatter_avgage.png', width=800, height=500)
#pdf("avg_age.pdf", height=8, width=15)
scatter_avgage()
dev.off()
