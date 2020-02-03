# -*- coding: utf-8 -*
"""
Created on Mon Jun 17 16:14:05 2019

@author: simasurk
"""
def validSolution(board):
    
    list_blocks = [x for x in board] + list(zip(*array))
    
    blocks = [list(zip(*array[a:b])) for a,b in [(0,3),(3,6),(6,9)]]
    ranges = [(0,3),(3,6),(6,9)]*3
    rows = [2,2,2,1,1,1,0,0,0]
    for a,b in ranges:
        list_blocks.append([x for y in blocks[rows.pop()][a:b] for x in y])
      
    for block in list_blocks:
        return False if len(block) != len(set(block)) or 0 in block
    
    return True
    
"""
array = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [4, 8, 7, 2, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 3, 9]]

validSolution(array)
"""