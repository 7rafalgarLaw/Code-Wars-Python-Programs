# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:36:55 2019

@author: simasurk
"""
def snail(array):
    
    if array == [[]]: return []
    
    snail_list = []
    positions = []
    i, j = 0, 0
    minsize, maxsize = 0, len(array[0]) - 1
    
    while True:
        
        snail_list.append(array[i][j])
        array[i][i] = None
        
        if i == minsize and j == minsize:
            while j != maxsize:
                j += 1
                positions.append((i,j))
            else:
                updatesnaillist(array, positions, snail_list)
                positions.clear()
            
        if i == minsize and j == maxsize:
            while i != maxsize:
                i += 1
                positions.append((i,j))
            else:
                updatesnaillist(array, positions, snail_list)
                positions.clear()

        if i == maxsize and j == maxsize:
            while j != minsize:
                j -= 1
                positions.append((i,j))
            else:
                updatesnaillist(array, positions, snail_list)
                positions.clear()
        
        if i == maxsize and j == minsize:
            while i != minsize:
                i -= 1
                positions.append((i,j))
            else:
                updatesnaillist(array, positions, snail_list)
                positions.clear()
        
        i, j = minsize + 1, minsize + 1
        minsize, maxsize = minsize + 1, maxsize - 1
        if minsize > maxsize:
            break
        
    return snail_list

def updatesnaillist(array, positions, snail_list):
    """
    Get the values on each right turn while traversing the matrix.
    """
    for a,b in positions:
        if array[a][b] != None:
            snail_list.append(array[a][b])
            array[a][b] = None
    
"""   
array = [[1,2,3,4],
         [4,5,6,7],
         [7,8,9,8],
         [1,2,3,4]]
array1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array1)
"""
