# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:08:34 2019

@author: simasurk
"""

import pdb

def recoverSecret(triplets):
    '''
    Get Secret word from triplets provided.
    '''
    word_list = list()
    
    for triplet in triplets:
        index = None
        for l in triplet:
            if l not in word_list:
                if not index:
                    word_list.append(l)
                    index = word_list.index(l)
                else:
                    index = index+1
                    word_list.insert(index, l)     
            else:
                if not index:
                    pass
                elif word_list.index(l) < index:
                    list_to_move = list()
                    prev_letter = word_list[index]
                    let = l
                    
                    #If first letter is in between 2nd and 3rd letter
                    if word_list.index(triplet[0]) < index and word_list.index(triplet[0]) > word_list.index(l):
                        prev_letter = triplet[0]
                        
                    #List of elements to be moved.
                    while let != prev_letter:
                        list_to_move.append(let)
                        ind = word_list.index(let)
                        word_list.remove(let)
                        let = word_list[ind]
                    
                    #Move list_to_move to appropriate position
                    i = word_list.index(prev_letter)
                    for item in list_to_move:
                        i += 1
                        word_list.insert(i, item)
                    #print('list to move {}'.format(list_to_move))
                    #print('list moved {}'.format(word_list))
                        
                index = word_list.index(l)    
        print(triplet)
        print(word_list)
        print()
    
    return ''.join(word_list)