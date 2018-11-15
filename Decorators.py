# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:15:33 2018

@author: shoeiching.chu
"""

def say_Hello(name) :
    return "Hello, " + str(name) + "!"

def p_decorate(func) :
    def func_wrapper(name) :
        return "<p>" + func(name) + "</p>"
    return func_wrapper

if __name__ == "__name__":
    my_say_hello = p_decorate(say_Hello)
    print(my_say_hello("John"))
    
    