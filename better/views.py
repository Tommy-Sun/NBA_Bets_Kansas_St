from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from better.models import NbaBetter
from .apirequests import getRankOfTeams
from .scores import west_scores, east_scores

def detail(request, id):
    actual_western_teams, actual_eastern_teams = getRankOfTeams()
    better = get_object_or_404(NbaBetter, pk=id)
    western_ranks = better.get_western_ranks()
    eastern_ranks = better.get_eastern_ranks()
    western_scores = west_scores(western_ranks=western_ranks, actual_western_teams=actual_western_teams)
    eastern_scores = east_scores(eastern_ranks=eastern_ranks, actual_eastern_teams=actual_eastern_teams)
    actual_western_ranks = actual_western_teams["Western Teams"].to_list()
    actual_eastern_ranks = actual_eastern_teams["Eastern Teams"].to_list()
    total_score = western_scores[-1] + eastern_scores[-1]

    return render(request, "better/detail.html",
                  {
                      'better': better, 'western_ranks': western_ranks, 'eastern_ranks': eastern_ranks,
                      'actual_western_ranks': actual_western_ranks, 'actual_eastern_ranks': actual_eastern_ranks,
                      'western_scores': western_scores, 'eastern_scores': eastern_scores, 'total_score': total_score
                  }
                  )

BettingForm = modelform_factory(NbaBetter, exclude=[])

def new_better(request):
    if request.method == "POST":
        form = BettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("form was not valid i guess.")
            print(form.errors)

    else:
        form = BettingForm()
    return render(request, "better/new_better.html", {"form": form})

def test(request):
    return render(request, 'better/test.html')

