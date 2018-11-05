# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:36:05 2018

@author: shoeiching.chu
"""


fileName = "Sample.txt"
accessMode = "w"

myFile = open(fileName, accessMode)
myFile.write("Hi!!\n")
myFile.write("How are you?")
myFile.close()

