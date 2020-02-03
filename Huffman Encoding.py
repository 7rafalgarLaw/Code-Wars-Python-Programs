# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:08:03 2019

@author: simasurk
"""
from collections import Counter

def encode(freqs, s):
    if len(freqs) in [0,1]: return None
    
    freqs.sort(key = lambda x : x[1])
    obj_dict = constructtree(freqs)    
    
    #bits_dict = {key : letter, value : encoded bits}
    bits_dict = dict()
    for l in [a for a,b in freqs]:
        bits_dict[l] = bitrepresentation(obj_dict, l)
        
    return ''.join([bits_dict[l] for l in s])

def decode(freqs, bits):
    if len(freqs) in [0,1]: return None

    freqs.sort(key = lambda x : x[1])
    
    obj_dict = constructtree(freqs)
    
    #bits_dict = {key : encoded bits, value : letter}
    bits_dict = dict()
    for l in [a for a,b in freqs]:
        bits_dict[bitrepresentation(obj_dict, l)] = l
      
    key = ''
    decoded_string = ''
    for l in bits:
        key+=l
        if key in bits_dict.keys():
            decoded_string += bits_dict[key]
            key = ''
    
    return decoded_string

class Node:
    
    def __init__(self, letter, freq):
        self.name = letter
        self.parent = None
        self.position = None
        self.frequency = freq
        
    def __str__(self):
        node_str = 'Letter : ' + self.name + ', Frequency : ' + str(self.frequency) + ', Position : ' + str(self.position)
        if self.parent != None:
            node_str += ', Parent : ' + self.parent.name
        return node_str

def frequencies(s):
    return list(Counter(s).items())

#Construct Tree
#obj_dict = {key : letter, value : node}
def constructtree(freqs):
    obj_dict = dict()
    
    node1 = Node(freqs[0][0], freqs[0][1])
    obj_dict[node1.name] = node1
    
    for x in range(1, len(freqs)):
        node2 = Node(freqs[x][0], freqs[x][1])
        obj_dict[node2.name] = node2
        
        if node1.frequency <= node2.frequency:
            node1.position,node2.position = 0,1
        else:
            node1.position,node2.position = 1,0
            
        node1.parent = Node(node1.name+node2.name, node1.frequency+node2.frequency)
        node2.parent = node1.parent
        node1 = node1.parent
    
    return obj_dict

def bitrepresentation(obj_dict, l):
    bit_rep = ''
    node = obj_dict[l]
    
    while node.parent != None:
        bit_rep += str(node.position)
        node = node.parent
    return bit_rep[::-1]



freqs = frequencies('siddheshmasurkar')
encoded_string = encode(freqs, 'siddheshmasurkar')
encoded_string
decode(freqs, '0111111110111101111011101111111110111011111110110011111101011111011010')

"""get Tree codes?
printtree(root, arr)

if left->
    arr+=0
    printTree(root->left, arr)
    
if right->
    arr+=0
    printTree(root->right, arr)
    
if leaf->
    dict(leaf-value, arr)
"""

"""Construct tree with left right

create heap with all nodes
get two leftmost nodes to create one
repreat till one node is left
"""