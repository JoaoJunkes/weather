# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:52:18 2019

@author: joaoi
"""

import psycopg2

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='postgres')
cur = con.cursor()

def getConnection():
    return con

def getCursor():
    return cur    

def closeConnection():
    con.close()    