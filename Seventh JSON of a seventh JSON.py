# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:40:28 2019

@author: simasurk
"""
import json
#old
def find_seventh_sons_of_seventh_sons(jstring):
    
    family_dict = json.loads(jstring)
    return recursion(family_dict, 0, set()) 
    
def recursion_old(family_dict, rank, seventhsons):
    
    for child in family_dict['children']:
            
        if child['gender'] == 'female': rank = 0
        else: rank += 1 
        
        if rank == 7:
            recursion(child, rank, seventhsons)
        elif rank == 14:
            seventhsons.add(child['name'])
        
        if len(child['children']) > 0 and rank != 7:
            recursion(child, 0, seventhsons)
                
    return seventhsons
#end


#new working   
def find_seventh_sons_of_seventh_sons(family_dict, ss_set = set()):
        
    if type(family_dict) == str: family_dict = json.loads(family_dict) 
    
    if len(family_dict['children']) > 6 and len(family_dict['children'][6]['children']) > 6:
        children_genders = [x['gender'] for x in family_dict['children'][:7]] + [x['gender'] for x in family_dict['children'][6]['children'][:7]]
        #print(children_genders)
        if not 'female' in children_genders:
            ss_set.add(family_dict['children'][6]['children'][6]['name']) 
        
    for child in family_dict['children']:
        find_seventh_sons_of_seventh_sons(child, ss_set)
        
    return ss_set
 #end   
    
find_seventh_sons_of_seventh_sons(contains_seventh_son_of_seventh_son)

contains_seventh_son_of_seventh_son['children'][6]['children'] #77

contains_seventh_son_of_seventh_son = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'male',
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H', # This is the seventh son
         'gender': 'male',
         'children':[
            {'name': 'I',
             'gender': 'male',
             'children': []},
            {'name': 'J',
             'gender': 'male',
             'children': []},
            {'name': 'K',
             'gender': 'male',
             'children': []},
            {'name': 'L',
             'gender': 'male',
             'children': []},
            {'name': 'M',
             'gender': 'male',
             'children': []},
            {'name': 'N',
             'gender': 'male',
             'children': []},
            {'name': 'O', # This is the sventh son of the seventh son
             'gender': 'male',
             'children': [    
                {'name': 'I1',
                 'gender': 'male',
                 'children': []},
                {'name': 'J2',
                 'gender': 'male',
                 'children': []},
                {'name': 'K3',
                 'gender': 'male',
                 'children': []},
                {'name': 'L4',
                 'gender': 'male',
                 'children': []},
                {'name': 'M5',
                 'gender': 'male',
                 'children': []},
                {'name': 'N6',
                 'gender': 'female',
                 'children': []},
                {'name': 'O7', # This is the sventh son of the seventh son
                 'gender': 'male',
                 'children': []}
                    ]}
         ]},
         {'name': 'H2',
         'gender': 'male',
         'children': []}
    ]
}       
