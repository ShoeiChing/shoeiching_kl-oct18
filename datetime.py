# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:11:40 2018

@author: shoeiching.chu
"""
import datetime

currentDate = datetime.date.today()

print (currentDate)
print (currentDate.year)
print (currentDate.month)
print (currentDate.day)

#print (currentDate.strftime('%d %b,%Y'))

print (currentDate.strftime('%A %d %B,%Y'))

print (currentDate.strftime
('Please attend our event %A, %B %d in the year %Y'))