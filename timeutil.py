# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:08:01 2018

@author: shoeiching.chu
"""

import datetime

currentTime = datetime.datetime.now()

print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)


print (datetime.datetime.strftime(currentTime,'%H:%M'))
print (datetime.datetime.strftime(currentTime,'%I:%M %p'))
