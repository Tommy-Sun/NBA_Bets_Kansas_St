# NBA_Bets_Kansas_St
A website that allows Betters to compare their NBA Standings with the actual rankings and determine their score. Made with Django. 

Ever wanted to make a bet on what the top standings in the NBA would be by the end of the season? This Django website allows you to do just that. 
You can create a new NBA Better; add a name, and predictions for the top 10 teams in the West and top 10 teams in the East. 
Then a score is automatically calculated based off the differences between the predicted standings and the actual standings. Each prediction is compared to the predicted team's actual standing and a score is given based off the difference. For example, if you predicted the Los Angeles Lakers to be number 1 in the West, but they are actually number 5, you would get a score of 4 for that prediction (|5-1|). The higher the score, the worse your prediction turned out to be. 

A full detail view of scores is available by clicking on the Better's name on the Home page.
