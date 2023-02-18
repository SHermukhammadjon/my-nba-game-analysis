import re
from action import get_actions, get_names
from separate import consil, separate_team


# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()

def analyse_nba_game(data):
    actions = get_actions(data.split('\n'))
    names = get_names(data.split('\n'))
    respons = separate_team(names, data)

    return respons


respons = analyse_nba_game(data)


# print(respons)


consil(respons)