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
# print(names)
# print(len(names))

def split(csv_data):
    table = []
    for data in csv_data.split("\n"):
        series_list = []
        for series in data.split("|"):
            series_list.append(series)
        table.append(series_list)
    return table

def makes(series, match):
    # match = f"{name} makes 3-pt"
    respons = re.search(match, series[-1])
    if respons:
        return True
    return False

def wher_play(nba_data, names):
    players = {nba_data[0][4] : [], nba_data[0][3] : []}
    for name in names:
        for series in nba_data:
            if makes(series, f"{name} makes 3-pt"):
                players[series[2]].append(name)
                break
            elif makes(series, f"{name} makes 2-pt"):
                players[series[2]].append(name)
                break
            elif makes(series, f"{name} misses 3-pt"):
                players[series[2]].append(name)
                break
            elif makes(series, f"{name} misses 2-pt"):
                players[series[2]].append(name)
                break
            elif makes(series, f"Defensive rebound by {name}"):
                players[series[2]].append(name)
                break
            elif makes(series, f"Offensive rebound by {name}"):
                players[series[2]].append(name)
                break
    return players


def separate_team(names, nba_data):
    nba_data = split(nba_data)
    respons = {"home_team": {"name": nba_data[0][4], "players_data": []}, "away_team": {"name": nba_data[0][3], "players_data": []}}

    players = wher_play(nba_data, names)

    teams = {nba_data[0][4] : [], nba_data[0][3] : []}
    for team, players in players.items():
        print(team)
        n = 0
        for player in players:
            z = {"player_name": player, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
            # print(z)
            teams[team].append(z)
            # n+=1
            # print(f'{n}. {player}')
        
    for key, value in teams.items():
        print(f">>> {key.title()}")
        for n in value:
            print(n)

    # print(f"LEN >>> {len(players[nba_data[0][4]]) + len(players[nba_data[0][3]])}")

    # print(players)

    return respons






request = separate_team(names, data)

# for key, value in request.items():
#     print(f">>> {key.title()}: ")
#     i = 0
#     for key1, value1 in value.items():
#         print(f"{key1.title()}: ")
#         i += 1
#         if i != 1:
#             for n in value1:
#                 print(n)
