# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:29:52 2018

@author: shoeiching.chu
"""

class puppy:

    name=""

    color=""
    def __init__(self, name, color) :
       
        self.name = name
        self.color = color
        
    def bark(self) :
        print("I am", self.color, self.name)
        
    def __str__(self):
        ret = "Puppy Object\n"
        ret+= "Name:" + self.name +"\n"
        return ret
        
puppy1 = puppy("Max", "brown") 
puppy1.bark()

puppy2 = puppy("Ruby", "black")
puppy2.bark()

print (puppy2.name)

print(dir(puppy2))   
print(puppy2)    