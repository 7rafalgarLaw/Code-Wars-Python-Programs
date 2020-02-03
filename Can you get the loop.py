# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:42:46 2019

@author: simasurk
"""
class Node:
    
    def __init__(self):
        self.next = None
    
def loop_size(node):
    
    nodes_dict, i = dict(), 1

    while id(node) not in nodes_dict:
        nodes_dict[id(node)] = i
        i += 1
        node = node.next
    else:
        return i - nodes_dict[id(node)]

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

#loop_size(node1)
