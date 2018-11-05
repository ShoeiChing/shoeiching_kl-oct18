# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:31:39 2018

@author: shoeiching.chu
"""

guests = []
name=  " "

while name != "DONE":
    name = input("Please enter the guest name(Please enter DONE if done):")

if name="DONE":
    guests.append(name)    

guests.sort()

for name in guests:
    print(name)