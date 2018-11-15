# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:53:56 2018

@author: shoeiching.chu
"""
#Open file
import re
hand = open('data/mbox-short.txt')

'''
for line in hand:
    line = line.rstrip()
'''

x='From: Using the : character:'
print(re.findall('^F.+:',x)) #Greedy match
print(re.findall('^F.+?:',x)) #NonGreedy match

y= re.findall('\S+@\S+',x)
print(y)

z= 'we just received $10 for cookies.'
a=re.findall('\$[0-9]',z)
print(a)

    

#    print(re.findall('[0-9]+',line))    
#    if re.search('^X-\S+:',line):
#            print(line)      
#    if re.search('^X.*:',line):
#            print(line)        
    # take line start with "From:" only
#   if re.search('^From:',line) :
#        print(line)
     #Method1 take any line with "From:"
#    if re.search('From:',line) :
#        print(line)
     #Method2 take any line with "From:"
#    if(line.find('From:')) >=0 :
#        print(line)

        
