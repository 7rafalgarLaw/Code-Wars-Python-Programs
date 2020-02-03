# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:05:35 2019

@author: simasurk
"""
def recursion(family_dict, rank):
    #Even child is capitalized
    print(family_dict['name'].upper()) if rank == 2 else print(family_dict['name'])
    
    if isinstance(family_dict['children'], list):
        rank = 0 
        for child in family_dict['children']:  
            if rank == 2: rank = 0
            rank += 1
            recursion(child, rank)
    
recursion(family_dict, 0)

family_dict = {
    "name": "Jonathan Smith",
    "children": [
        {
            "name": "Adam",
            "children": [
                {
                    "name": "Suzy",
                    "children": ""
                },
                {
                    "name": "Clare",
                    "children": [
                        {
                            "name": "Nat",
                            "children": ""
                        },
                        {
                            "name": "Zakar",
                            "children": ""
                        }
                    ]
                },
                {
                    "name": "Aaron",
                    "children": ""
                },
                {
                    "name": "Simon",
                    "children": ""
                }
            ]
        },
        {
            "name": "Timmy",
            "children": ""
        },
        {
            "name": "Sid",
            "children": ""
        },
        {
            "name": "Alison",
            "children": [
                {
                    "name": "Natasha",
                    "children": ""
                },
                {
                    "name": "Zak",
                    "children": ""
                }
            ]
        }
    ]
}
        