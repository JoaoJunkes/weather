# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:20:20 2019

@author: joaoi
"""

class City(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name