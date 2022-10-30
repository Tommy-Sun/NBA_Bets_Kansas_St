from typing import List, Any
from django.db import models
import json
import requests
import pandas as pd

NBATeamsWest = (
    ("Utah Jazz", "Utah Jazz"),
    ("Phoenix Suns", "Phoenix Suns"),
    ("LA Clippers", "LA Clippers"),
    ("Los Angeles Lakers", "Los Angeles Lakers"),
    ("Denver Nuggets", "Denver Nuggets"),
    ("Portland Trail Blazers", "Portland Trail Blazers"),
    ("San Antonio Spurs", "San Antonio Spurs"),
    ("Dallas Mavericks", "Dallas Mavericks"),
    ("Memphis Grizzlies", "Memphis Grizzlies"),
    ("Golden State Warriors", "Golden State Warriors"),
    ("Sacramento Kings", "Sacramento Kings"),
    ("New Orleans Pelicans", "New Orleans Pelicans"),
    ("Oklahoma City Thunder", "Oklahoma City Thunder"),
    ("Houston Rockets", "Houston Rockets"),
    ("Minnesota Timberwolves", "Minnesota Timberwolves")
)

NBATeamsEast = (
    ("Philadelphia 76ers", "Philadelphia 76ers"),
    ("Brooklyn Nets", "Brooklyn Nets"),
    ("Milwaukee Bucks", "Milwaukee Bucks"),
    ("New York Knicks", "New York Knicks"),
    ("Charlotte Hornets", "Charlotte Hornets"),
    ("Atlanta Hawks", "Atlanta Hawks"),
    ("Boston Celtics", "Boston Celtics"),
    ("Miami Heat", "Miami Heat"),
    ("Indiana Pacers", "Indiana Pacers"),
    ("Chicago Bulls", "Chicago Bulls"),
    ("Toronto Raptors", "Toronto Raptors"),
    ("Washington Wizards", "Washington Wizards"),
    ("Orlando Magic", "Orlando Magic"),
    ("Cleveland Cavaliers", "Cleveland Cavaliers"),
    ("Detroit Pistons", "Detroit Pistons")
)


class NbaBetter(models.Model):
    name = models.CharField(max_length=30)

    west_rank1 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 1')
    west_rank2 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 2')
    west_rank3 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 3')
    west_rank4 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 4')
    west_rank5 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 5')
    west_rank6 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 6')
    west_rank7 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 7')
    west_rank8 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 8')
    west_rank9 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 9')
    west_rank10 = models.CharField(max_length=40, choices=NBATeamsWest, verbose_name='West Rank 10')

    east_rank1 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 1')
    east_rank2 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 2')
    east_rank3 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 3')
    east_rank4 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 4')
    east_rank5 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 5')
    east_rank6 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 6')
    east_rank7 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 7')
    east_rank8 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 8')
    east_rank9 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 9')
    east_rank10 = models.CharField(max_length=40, choices=NBATeamsEast, verbose_name='East Rank 10')

    def __str__(self):
        return f"{self.name}"

    def get_western_ranks(self):
        return [self.west_rank1, self.west_rank2, self.west_rank3, self.west_rank4, self.west_rank5,
                self.west_rank6, self.west_rank7, self.west_rank8, self.west_rank9, self.west_rank10]

    def get_eastern_ranks(self):
        return [self.east_rank1, self.east_rank2, self.east_rank3, self.east_rank4, self.east_rank5,
                self.east_rank6, self.east_rank7, self.east_rank8, self.east_rank9, self.east_rank10]

    def west_scores(self, actual_western_teams):
        df_better = pd.Series(self.get_western_ranks())
        df_actual = actual_western_teams["Western Teams"]
        list_of_scores = []
        for rank_better, team_better in df_better.items():
            for rank_actual, team_actual in df_actual.items():
                if team_better == team_actual:
                    list_of_scores.append(abs((1 + rank_better) - rank_actual))
        total = sum(list_of_scores)
        list_of_scores.append(total)
        return list_of_scores

    def east_scores(self, actual_eastern_teams):
        df_better = pd.Series(self.get_eastern_ranks())
        df_actual = actual_eastern_teams["Eastern Teams"]
        list_of_scores = []
        for rank_better, team_better in df_better.items():
            for rank_actual, team_actual in df_actual.items():
                if team_better == team_actual:
                    list_of_scores.append(abs((1 + rank_better) - rank_actual))
        total = sum(list_of_scores)
        list_of_scores.append(total)
        return list_of_scores

headers = {
        'x-rapidapi-key': "65aa355da0msh7a94a499e17ce8ep1b0482jsn9441b7300bee",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
}
def fetchTeamNames(teamId):
    url = "https://api-nba-v1.p.rapidapi.com/teams/teamId/" + teamId

    response = requests.request("GET", url, headers=headers)

    if (response.status_code == 200):
        return response.json()["api"]["teams"][0]["fullName"]
    else:
        return None
        print(f"Team name did not get fetched properly. {teamId} is the teamId.")

def fetchStandingData():
    url_teams = "https://api-nba-v1.p.rapidapi.com/standings/standard/2022/"

    response_teams = requests.request("GET", url_teams, headers=headers)

    if (response_teams.status_code == 200):
        return response_teams.json()
    else:
        print("Team did not get fetched properly. Not code 200.")
        return None

class Teams(models.Model):
    name = models.CharField(max_length=25)
    data = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.name}"

    def set_data(self):
        data = json.loads(self.data)

        response = fetchStandingData()
        if (None != response):
            standings_data = response["api"]["standings"]
            for team_data in standings_data:
                if team_data["conference"]["name"] == "west": #to update east teams cache change west to east.
                    data[int(team_data["teamId"])] = fetchTeamNames(teamId=team_data["teamId"])
        print(data)
        self.data = json.dumps(data)
        super().save()

    def get_data(self):
        return json.loads(self.data)

