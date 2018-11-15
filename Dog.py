# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:04:47 2018

@author: shoeiching.chu
"""

class Dog:
    
    Species='mammal'
    name = ""
    age = 0
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
jake = Dog("Jake",7)
doug = Dog("Doug",8)
william = Dog("William",5)

def get_biggest_number(*args):
    return max(args) 

print("The oldest dog is {} years old.".format
      (get_biggest_number(jake.age,doug.age,william.age)))

print(jake.Species)

        