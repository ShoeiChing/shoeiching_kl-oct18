# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:56:59 2018

@author: shoeiching.chu
"""

class Critter():
    
    name = ""
    
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        print ("Hi. I'm", self.name, "\n")
            
crit1 = Critter("instances")         
crit1.talk()
print (crit1.name)
