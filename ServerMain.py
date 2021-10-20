import socket
import DataBaseAPI
import read_port
import logging
import threading
import uttil

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
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((HOST, PORT))
            self.server_socket.listen()
            logging.info("created a socket, bind it and listen")
        except Exception as e:
            logging.error(e)

        self._accept_conn()

    def _accept_conn(self):
        """
            Accept connection, create a thread to handle him.
        :return:
        """
        while True: # temp while
            conn, addr = self.server_socket.accept()
            logging.info(f" {conn} : {addr} was accepted and now there is a thread for him")
            handle_connection_thread = threading.Thread(target=self.handle_connection, args=(conn, ))

    def read_request(self, conn):
        Client_ID = hex(int(conn.recv(16).decode(), 16))
        Version = int(conn.recv(1).decode())
        Code = conn.recv(2).decode()
        Payload_size = conn.recv(4).decode()
        Payload = conn.recv(int(Payload_size)).decode()

    def handle_connection(self, conn):
        pass

    def __del__(self):
        self.server_socket.close()


class User:

    def __init__(self, IP, uuid):
        self.IP = IP
        self.uuid = uttil.UUID()