import re
from action import get_actions, get_names
from separate import consil, separate_team
from loader import loader_action

def box(word, size):
    box = str(word)
    while len(box) != size:
        if len(box) < size:
            box = box + " "
        elif len(box) > size:
            box = box[0:-2]

    return box


def column(series):
    n=0
    for key in series.keys():
        n+=1
        if n == 1:
            print(box(key, 15), end = "|")
        else:
            print(box(key, 5), end = "|")
    print()

def series(series):
    n = 0
    for key, value in series.items():
        # print(type(value), end = " ")
        n+=1
        if n == 1:
            print(box(value, 15), end = "|")
        else:
            print(box(value, 5), end = "|")
    print()
        

def print_nba_game_stats(team_dict):
    for home_or_away, team in team_dict.items():
        print(f">>> \n{home_or_away}\n")
        n = 0
        for team_name, players_data in team.items():
            n += 1
            if n != 1:
                z = 0
                for player in players_data:
                    z+=1
                    if z == 1:
                        column(player)
                        
                    series(player)
            else:
                print(team_name)
                print(team[team_name])




# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()

def analyse_nba_game(data):
    actions = get_actions(data.split('\n'))
    names = get_names(data.split('\n'))
    respons = separate_team(names, data)
    respons = loader_action(respons, actions)

    return respons


respons = analyse_nba_game(data)
print_nba_game_stats(respons)

# print(respons)


# consil(respons)