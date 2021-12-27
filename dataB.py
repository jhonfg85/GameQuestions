# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:34:57 2021

@author: John
"""

import sqlite3

class DataB:
    
    def __init__(self, dbName):
        try:
            self.conexion = sqlite3.connect(dbName)    #connect database
            self.cursor = self.conexion.cursor()  #open the cursor
        except:
            print("Error de conexion")
        self.dbName = dbName
    def openConection(self, dbName):
        try:
            self.conexion = sqlite3.connect(dbName)    #connect database
            self.cursor = self.conexion.cursor()  #open the cursor
        except:
            print("Error de conexion")

    def execution(self, instruction):
        self.openConection(self.dbName)
        self.cursor.execute(instruction)
        datos = self.cursor.fetchall()
        self.conexion.commit()
        self.closeConnection()
        return datos

    def closeConnection(self):
        self.conexion.commit()   #confirm changes
        self.conexion.close()    #close database