from django.shortcuts import render
from better.models import NbaBetter
from better.apirequests import getRankOfTeams

# Create your views here.
def home(request):
    actual_western_teams, actual_eastern_teams = getRankOfTeams()
    betters = NbaBetter.objects.all()
    betters_scores_west = [better.west_scores(actual_western_teams=actual_western_teams)[-1] for better in betters]
    betters_scores_east = [better.east_scores(actual_eastern_teams=actual_eastern_teams)[-1] for better in betters]
    betters_scores_total = [west_score + east_score for west_score, east_score in zip(betters_scores_west, betters_scores_east)]
    return render(request, "website/home.html",
                  {"betters": betters, "betters_scores_west": betters_scores_west,
                   "betters_scores_east": betters_scores_east, "betters_scores_total": betters_scores_total})


