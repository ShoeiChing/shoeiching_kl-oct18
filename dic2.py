# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:26:25 2018

@author: shoeiching.chu
"""

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
        
print(counts)   

print(counts.get('cwen',0))
