#Greeen with Recursion

import itertools as it

def infinite_seq():
    num = 1
    while True:
        yield num
        num += 1
inf_seq = infinite_seq()

def recurGreen(prevNumber, start, count):
    inf_seq = infinite_seq()
    for i in inf_seq:
        newN = int (str(i) + str(prevNumber))
        if str(newN**2).endswith(str(newN)):
            print('Number : '+str(newN)+' -> Square : '+str(newN**2))
            start += 1
            if start == count:
                print('10 done')
                return newN
            recurGreen(newN, start, count)