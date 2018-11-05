# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:01:42 2018

@author: shoeiching.chu
"""

#1.create a funstcion to print "Hello"
'''
def sayHello(name) :
    print ("Hello " + name +", how are you?")
    return
#Invoke the function
sayHello("Everyone")
sayHello("Girls")
sayHello("Guys")
'''

'''
def sayHello(firstname,lastname) :
    print ("Hello " + firstname +" "+lastname +", how are you?")
    return

#Invoke the function
sayHello("Everyone"," ")

sayHello("Girls"," ")

sayHello("Guys"," ")
'''
'''
def addTwo(var1,var2):
    sum=var1+var2
    return sum

print("Sum of 5+5 =" + str(addTwo(5,5)))
 '''
 
def printinfo(name,age=16,location="KL"):
     print ("Name:", name)
     print ("Age:", age)
     print ("Location:", location)
     return;
 
printinfo("miki",50,"Penang")
printinfo(age=50,name="miki",location="PJ")
printinfo("bob")

 