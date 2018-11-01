# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:11:40 2018

@author: shoeiching.chu
"""
import datetime

currDate = datetime.date.today()

print (currDate)
print (currDate.year)
print (currDate.month)
print (currDate.day)

#print (currentDate.strftime('%d %b,%Y'))

print (currDate.strftime('%A %d %B,%Y'))

print (currDate.strftime
('Please attend our event %A, %B %d in the year %Y'))

print ("Timedelta 15 days :")
print (currDate + datetime.timedelta(days=15))
print ("Timedelta 15 hours :")
print (currDate + datetime.timedelta(hours=15))