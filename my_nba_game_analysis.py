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

def 



def separate_team(names, nba_data):

    nba_data = split(nba_data)
    respons = {"home_team": {"name": nba_data[0][4], "players_data": {}}, "away_team": {"name": nba_data[0][3], "players_data": {}}}

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

    print(f"LEN >>> {len(players[nba_data[0][4]]) + len(players[nba_data[0][3]])}")

    # print("founded names: ")
    foundes = []
    for n in players[nba_data[0][4]]:
        foundes.append(n)
    for n in players[nba_data[0][3]]:
        foundes.append(n)

    # print("\nnames: ")
    for found in foundes:
        for name in names:
            if name == found:
                names.remove(name)
    print(f"names : {name}")
    print(names)
    print(players)

    return respons

request = separate_team(names, data)

# print(request)