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