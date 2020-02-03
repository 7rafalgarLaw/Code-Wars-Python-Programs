# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:47:16 2019

@author: simasurk
"""
class Store:
    def __init__(self, name):
        self.Parentname = name
        self.items = []
        
    @classmethod
    def createChain(cls, *args):
        return cls(*args)
    
class SubStore(Store):
    def __init__(self, Pname, name):
        super().__init__(Pname)
        self.name = name
        
newStore = Store('ABC')
newStore.Parentname

newsubStore = SubStore('ABC', 'abc1')
newsubStore.name
newsubStore.Parentname

ns = Store.createChain('Siddhesh')
ns.Parentname
ns.items

nss = SubStore.createChain('Siddhesh', 'Masurkar')
nss.Parentname
nss.name
nss.items




