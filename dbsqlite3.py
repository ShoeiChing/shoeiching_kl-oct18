# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:34:48 2018

@author: shoeiching.chu
"""

import sqlite3 as lite
import sys

con = None
try:
    #con = lite.connect('newtest.db')
    con = lite.connect('data/testdb.db')
    cur = con.cursor()
    #cur.execute('SELECT SQLITE_VERSION()')
    cur.execute('SELECT * FROM stuff')
    #data = cur.fetchone()
    #print(f'SQLITE version: {data}')
    
    data = cur.fetchall()

    for row in data :
        print(row)    
    
except lite.Error as e :
    print(f"Error {e.args[0]}")
finally :
    if con:
        con.close()
        
    