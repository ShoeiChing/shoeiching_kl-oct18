# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:23:54 2018

@author: shoeiching.chu
"""

import re
hand = open('data/mbox-short.txt')

for line in hand:
    line = line.rstrip()

    if re.search('[A-Z][0-9]+',line):
            print(line)  

 