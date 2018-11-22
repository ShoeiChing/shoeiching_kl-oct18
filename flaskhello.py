# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:22:48 2018

@author: shoeiching.chu
"""

from flask import Flask
app = Flask(__name__)

@app.route("/Hello")
def hello():
   return "Hello World!"

@app.route("/Goodbye")
def goodbye():
   return "Goodbye World!"

if __name__=="__main__":
   app.run()
    