# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:01:53 2019

@author: simasurk
"""
KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/C "
MAP      = {c: (i//8, i%8) for i,c in enumerate(KEYBOARD)}

def tv_remote(words):
    if not words: return 0

    keys_pressed = ''
    CapsLock = False
    #derive keypresses required to type words
    for l in words:
        if (l.isupper() and CapsLock == False) or (l.islower() and CapsLock == True):
            keys_pressed += 'C'
            CapsLock = not CapsLock
        keys_pressed += l.lower()
    
    #calculate the number of keys pressed
    key_presses, prev_position = 0, (0, 0)
    for l in keys_pressed:
        key_presses += shortest_route(MAP[l], prev_position) + 1
        prev_position = MAP[l]
        
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
    
tv_remote('Code Wars')  #49