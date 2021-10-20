"""
    DataBase object to control it's API
"""
import sqlite3
from sqlite3 import Error
import logging
import os

class DataBase:
    """DataBase class for managing the DB with easy API """
    logging.basicConfig(filename="data_base_log.log", filemode='w', level=logging.INFO, format='%(name)s@%(levelname)s -> %(message)s')

    def __init__(self):
        """
            Initialize the connection to the DB
        """
        try:
            #os.remove("server.db")
            self.conn = sqlite3.connect("server.db")  # creating the DB
            self.cur = self.conn.cursor()
            logging.info("connected to DB")

            success_clients = self._create_clients_db()
            success_message = self._create_messages_db()

            if not (success_clients and success_message):
                self.__del__()
                logging.error("Closing DB Connection")
                logging.error("Closing Program")
                exit(0)
        except Error as e:
            logging.error(e)

    def __del__(self):
        self.conn.close()

    def _create_clients_db(self):
        """
            creating a clients table
        :return: success status
        """
        try:
            self.conn.executescript('''CREATE TABLE clients
                            (ID HEX TEXT PRIMARY KEY NOT NULL,
                            Name VARCHAR(255) NOT NULL,
                            PublicKey HEX TEXT,
                            LastSeen DATE);''')  # create client DB
            self.conn.commit()
            logging.info("Created clients table")
            return True
        except Error as e:
            logging.error(e)
            return False

    def _create_messages_db(self):
        """
            creating a messages table
        :return: success status
        """
        try:
            self.conn.executescript('''CREATE TABLE messages
                            (ID INT PRIMARY KEY NOT NULL,
                            ToClient HEX TEXT NOT NULL,
                            FromClient HEX TEXT NOT NULL,
                            Type INT NOT NULL,
                            Content Blob,
                            FOREIGN KEY(ToClient) REFERENCES clients(ID),
                            FOREIGN KEY(FromClient) REFERENCES clients(ID));''')  # create messages DB
            self.conn.commit()
            logging.info("Created message table")
            return True
        except Error as e:
            logging.error(e)
            return False

    def insert_messages_to_db(self, msg_id, dest_id, src_id, msg_type, msg_content):
        """
            Inserting a message to the db
        :param msg_id: unique id for message (4 bytes int)
        :param dest_id: unique id for the sender client of the message (16 bytes int)
        :param src_id: unique id for the receiver client of the message (16 bytes int)
        :param msg_type: message type (byte int)
        :param msg_content: the content of the message
        :return:
        """
        try:
            self.conn.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?);", [msg_id, dest_id, src_id, msg_type, msg_content])
            self.conn.commit()
        except Error as e:
            logging.error(e)

    def insert_clients_to_db(self, client_id, client_name, client_public_key, client_last_seen):
        """
            Inserting a client to DB
        :param client_id:
        :param client_name:
        :param client_public_key:
        :param client_last_seen:
        :return:
        """
        try:
            self.conn.execute("INSERT INTO clients VALUES (?, ?, ?, ?);", [client_id, client_name, client_public_key, client_last_seen])
            self.conn.commit()
        except Error as e:
            logging.error(e)

    def get_messages_for_client(self, dest_client_uuid):
        """
            pull all waiting message
        :param dest_client_uuid: a unique id for the destination of the message
        :return: messages array
        """
        try:
            self.cur.execute("SELECT FROM messages WHERE ToClient = ?;", [dest_client_uuid])
            messages_array = self.cur.fetchall()
            return messages_array
        except Error as e:
            logging.error(e)
            return None

    def get_public_key(self, ID):
        """
            send the public key
        :param ID: Client ID
        :return: Public key (HEX)
        """
        try:
            self.cur.execute("SELECT PublicKey FROM clients WHERE ID = ?;", [id])
            public_key = self.cur.fetchall()
            return public_key
        except Error as e:
            logging.error(e)
            return 0

    def get_name(self, ID):
        """
            send the public key
        :param ID: Client ID
        :return: Name
        """
        try:
            self.cur.execute("SELECT Name FROM clients WHERE ID = ?;", [id])
            name = self.cur.fetchall()
            return name
        except Error as e:
            logging.error(e)
            return ""

    def get_last_seen(self, ID):
        """
            send the public key
        :param ID: Client ID
        :return: LastSeen
        """
        try:
            self.cur.execute("SELECT LastSeen FROM clients WHERE ID = ?;", [id])
            last_seen = self.cur.fetchall()
            return last_seen
        except Error as e:
            logging.error(e)
            return 0

    def get_client_list(self, client_id):
        """
            return the client list
        :return: Name , ID
        """
        try:
            self.cur.execute("SELECT ID, Name FROM clients WHERE ID != [?];", client_id)
            client_list = self.cur.fetchall()
            return client_list
        except Error as e:
            logging.error(e)
            return ""

