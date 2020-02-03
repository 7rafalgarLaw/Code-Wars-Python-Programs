# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:00:59 2019

@author: simasurk
"""

'''
ALGORITHM
Derive Keypresses

Find char in current keypad x
if not found 
    goto next keypad
return keys_pressed
    
Number of keys pressed

loop over keys_pressed
    if shift pressed 
        change keypad
        prev position = 0,0
    else
        add prev position
'''

KEYPAD1 = "abcde123fghij456klmno789pqrst.@0uvwxyz_/` "
KEYPAD2 = "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/` "
KEYPAD3 = """^~?!'"()-:;+&%*=<>€£$¥¤\[]{},.@§#¿¡111_/` """
MAP1    = {c: (i//8, i%8) for i,c in enumerate(KEYPAD1)}
MAP2    = {c: (i//8, i%8) for i,c in enumerate(KEYPAD2)}
MAP3    = {c: (i//8, i%8) for i,c in enumerate(KEYPAD3) if c != '1'}
MAPS = {0: MAP1, 1: MAP2, 2:MAP3}

def current_keypad(active_keypad):
    return MAPS[active_keypad % 3]

def tv_remote(words):
    if not words: return 0

    #derive keypresses required to type - words
    keys_pressed, active_keypad = '', 0
    for l in words:
        while l not in current_keypad(active_keypad):
            keys_pressed += '`'                                             #'`' is shift                 
            active_keypad += 1                                              #keypad changed after ` pressed
        else:
            keys_pressed += l
            
    #calculate the number of keys pressed
    key_presses, active_keypad = 0, 0
    prev_position = (0, 0)
    
    for l in keys_pressed:
        key_presses += shortest_route(current_keypad(active_keypad)[l], prev_position) + 1
        if l == '`':
            active_keypad += 1
        prev_position = current_keypad(active_keypad)[l]
        
    return key_presses

def shortest_route(new_position, prev_position):
    dist_along_x = abs(new_position[0] - prev_position[0])
    dist_along_y = abs(new_position[1] - prev_position[1])
    routes = list()
    
    #routes with wrapping.
    routes.append(dist_along_x + dist_along_y)
    if dist_along_x: routes.append(abs(6 - dist_along_x) + dist_along_y)    #wrap along x
    if dist_along_y: routes.append(dist_along_x + abs(8 - dist_along_y))    #wrap along y
    if dist_along_x and dist_along_y: 
        routes.append(abs(6 - dist_along_x) + abs(8 - dist_along_y))        #wrap along x and y
    
    return min(routes)
    
tv_remote('Too Easy?')  #71