import re

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
                    if nba_data[home_or_away]['players_data'][player_index][key1] != 0 and nba_data[home_or_away]['players_data'][player_index][key2] != 0:
                        nba_data[home_or_away]['players_data'][player_index][equal] = nba_data[home_or_away]['players_data'][player_index][key1] / nba_data[home_or_away]['players_data'][player_index][key2]
                # print(nba_data[home_or_away]['players_data'][player_index])
    return nba_data
          
def to_fill(respons):
    respons = do_it(respons, "PTS.3P.*.3")
    respons = do_it(respons, "PTS.FG.*.2")
    respons = do_it(respons, "PTS.FT.+.0")

    respons = do_it(respons, "FGA.FG.+.0")
    respons = do_it(respons, "3PA.3P.+.0")
    respons = do_it(respons, "FGA.3PA.+.0")
    respons = do_it(respons, "FG.3P.+.0")

    respons = do_it(respons, "FG%.FG./.FGA")
    respons = do_it(respons, "FTA.FT.+.0")

    respons = do_it(respons, "FT%.FT./.FTA")
    respons = do_it(respons, "TRB.ORB.+.DRB")

    respons = do_it(respons, "3P%.3P./.3PA")
    return respons