import pandas as pd

def west_scores(western_ranks, actual_western_teams):
    df_better = pd.Series(western_ranks)
    print("Western Better ranks/teams: ")
    print(df_better)
    df_actual = actual_western_teams["Western Teams"]
    list_of_scores = []
    for rank_better, team_better in df_better.items():
        for rank_actual, team_actual in df_actual.items():
            if team_better == team_actual:
                list_of_scores.append(abs((1+rank_better) - rank_actual))
    total = sum(list_of_scores)
    list_of_scores.append(total)
    print("\n")
    print("the number of elements in the west list: " + str(len(list_of_scores)))
    print(list_of_scores)
    print("^These are the WEST scores")
    return list_of_scores

def east_scores(eastern_ranks, actual_eastern_teams):
    df_better = pd.Series(eastern_ranks)
    df_actual = actual_eastern_teams["Eastern Teams"]
    list_of_scores = []
    for rank_better, team_better in df_better.items():
        for rank_actual, team_actual in df_actual.items():
            if team_better == team_actual:
                list_of_scores.append(abs((1+rank_better) - rank_actual))
    total = sum(list_of_scores)
    list_of_scores.append(total)
    print("\n")
    print("the number of elements in the east list: " + str(len(list_of_scores)))
    print(list_of_scores)
    print("^These are the EAST scores")
    return list_of_scores