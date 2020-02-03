# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:34:27 2019

@author: simasurk
"""
import itertools as it

def encode_rail_fence_cipher(string, n):
    
    encoded_string = ''
    dict_encoded = {x:list() for x in range(1,n+1)}
    
    pattern = list(range(1,n+1))
    pattern.extend(list(range(n-1,1,-1)))
    
    len_string = len(string)
    i=-1
    for p in it.cycle(pattern):
        i+=1
        if i == len_string:
            break
        dict_encoded[p].append(string[i])
        
    for i in range(1,n+1):
        encoded_string += ''.join(dict_encoded[i])   
        
    return encoded_string
    
def decode_rail_fence_cipher(string, n):
    
    decoded_string = ''
    encoding = []
    dict_encoded = {x:list() for x in range(1,n+1)}
    len_string = len(string)
    
    pattern = list(range(1,n+1))
    pattern.extend(list(range(n-1,1,-1)))
    
    i=0
    for p in it.cycle(pattern):
        if i == len_string:
            break
        encoding.append(p)
        i+=1
        
    i=0
    for x in sorted(encoding):
        dict_encoded[x].insert(0, string[i])
        i+=1
    
    i=0
    for j in it.cycle(pattern):
        if i == len_string:
            break
        if len(dict_encoded[j]) !=0:
            decoded_string += dict_encoded[j].pop()
        i+=1
        
    return decoded_string