import sqlite3
import logging
import DataBaseAPI
import socket
#A = DataBaseAPI.DataBase()
#A.insert_clients_to_db(123, "Tal", 1234, "a")

HOST = '5.29.43.73'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    #data = s.recv(1024)

#print('Received', repr(data))