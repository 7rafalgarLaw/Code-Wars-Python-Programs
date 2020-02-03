# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:13:45 2019

@author: simasurk
"""

'''
Algorithm: 

symbol_position_dict (value, position)
to go from (g, 1,1) to (n, 2,3)
to go from (e, 0,4) to (w, 4,2)
Find diff in x and y and add 1 for OK
'''

#Dictionary creation for the screen keyboard
#key - letter, value - position
data = 'abcde123 fghij456 klmno789 pqrst.@0 uvwxyz_/'

i, j = 0, 0
symbol_position_dict = dict()
for string in data.split(' '):
    for l in string:
        symbol_position_dict[l] = (i, j)
        j += 1
    i += 1
    j = 0

#updated data creation
#KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/"
#MAP      = {c: (i//8, i%8) for i,c in enumerate(KEYBOARD)}

def tv_remote(word):
    key_presses, prev_position = 0, (0, 0)
    for l in word:
        key_presses += abs(symbol_position_dict[l][0] - prev_position[0]) + \
                        abs(symbol_position_dict[l][1] - prev_position[1]) + 1
        prev_position = symbol_position_dict[l]
        
    return key_presses
    
tv_remote('codewars')