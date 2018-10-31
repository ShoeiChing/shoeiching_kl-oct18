# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:33 2018

@author: shoeiching.chu
"""

answer = input("Would you like express shipping? (yes/no):").lower()
shippingSelected = False

if answer == "yes" :
    print("That will be an extra $10")
    shippingSelected = True
else:
    print("Standard Shipping selected..")  
 
if(shippingSelected) :
      print("Thank you for selecting Express Shipping!!")          
        
    
    
    
    