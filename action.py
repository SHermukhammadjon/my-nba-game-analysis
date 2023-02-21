import re


def action_catch(match, data):
    respons = []
    for action in data:
        n = re.compile(match).search(action)
        if n: 
            respons.append(action[n.span()[0] : n.span()[1]])
    return respons


def get_actions(data):
    mept3 = action_catch(r'([\S]. [\S]*) makes 3-pt jump shot from', data)   # 3P
    mispt3 = action_catch(r'([\S]. [\S]*) misses 3-pt jump shot from', data) # 3PA

    mept2 = action_catch(r'([\S]. [\S]*) makes 2-pt', data)   # 2P
    mispt2 = action_catch(r'([\S]. [\S]*) misses 2-pt', data) # 2PA

    ft = action_catch(r'([\S]. [\S]*) makes free throw', data)   # FT
    fta = action_catch(r'([\S]. [\S]*) misses free throw', data) # FTA

    orb = action_catch(r'Offensive rebound by ([\S]. [\S]*)', data)    # ORB
    drb =  action_catch(r'Defensive rebound by ([\S]. [\S]*)', data)   # DRB

    ast = action_catch(r'assist by ([\S]. [\S]*[^)])', data) # AST

    stl = action_catch(r'steal by ([\S]. [\S]*[^)])', data) # STL
    blk = action_catch(r'block by ([\S]. [\S]*[^)])', data) # BLK

    tov =  action_catch(r'Turnover by ([\S]. [\S]*)', data) # TOV
    pf = action_catch(r'Personal foul by ([\S]. [\S]*)', data) # PF

    return {'3P' : mept3, '3PA' : mispt3, '2P' : mept2, '2PA' : mispt2, 'FT' : ft, 'FTA' : fta, 'ORB' : orb, 'DRB' : drb, 'AST' : ast, 'STL' : stl, 'BLK' : blk, 'TOV' : tov, 'PF' :pf}


def get_names(data):
    players_name = []
    for action in data:
            n = re.compile(r'([\S]\. [\S]*[^)])').search(action)
            if n: 
                players_name.append(action[n.span()[0] : n.span()[1]].strip())
    return list(dict.fromkeys(players_name))
