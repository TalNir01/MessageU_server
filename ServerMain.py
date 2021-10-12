import socket
import DataBaseAPI
import read_port
import logging
import threading


class ServerSock:

    logging.basicConfig(filename="server_socket.log", filemode='w', level=logging.INFO, format='%(name)s@%(levelname)s -> %(message)s')


    def __init__(self, DB):
        """
            Init Socket
        :param DB: the Data-Base API object
        """
        self.DB = DB
        PORT = read_port.read_port_number()
        HOST = "0.0.0.0"
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen()
        logging.info("created a socket, bind it and listen")

        self._accept_conn()

    def _accept_conn(self):
        """
            Accept connection, create a thread to handle him.
        :return:
        """
        while True: # temp while
            conn, addr = self.server_socket.accept()
            handle_connection_thread = threading.Thread(target=)



    def __del__(self):
        self.server_socket.close()
