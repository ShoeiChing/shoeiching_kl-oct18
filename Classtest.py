# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:28:32 2018

@author: shoeiching.chu
"""

class Test:
    
    name = "Test"
#    __name = "Test"
    
    def __init__(self,name="Object"):
        self.name=name
        
    def talk(self,msg):
        #talkName = "Just Talk"
        print(self.name + "," + msg)
        
    def myName(self):
        print(self.name + ", I am Test..")
        
        
obj1 = Test()
obj1.talk("Hi")
obj1.myName()

obj2 = Test("Obj2")
obj2.myName()
 
print(f"Class Name {Test.name}")
print(f"Class Name {obj1.name}")
print(f"Class Name {obj2.name}")