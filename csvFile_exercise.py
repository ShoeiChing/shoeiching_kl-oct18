# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:29:15 2018

@author: shoeiching.chu
"""

import csv

fileName = "demo.csv"
accessMode = "r"

with open(fileName, accessMode) as myCSVFile:
    dataFromFile = csv.reader(myCSVFile)

    for row in dataFromFile :
        print(row)
        
myCSVFile.close()          