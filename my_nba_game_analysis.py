import re
from action import get_actions, get_names
from separate import consil, separate_team





def loader_action(nba_game, action):
    # consil(nba_game)
    for key, team in nba_game.items():
        # print(key)
        # print(team)
        for player_data in team['players_data']:
            print(player_data['player_name'], end = "")
            name = player_data['player_name']

            for act in action['3P']:
                found = re.search(name, act)
                if found:
                    player_data["3P"] = player_data["3P"] + 1
                    # print(act)

            print(f" make 3pt : {player_data['3P']}")


    print("___________")
    for n in action['3P']:
        print(n)




# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()

def analyse_nba_game(data):
    actions = get_actions(data.split('\n'))
    names = get_names(data.split('\n'))
    respons = separate_team(names, data)
    loader_action(respons, actions)

    return respons


respons = analyse_nba_game(data)


# print(respons)


# consil(respons)