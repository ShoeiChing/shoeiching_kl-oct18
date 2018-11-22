# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:54:44 2018

@author: shoeiching.chu
"""


from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
   return "Welcome World! </p> <a href=http://127.0.0.1:5000/hello> Hello </a></p> <a href=http://127.0.0.1:5000/goodbye> Goodbye </a>"

@app.route("/hello")
def hello():
   return "Hello World!"
   
@app.route("/goodbye")
def goodbye():
   return "Goodbye World!"

if __name__=="__main__":
   app.run()