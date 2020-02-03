# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:13:14 2019

@author: simasurk
"""

import time
import timeit
import threading
import random
from functools import reduce

number = 0

def func(num):
    global number
    random_list = random.sample(range(1000000000), num)
    number += reduce(lambda x, y: x+y, random_list)

#Threading
start_time = time.time()
thread1 = threading.Thread(target=func, args=(5000000,))
thread2 = threading.Thread(target=func, args=(5000000,))
thread1.start()
thread2.start()
#print(number) = 0
thread1.join()
thread2.join()
end_time = time.time()
print(end_time - start_time)
print(number)



#Normal Processing
start_time = time.time()
func(5000000)
func(5000000)
end_time = time.time()
print(end_time - start_time)
print(number)










# https://stackoverflow.com/questions/29523328/threading-in-python-takes-longer-time-instead-of-making-it-faster
# The example code below it is 100% computation so threading really doesnt improve execution time
import timeit
import time
import threading
import multiprocessing

def fn():
    x = 0
    while  x < 100000000:
        x += 1

def TEST_THREADS():
    new_thread1  = threading.Thread(target = fn , args = ())
    new_thread2  = threading.Thread(target = fn, args = ())
    new_thread3  = threading.Thread(target = fn, args = ())
    new_thread1.start()
    new_thread2.start()
    new_thread3.start()
    new_thread1.join()
    new_thread2.join()
    new_thread3.join()

def TEST_NORMAL():
    fn()
    fn()
    fn()

def TEST_MULTIPROCESSING():
    new_process1  = multiprocessing.Process(target = fn , args = ())
    new_process2  = multiprocessing.Process(target = fn, args = ())
    new_process3  = multiprocessing.Process(target = fn, args = ())
    new_process1.start()
    new_process2.start()
    new_process3.start()
    new_process1.join()
    new_process2.join()
    new_process3.join
    
if __name__ == "__main__":  
    '''It is very important to use name == __main__ guard code with threads and multiprocessing'''
    print(timeit.timeit(fn,number=1))
    print(timeit.timeit(TEST_NORMAL,number=1))
    print(timeit.timeit(TEST_THREADS,number=1))
    print(timeit.timeit(TEST_MULTIPROCESSING,number=1))
#OUTPUT
'''
5.90055779999966
19.156090200000108
18.675973899999008
0.30363299999953597    
'''