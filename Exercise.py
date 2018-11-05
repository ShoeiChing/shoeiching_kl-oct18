# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:31:39 2018

@author: shoeiching.chu
"""

guests = []
name=  "0"

while name != " ":
    name = input("Please enter the guest name(Please enter space if done):")

    if name !=" ":
        guests.append(name)    

guests.sort()

for name in guests:
    print(name)