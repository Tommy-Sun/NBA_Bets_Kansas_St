import requests
import pandas as pd
from timer.models import Timer
from .models import Teams, fetchStandingData

timer = Timer()

headers = {
        'x-rapidapi-key': "65aa355da0msh7a94a499e17ce8ep1b0482jsn9441b7300bee",
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

teams = Teams(name="Current Teams Data")

def getRankOfTeams():
    inputdata1 = dict()
    inputdata1["Western Teams"] = list()
    inputdata1["Team ID"] = list()
    inputdata1["Western Rank"] = list()
    inputdata1["Win Percentage"] = list()

    inputdata2 = dict()
    inputdata2["Eastern Teams"] = list()
    inputdata2["Team ID"] = list()
    inputdata2["Eastern Rank"] = list()
    inputdata2["Win Percentage"] = list()

    response = fetchStandingData()
    teams = Teams.objects.first()
    if (None != response):
        standings_data = response["api"]["standings"]
        if False:
            teams.set_data()
            teams.save()
        for count, team_data in enumerate(standings_data):
            team_id = team_data["teamId"]
            team_name = teams.get_data()[team_id]
            if team_data["conference"]["name"] == "west":
                inputdata1["Western Teams"].append(team_name)
                inputdata1["Team ID"].append(team_id)
                inputdata1["Western Rank"].append(int(team_data["conference"]["rank"]))
                inputdata1["Win Percentage"].append(float(team_data["winPercentage"]))
            if team_data["conference"]["name"] == "east":
                inputdata2["Eastern Teams"].append(team_name)
                inputdata2["Team ID"].append(team_id)
                inputdata2["Eastern Rank"].append(int(team_data["conference"]["rank"]))
                inputdata2['Win Percentage'].append(float(team_data["winPercentage"]))

        df1_western_ranks = pd.DataFrame(inputdata1)
        df2_eastern_ranks = pd.DataFrame(inputdata2)
        df1_western_ranks = df1_western_ranks.sort_values('Western Rank')
        df2_eastern_ranks = df2_eastern_ranks.sort_values('Eastern Rank')
        df1_western_ranks = df1_western_ranks.set_index('Western Rank')
        df2_eastern_ranks = df2_eastern_ranks.set_index('Eastern Rank')

        return df1_western_ranks, df2_eastern_ranks

#timer.has_already_updated_for_the_day() == False