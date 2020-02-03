# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:29:58 2019

@author: simasurk
"""

class Player:
    
    def __init__(self, name, results):
        self.name = name
        self.last_name = name.split(' ')[1]
        self.results = results
        self.pts = float("{:.1f}".format(sum(list(filter(None, results)))))
        self.SB = 0
        self.rank = ''
    
class Player_Table:
    
    number_of_players = None
    player_column_size = None
    total_pts_column_size = None
    pts_column_size = None
    rank_column_size = None
    width_size = None
    SB_column_size = None
    
    def print_table(players, matches_dict):
        #header
        SB_adjust = Player_Table.SB_column_size if Player_Table.SB_column_size % 2 == 0 else Player_Table.SB_column_size - 1
        string = '#'.rjust(Player_Table.rank_column_size) + '  ' + 'Player'.ljust(Player_Table.player_column_size) + '  '
        for i in range(1, Player_Table.number_of_players + 1):
            string += str(i).rjust(Player_Table.pts_column_size) + ' '
        string += ' ' + 'Pts'.ljust(Player_Table.total_pts_column_size) + '  ' + 'SB'.center(SB_adjust).rstrip() + '\n'
        
        #divider
        string += Player_Table.width_size * '='
            
        #data
        for p in players:
            string += '\n' + p.rank.rjust((Player_Table.rank_column_size)) + '  ' + p.name.ljust(Player_Table.player_column_size + 2)
            for j in players:
                string += matches_dict[p.name+'-'+j.name].rjust(Player_Table.pts_column_size) + ' '
            string += ' ' + str("{0:.1f}".format(p.pts)).rjust(Player_Table.total_pts_column_size)
            string += '  ' + "{0:.2f}".format(p.SB).rjust(Player_Table.SB_column_size)
        
        return string
            
def crosstable(players, results):
    Player_Table.number_of_players = len(players)
    player_dict = dict()
    
    #create players
    list_players = list()
    for i in range(Player_Table.number_of_players):
        p = Player(players[i], results[i])
        list_players.append(p)
        player_dict[p.name] = p
        
    #matches history
    matches_dict = dict()
    for i in range(Player_Table.number_of_players):
        for j in range(Player_Table.number_of_players):
            if None == results[i][j]:
                result = ' '
            elif 0.5 == results[i][j]:
                result = '='
            else:
                result = str(round(results[i][j]))
            matches_dict[players[i]+'-'+players[j]] = result
    
    #calculate SB
    for p in list_players:
        for i in range(Player_Table.number_of_players):
            if p.results[i] == 1:
                p.SB += list_players[i].pts
            elif p.results[i] == 0.5:
                p.SB += list_players[i].pts / 2
                
    #sort players         
    sorted_players = sorted(list_players,key=lambda x: (-x.pts,-x.SB,x.last_name))
       
    #Set ranks
    prev_pts, prev_SB = 0, 0
    rank = 1
    for sp in sorted_players:
         if sp.pts != prev_pts or sp.SB != prev_SB:
             sp.rank = str(rank)
         rank += 1 
         prev_pts, prev_SB = sp.pts, sp.SB
    
    #Column Sizes
    Player_Table.player_column_size = len(max(players, key=len))
    Player_Table.total_pts_column_size = len(str(max([x.pts for x in list_players])))
    Player_Table.pts_column_size = len(str(Player_Table.number_of_players))
    Player_Table.rank_column_size = len(str(Player_Table.number_of_players))
    Player_Table.SB_column_size = len(str(max([round(x.SB) for x in sorted_players]))) + 3
        
    Player_Table.width_size = Player_Table.rank_column_size + Player_Table.player_column_size +\
                              (Player_Table.pts_column_size + 1) * Player_Table.number_of_players +\
                              Player_Table.total_pts_column_size + Player_Table.SB_column_size + 7
        
    return Player_Table.print_table(sorted_players, matches_dict)

crosstable(['Emmett Frost', 'Cruz Sullivan', 'Deandre Bullock', 'George Bautista', 'Norah Underwood', 'Renee Preston'], [[None, 1, 0, 0, 0.5, 0], [0, None, 0.5, 1, 0, 0], [1, 0.5, None, 0.5, 0.5, 0.5], [1, 0, 0.5, None, 0.5, 0.5], [0.5, 1, 0.5, 0.5, None, 0.5], [1, 1, 0.5, 0.5, 0.5, None]])
crosstable(['K. Kel', 'A. Vau', 'Z. Aya', 'J. Coc', 'M. Hue', 'A. Sim', 'C. Yan', 'J. Wal', 'M. Hor', 'L. Ell', 'H. Mic', 'P. Bla', 'L. Lan', 'M. Rid', 'M. Bec', 'J. Gat'], [[None, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, None, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, None, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, None, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, None, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, None, 1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1, 0, None, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, None, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, None, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, None, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, None, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, None, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, None, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None]])