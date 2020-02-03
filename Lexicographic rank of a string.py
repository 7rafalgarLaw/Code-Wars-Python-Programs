# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:07:57 2019

@author: simasurk
"""
import itertools as it
from functools import reduce 
from collections import Counter

def listPositionOld(word):
    """Time Consuming Solution"""
    list_words = [''.join(x) for x in sorted(set(it.permutations(word)))]
    word_dict = {y:x for x,y in enumerate(list_words, 1)}
    #print(word_dict)
    return word_dict[word]  

def fact(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

listPositionOld('NGDFYHTEIXVOSWFBPYNOKA')  
listPositionOld('BOOKKEEPER')


#working for strings with no repeating characters.
"""
New ALGORITHM
word - string
sorted word - ginrst

s - 4 * 5!
t - 4 * 4!
r - 3 * 3!
i - 1 * 2!
n - 1 * 1!

4 * 5*4*3*2 + 4 * 4*3*2 + 3 * 3*2 + 1 * 2 + 1 * 1
"""
def listPositionUpdated(word):

    sorted_word = sorted(word)
    len_word = len(word)
    position = 0
    
    for l in word[:-1]:
        position += (sorted_word.index(l) * fact(len_word - (word.index(l)+1)))
        sorted_word.remove(l)
    return position + 1   





#For strings with repeating characters
# https://www.geeksforgeeks.org/lexicographic-rank-string-duplicate-characters/
"""
ANalysis
BOOKKEEPER - 10743
[B, E, E, E, K, K, O, O, P, R]

B - 
0 
O - 
(5 * fact(8)) / (2*2*3*2) -> 8400
O -
(5 * fact(7)) / (2*3*2) -> 2100
K -
(3 * fact(6)) / (2*3*2) -> 180
K - 
(3 * fact(5)) / (2*3) -> 60
E -
(0 * fact(6)) / (2*3*2) -> 0
E - 
(0 * fact(6)) / (2*3*2) -> 0
P -
(1 * fact(2)) -> 2
E -
0
R -
0
"""
def listPosition(word):
    
    word, sorted_word, len_word = list(word), sorted(word), len(word)
    
    position = 0
    for l in word[:-1]:
        #div is used to handle duplicate letters
        val = filter(lambda y: y > 1, list(Counter(word[word.index(l):]).values()))
        div = reduce(lambda x,y:(x * y), [fact(x) for x in [1] + list(val)])
        
        position += (sorted_word.index(l) * (fact(len_word - (word.index(l)+1)))) / div
        word[word.index(l)] = ''
        sorted_word.remove(l)

    return int(position + 1)   

listPositionOld('BOOKKEEPER')
listPosition('NGDFYHTEIXVOSWFBPYNOKA')
