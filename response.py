import uttil
"""
class Respone:

    def __init__(self):
"""



class ResponsePayLoad:
    """
        BaseClass for respones
    """
    def __init__(self, Version):
        self.Version = Version


class Response2000(ResponsePayLoad):
    """
        Accept Registration
    """
    def __init__(self, client_id, client_name, DB):
        ResponsePayLoad.__init__(self, 1)
        self.DB = DB
        self.code = 2000
        self.Payload_size = 16
        self.Client_name = client_name
        self.Client_ID = uttil.UUID() # spoused to be 16 bytes

    def _register_user(self):
        self.DB.insert_clients_to_db(self.Client_ID, self.Client_name, 0, "")


class Response2001(ResponsePayLoad):
    """
        Client list
    """
    def __init__(self, client_id, DB):
        """
            Init Function for response with code 2001
        :param client_id:
        :param DB:
        """
        ResponsePayLoad.__init__(self, 1)
        self.DB = DB
        self.code = 2001
        self.Client_ID = client_id  # spoused to be 16 bytes
        self.Clist = self._client_list()
        self.Payload_size = (16 + 255)*len(self.Clist)
        self.Payload = self._string_format_list()

    def _client_list(self):
        return self.DB.get_client_list(self.Client_ID) # get client list from Data Base

    def _string_format_list(self): # NOT FINISHED
        output = ""
        for i in self.Clist:
            output += "{}{}".format(str(i[0]), str(i[1])) # <id:name>

        return output


class Response2002(ResponsePayLoad):
    """
        Response for 2002 code
    """
    def __init__(self, DB, client_id):
        ResponsePayLoad.__init__(self, 1)
        self.code = 2002
        self.client_id = client_id
        self.DB = DB
        self.Payload_size = 176
        self.payload = "{}{}".format(str(self.client_id), str(self._get_pub_key()))

    def _get_pub_key(self):
        self.DB.get_public_key(self.client_id)  # ret public key


class Response2003(ResponsePayLoad):
    """
        Response for 2003 code, approve a message was sent
    """
    def __init__(self, DB, client_id):
        ResponsePayLoad.__init__(self, 1)
        self.code = 2003
        self.dst_client_id = client_id
        self.DB = DB
        self.Payload_size = 16
        self.payload = "{}{}".format(str(self.dst_client_id), str(uttil.MSG_UUID()))

