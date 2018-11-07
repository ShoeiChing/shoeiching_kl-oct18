# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:15:49 2018

@author: shoeiching.chu
"""


import csv

myCSVFile = open('data/demo.csv','r')
dataFromFile = csv.reader(myCSVFile)

print(dataFromFile)

'''standard -->['Test1', '22']
for row in dataFromFile :
    print(value)
'''

'''print in next row
for row in dataFromFile :
    #print row
    for value in row :
        print(value)
'''

#print for format --> Test1 22 /Test1, 22
for row in dataFromFile :
#    print (', '.join(row))
    print (' '.join(row))
    
myCSVFile.close()   