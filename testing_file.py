import sqlite3
import logging
import DataBaseAPI
import socket

class U1():
    def __init__(self):
        self.fname = "Tal"
        self.lname = "Nir"
    def __bytes__(self):
        pass
    def __str__(self):
        return self.fname + " " + self.lname

t1 = U1()
print(t1)
t2 = t1
t2.fname = "Bad"
print(t2)
print(t1)
