import re
import nba

# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()


def analyse_nba_game(data):
    respons = {"home_team": {"name": None, "players_data": {}}, "away_team": {"name": None, "players_data": {}}}
    # nba.actions(data.split('\n'))
    names = nba.get_names(data.split('\n'))

    # print(len(names))
    # for n in names:
    #     print(n)

    return names


names = analyse_nba_game(data)
print(names)
print(len(names))


def separate_team(names, nba_data):

    respons = {"home_team": {"name": None, "players_data": {}}, "away_team": {"name": None, "players_data": {}}}
    nba_data = nba_data.split("\n")
    

    return respons

separate_team(names, data)
