# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:59:25 2019

@author: simasurk
"""
class Player:
    
    def __init__(self, name, results):
        self.name = name
        self.last_name = name.split(' ')[1]
        self.results = results
        self.pts = sum(list(filter(None, results))) #works somehow! removes None
        self.SB = 0
        self.rank = ''
        
    def __str__(self):
        '''
        table_row = self.name.ljust(15)
        for i in self.results:
            if self.results[i] == ' ': table_row += '   ' 
            else: table_row += str(self.results[i]) + '  '
        return table_row[:-2]
        '''
        return str(self.rank).ljust(4) + self.name.ljust(Player_Table.player_column_size) +\
        str(self.results).ljust(35) + str(self.pts).ljust(Player_Table.pts_column_size) + str(self.SB)
        
    def __repr__(self):
        return repr((self.name, self.pts, self.SB))
    
class Player_Table:
    
    number_of_players = None
    player_column_size = None
    pts_column_size = None
    rank_column_size = None
    width_size = None
    SB_column_size = None
    
    #put it in a string
    #v1.0
    '''
    def print_table(players, matches_dict):
        print('#'.ljust(Player_Table.rank_column_size) + 'Player'.ljust(Player_Table.player_column_size), end='')
        for i in range(1, Player_Table.number_of_players + 1):
            print(i, end = ' ')
        print(' ' + 'Pts'.ljust(Player_Table.pts_column_size) + 'SB'.center(Player_Table.SB_column_size) + '\n', end = '')
        
        print(Player_Table.width_size * '=' + '\n', end='')
            
        for p in players:
            print(p.rank.ljust(3) + p.name.ljust(Player_Table.player_column_size), end='')
            for j in players:
                print(matches_dict[p.name+'-'+j.name], end = ' ')
            print(' '+str(p.pts).ljust(Player_Table.pts_column_size), end = '')
            print("{0:.2f}".format(p.SB), end = '\n')
    '''
    
    #v2.0
    def print_table(players, matches_dict):
        SB_adjust = Player_Table.SB_column_size if Player_Table.SB_column_size % 2 == 0 else Player_Table.SB_column_size - 1
        string = ''
        string += '#'.ljust(Player_Table.rank_column_size) + 'Player'.ljust(Player_Table.player_column_size)
        
        for i in range(1, Player_Table.number_of_players + 1):
            string += str(i) + ' '
        string += ' ' + 'Pts'.ljust(Player_Table.pts_column_size) + 'SB'.center(SB_adjust).rstrip() + '\n'
        
        string += Player_Table.width_size * '='
            
        for p in players:
            string += '\n' + p.rank.ljust((Player_Table.rank_column_size)) + p.name.ljust(Player_Table.player_column_size)
            for j in players:
                string += matches_dict[p.name+'-'+j.name] + ' '
            string += ' ' + str(p.pts).ljust(Player_Table.pts_column_size)
            string += "{0:.2f}".format(p.SB)
        
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
                result = str(results[i][j])
            matches_dict[players[i]+'-'+players[j]] = result
        
    Player_Table.player_column_size = len(max(players, key=len)) + 2
    #Player_Table.pts_column_size = len(max([str(x.pts) for x in list_players], key=len)) + 2
    Player_Table.pts_column_size = len(str(max([x.pts for x in list_players]))) + 2
    
    #calculate SB
    for p in list_players:
        for i in range(Player_Table.number_of_players):
            if p.results[i] == 1:
                p.SB += list_players[i].pts
            elif p.results[i] == 0.5:
                p.SB += list_players[i].pts / 2
                
#rank the players
    #data_players = [(x.pts, x.SB, x.name.split(' ')[1]) for x in list_players]
    #print(data_players)
    #print()
    sorted_players = sorted(list_players,key=lambda x: (-x.pts,-x.SB,x.last_name))
       
    #Set ranks
    prev_pts, prev_SB = 0, 0
    rank = 1
    for sp in sorted_players:
         if sp.pts != prev_pts or sp.SB != prev_SB:
             sp.rank = str(rank)
         rank += 1 
         prev_pts, prev_SB = sp.pts, sp.SB
        
    #for p in sorted_players:
        #print(p)
    
    Player_Table.rank_column_size = len(str(Player_Table.number_of_players)) + 2
    Player_Table.SB_column_size = len(str(max([round(x.SB) for x in sorted_players]))) + 3
        
    Player_Table.width_size = Player_Table.rank_column_size + Player_Table.player_column_size +\
                              Player_Table.number_of_players * 2 + 1 + Player_Table.pts_column_size +\
                              Player_Table.SB_column_size
    print(Player_Table.print_table(sorted_players, matches_dict))
    return Player_Table.print_table(sorted_players, matches_dict)

players = ['Emmett Frost', 'Cruz Sullivan', 'Deandre Bullock', 'George Bautista', 'Norah Underwood', 'Renee Preston']
results = [[None, 1, 0, 0, 0.5, 0], [0, None, 0.5, 1, 0, 0], [1, 0.5, None, 0.5, 0.5, 0.5], [1, 0, 0.5, None, 0.5, 0.5], [0.5, 1, 0.5, 0.5, None, 0.5], [1, 1, 0.5, 0.5, 0.5, None]]

crosstable(players, results)

'''
Expected Result

'#  Player           1 2 3 4 5 6  Pts   SB\n' +
'==========================================\n' +
'1  Renee Preston      = = = 1 1  3.5  7.25\n' +
'2  Deandre Bullock  =   = = = 1  3.0  6.75\n' +
'   Norah Underwood  = =   = 1 =  3.0  6.75\n' +
'4  George Bautista  = = =   0 1  2.5  6.25\n' +
'5  Cruz Sullivan    0 = 0 1   0  1.5  4.00\n' +
'6  Emmett Frost     0 0 = 0 1    1.5  3.00'
'''

'''
Sorting with ranks

oldranks - default rank: player name
dict1 - name1,name2: match result

for i in players:
    for j in players:
        dict1 [name1,name2] = results[0][0]
'''



