# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:05:02 2019

@author: simasurk
"""
def next_bigger(int_number):

    list_numbers = list()
    number = list(str(int_number))
    
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            new_number = number.copy()
            new_number[i], new_number[j] = new_number[j], new_number[i]
            list_numbers.append(int(''.join(new_number)))
    print(list_numbers)        
                
    bigger_numbers = list(filter(lambda x: x>int_number, list_numbers))
    if len(bigger_numbers) == 0: return -1
    return sorted(list(bigger_numbers))[0]

next_bigger(375)
        