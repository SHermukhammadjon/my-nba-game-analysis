import re
import nba

# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()

def action_catch(match, data):
    respons = []
    for action in data:
        # z = r'([\S]. [\S]*) makes 3-pt jump shot from'
        n = re.compile(match).search(action)
        if n: 
            respons.append(action[n.span()[0] : n.span()[1]])
    return respons







def analyse_nba_game(play_by_play_moves):
    data = play_by_play_moves.split("\n")

    respons = {"home_team": {"name": None, "players_data": {}}, "away_team": {"name": None, "players_data": {}}}


    makes_3pt = action_catch(r'([\S]. [\S]*) makes 3-pt jump shot from', data)  
    misses_3pt = action_catch(r'([\S]. [\S]*) misses 3-pt jump shot from', data)
    makes_2pt = action_catch(r'([\S]. [\S]*) makes 2-pt', data)
    makes_free_throw = action_catch(r'([\S]. [\S]*) makes free throw . of .', data)
    misses_free_throw = action_catch(r'([\S]. [\S]*) misses free throw . of .', data)
    offensive_rebounds = action_catch(r'Offensive rebound by ([\S]. [\S]*)', data)
    defensive_rebounds =  action_catch(r'Defensive rebound by ([\S]. [\S]*)', data)
    assists = action_catch(r'assist by ([\S]. [\S]*^\))', data)



    print(len(assists))
    for n in assists:
        print(n)




    return respons

analyse_nba_game(data)

# respons = analyse_nba_game(data)

# for key, value in respons.items():
#     print(f">>>  {key}:\n")
#     for key2, value2 in value.items():
#         print(f"{key2} : {value2}" )