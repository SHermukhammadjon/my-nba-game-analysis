import re
from action import get_actions, get_names
from separate import consil, separate_team

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
    nba_game = count(nba_game, action, '3PA', '3PA')
    nba_game = count(nba_game, action, 'FG', '2P')
    nba_game = count(nba_game, action, 'FGA', '2PA')
    nba_game = count(nba_game, action, 'FT', 'FT')
    nba_game = count(nba_game, action, 'FTA', 'FTA')
    nba_game = count(nba_game, action, 'ORB', 'ORB')
    nba_game = count(nba_game, action, 'DRB', 'DRB')
    nba_game = count(nba_game, action, 'AST', 'AST')
    nba_game = count(nba_game, action, 'STL', 'STL')
    nba_game = count(nba_game, action, 'BLK', 'BLK')
    nba_game = count(nba_game, action, 'TOV', 'TOV')
    nba_game = count(nba_game, action, 'PF', 'PF')
    


    # print_nba_game_stats(nba_game)
    return nba_game

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