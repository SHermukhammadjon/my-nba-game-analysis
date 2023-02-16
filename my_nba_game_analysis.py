import re
import nba

# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()

def analyse_nba_game(data):
    respons = {"home_team": {"name": None, "players_data": {}}, "away_team": {"name": None, "players_data": {}}}
    nba.actions(data.split('\n'))
    return respons





def get_names(data):
    data = data.split("\n")
    playes_name = []
    for action in data:
            n = re.compile(r'([\S]\. [\S]*[^)])').search(action)
            if n: 
                playes_name.append(action[n.span()[0] : n.span()[1]])
    return playes_name




names = get_names(data)

print(f"LEN >> {len(names)}")
for name in names:
    print(name)