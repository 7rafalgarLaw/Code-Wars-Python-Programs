# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:09:35 2019

@author: simasurk
"""
KEYBOARD = "a,b,c,d,e,1,2,3,f,g,h,i,j,4,5,6,k,l,m,n,o,7,8,9,p,q,r,s,t,.,@,0,u,v,w,x,y,z,_,/,aA,SP"
MAP      = {c: (i//8, i%8) for i,c in enumerate(KEYBOARD.split(','))}

def tv_remote(words):
    keys_pressed = ''
    if not words: return keys_pressed
    CapsLock = False
    #derive keypresses seperated by ','
    for l in words:
        if l == ' ':  
            keys_pressed += 'SP,'
            continue
        if (l.isupper() and CapsLock == False) or (l.islower() and CapsLock == True):
            keys_pressed += 'aA,'
            CapsLock = not CapsLock
        keys_pressed += l.lower() + ','
    
    #calculate the number of keys pressed
    key_presses, prev_position = 0, (0, 0)
    for l in keys_pressed[:-1].split(','):
        key_presses += abs(MAP[l][0] - prev_position[0]) + \
                        abs(MAP[l][1] - prev_position[1]) + 1
        prev_position = MAP[l]
        
    return key_presses

tv_remote('    x   X    ')