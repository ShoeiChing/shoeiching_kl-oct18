# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:34:48 2018

@author: shoeiching.chu
"""


guests = ['first','second','third']
#print(guests[2])
#print(guests[-1])

#print('First value default :' + guests[0])

guests[0] = 'Steve'

#print('First value is now :' + guests[0])

guests.append('New Guy')

#print('New value is now :' + guests[-1])

#print('2nd Element is :' + guests[1])

#guests.remove('second')
#del guests[1]
#print('2nd Element After remove is :' + guests[1])
   

#scores = [78,68,88,98,25]
#print(scores[3])
#print(scores[-2])


#***check array position****
#print(guests.index('fourth'))

#for steps in range (4):
#    for steps in range len(guests):
#    print(guests[steps])

'''
guests.sort()
    
for guest in guests:
    print(guest)
    
print("Done")
'''

scores = [78,68,88,98,25]
for score in scores:
    print(score)
    
