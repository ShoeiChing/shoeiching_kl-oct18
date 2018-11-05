# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:59:27 2018

@author: shoeiching.chu
"""

fileName = "demo.csv"
accessMode = "r"
myFile = open(fileName, accessMode)

fileContent = myFile.readline()

while fileContent:
    print(fileContent)
    fileContent = myFile.readline() 
    
myFile.close()
