# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:52:18 2019

@author: joaoi
"""

import psycopg2

#Configuracao Database PostgreSQL (Alterar conforme configuracao do banco)
host='localhost'
database='postgres'
user='postgres'
password='postgres'

con = psycopg2.connect(host=host, database=database, user=user, password=password)
cur = con.cursor()

def getConnection():
    return con

def getCursor():
    return cur    

def closeConnection():
    con.close()    