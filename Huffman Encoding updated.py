# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:57:00 2019

@author: simasurk
"""
from collections import Counter

class Node:
    """
    Nodes used to create the tree structure.
    """
    def __init__(self, name, freq):
        self.left = None
        self.right = None
        self.frequency = freq
        self.name = name
        
    def __str__(self):
        return self.name + ', ' + str(self.frequency)
    
def encode(freqs, s):
    
    if len(freqs) in [0,1]:return None
    
    freqs.sort(key = lambda x : x[1])
    rootNode = constructTree(freqs) 
    
    #bits_dict = {key = letter, value = encoded bit representation}   
    bits_dict = dict()
    getEncodedbits(rootNode, '', bits_dict)
    
    return ''.join([bits_dict[l] for l in s])

def decode(freqs, bits):
    
    if len(freqs) in [0,1]:return None
    
    freqs.sort(key = lambda x : x[1])
    rootNode = constructTree(freqs) 
    
    #bits_dict = {key = letter, value = encoded bit representation}
    bits_dict = dict()
    getEncodedbits(rootNode, '', bits_dict)
    
    new_bits_dict = {value:key for key,value in bits_dict.items()}
    key = ''
    decoded_string = ''
    for l in bits:
        key+=l
        if key in new_bits_dict.keys():
            decoded_string += new_bits_dict[key]
            key = ''
            
    return decoded_string

def frequencies(s):

    return list(Counter(s).items())

def constructTree(freqs):
    """
    Method constructs the tree and returns the root node.
    """
    list_nodes = [Node(a,b) for a,b in freqs]
    list_nodes.sort(key = lambda n : n.frequency)
    
    while len(list_nodes) != 1:
        newNode = Node(list_nodes[0].name + list_nodes[1].name, list_nodes[0].frequency + list_nodes[1].frequency)
        newNode.left, newNode.right = list_nodes[0], list_nodes[1] 
        list_nodes = list_nodes[2:]
        list_nodes.append(newNode)
        list_nodes.sort(key = lambda n : n.frequency)
    else:
        return newNode

def getEncodedbits(root, string, bits_dict):
    """
    Tree traversal using recursion
    """
    if root.left != None:
        string += '0'
        getEncodedbits(root.left, string, bits_dict)
        
    if root.right != None:
        string = string[:-1]
        string += '1'
        getEncodedbits(root.right, string, bits_dict)
        
    if root.left == None and root.right == None:
        bits_dict[root.name] = string

freqs = frequencies('aaaabcc')
encode(freqs,'aaaabcc')
decode(freqs, '1111000101')


