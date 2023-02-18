import re
from action import get_actions, get_names
from separate import consil, separate_team

def print_nba_game_stats(team_dict):
    for home_or_away, team in team_dict.items():
        print(f">>> \n{home_or_away}\n")
        # print(team)
        n = 0
        for team_name, players_data in team.items():
            n += 1
            # print("n: ", n)
            if n != 1:
                for player in players_data:
                    print(player)
            else:
                print(team_name)
                print(team[team_name])







def count(nba_game, action, n_key, a_key):
    for home_or_away, team in nba_game.items():
        # print(home_or_away)
        # print(team)
        stop = len(team['players_data'])
        for player in range(stop):
            # print(team['players_data'][player]['player_name'])
            # team['players_data'][player][nbkey]
            for series in action[a_key]:
                if re.search(team['players_data'][player]['player_name'], series):
                    team['players_data'][player][n_key] = team['players_data'][player][n_key] + 1
    
    return nba_game
    


def loader_action(nba_game, action):
    nba_game = count(nba_game, action, '3P', '3P')
    nba_game = count(nba_game, action, 'FG', '2P')
    nba_game = count(nba_game, action, '3PA', '3PA')


    print_nba_game_stats(nba_game)

    # print("actions: \n")
    # for act in action:
    #     print(act)

    # # consil(nba_game)
    # for key, team in nba_game.items():
    #     # print(key)
    #     # print(team)
    #     for player_data in team['players_data']:
    #         print(player_data['player_name'], end = "")
    #         name = player_data['player_name']

    #         for act in action['3P']:
    #             found = re.search(name, act)
    #             if found:
    #                 player_data["3P"] = player_data["3P"] + 1
    #                 # print(act)

    #         print(f" make 3pt : {player_data['3P']}")


    # print("___________")
    # for n in action['3P']:
    #     print(n)




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