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
    
    for home_or_away, team_data in team_dict.items():
        print(f">>> {home_or_away}\n")
        n = 0
        # print(team_data)
        total_pts = 0
        for player in team_data['players_data']:
            n+=1
            if n == 1:
                column(player)
            series(player)
            total_pts += player["PTS"]
        print(f"Tota PTS {total_pts}\n")
            # print(player)
        #     print()
            # n += 1
            # if n != 1:
            #     z = 0
            #     for player in players_data:
            #         z+=1
            #         if z == 1:
            #             column(player)
                        
            #         series(player)
            # else:
            #     print(team_name)
            #     print(team[team_name])



# def is_all_num(word):
#     for n in word:
#         if n == "a"   

def do_it(nba_data, lable):
    lable = lable.split(".")
    equal, key1, do, key2 = lable[0], lable[1], lable[2], lable[3]
    for home_or_away, team_data in nba_data.items():
        for player_index in range(len(team_data['players_data'])):
            if key2.isnumeric():
                if do == "+":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] + int(key2)
                elif do == "-":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] - int(key2)
                elif do == "*":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] * int(key2)
                elif do == "/":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] / int(key2)
                # print(nba_data[home_or_away]['players_data'][player_index])
            else:
                if do == "+":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] + nba_data[home_or_away]['players_data'][player_index][key2]
                elif do == "-":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] - nba_data[home_or_away]['players_data'][player_index][key2]
                elif do == "*":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] * nba_data[home_or_away]['players_data'][player_index][key2]
                elif do == "/":
                    nba_data[home_or_away]['players_data'][player_index][equal] += nba_data[home_or_away]['players_data'][player_index][key1] / nba_data[home_or_away]['players_data'][player_index][key2]
                # print(nba_data[home_or_away]['players_data'][player_index])
    return nba_data
          



# UPLOAD DATA
data = open("nba_game_warriors_thunder_20181016.txt", "r")
data = data.read()

def analyse_nba_game(data):
    actions = get_actions(data.split('\n'))
    names = get_names(data.split('\n'))
    respons = separate_team(names, data)
    respons = loader_action(respons, actions)
    respons = do_it(respons, "PTS.FG.*.2")
    respons = do_it(respons, "PTS.3P.*.3")
    respons = do_it(respons, "PTS.FT.+.0")
    respons = do_it(respons, "TRB.ORB.+.DRB")

    # print_nba_game_stats(respons)


    return respons


respons = analyse_nba_game(data)
print_nba_game_stats(respons)

# print(respons)


# consil(respons)