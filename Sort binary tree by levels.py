# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:33:32 2019

@author: simasurk
"""
class Node:

    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    
    if node == None: return []
    
    values = [node.value]
    nodes = [node]
    elements_sortedbylevels(nodes, values)
    return values
    
def elements_sortedbylevels(nodes, values):
    """
    Recursion for every level of traversal.
    """
    list_nodes = []
    
    for node in nodes:
        if node.left != None:
            values.append(node.left.value)
            list_nodes.append(node.left)
        if node.right != None:
            values.append(node.right.value)
            list_nodes.append(node.right)
    
    if len(list_nodes) > 0: elements_sortedbylevels(list_nodes, values)


#tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))
