"""
    DataBase object to control it's API
"""
import sqlite3
from sqlite3 import Error
import logging


class DataBase:
    """DataBase class for managing the DB with easy API """
    logging.basicConfig(filename="data_base_log.log", filemode='w', level=logging.INFO , format='%(name)s # %(levelname)s -> %(message)s')

    def __init__(self):
        """
            Initialize the connection to the DB
        """
        try:
            self.conn = sqlite3.connect("server.db")  # creating the DB
            logging.info("connected to DB")

            success_clients = self._create_clients_db()
            success_message = self._create_messages_db()

            if not (success_clients and success_message):
                self.__del__()
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
            self.conn.execute('''CREATE TABLE clients
                            (ID HEX TEXT PRIMARY KEY NOT NULL,
                            Name VARCHAR(255) NOT NULL,
                            PublicKey HEX TEXT,
                            LastSeen DATE NOT NULL);''')  # create client DB
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
            self.conn.execute('''CREATE TABLE messages
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
        command = "INSERT INTO messages (ID,ToClient,FromClient,Type,Content) values ({}, {}, {}, {}, {});".format(msg_id, dest_id, src_id, msg_type, msg_content)
        try:
            self.conn.execute(command)
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
        command = "INSERT INTO clients (ID,Name,PublicKey,LastSeen) VALUES ({}, {}, {}, {});".format(client_id, client_name, client_public_key, client_last_seen)
        try:
            self.conn.execute(command)
            self.conn.commit()
        except Error as e:
            logging.error(e)

