# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:40:25 2019
4-kyu, Last digits of N^2 == N
@author: simasurk
"""

def green(n):
    
    dict_7 = {1:1, 2:5, 3:6, 4:25, 5:76, 6:376, 7:625}
    
    if n in dict_7:
        return dict_7[n]
    
    list_values = list(dict_7.values())
    
    num1 = 376
    num2 = 625
    while True:
        z=''
        numFound = False
        if num1<num2:
            while not numFound:
                for i in range(1,10):
                    num = str(i) + z + str(num1)
                    if str(int(num)**2).endswith(num):
                        num1 = int(num)
                        list_values.append(num1)
                        numFound = True
                        break
                if numFound == False:
                    z += '0'
        else:
            while not numFound:
                for i in range(1,10):    
                    num = str(i) + z + str(num2)
                    if str(int(num)**2).endswith(num):
                        num2 = int(num)
                        list_values.append(num2)
                        numFound = True
                        break
                if numFound == False:
                    z += '0'
        #n+1.Just to make sure we get the lowest green number. Hence sorting.
        if len(list_values) >= n+5:  
            return sorted(list_values)[n-1]
        
green(12)
