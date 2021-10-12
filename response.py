
class ResponsePayLoad:
    """
        BaseClass for respones
    """
    def __init__(self, Version):
        self.Version = Version
        self.Code = 0
        self.Payload_size = 0


class Response2000(ResponsePayLoad):
    """
        Accept Registration
    """
    def __init__(self, client_id):
        ResponsePayLoad.__init__(self, 1)
        self.code = 2000
        self.Payload_size = 16
        self.Client_ID = client_id # spoused to be 16 bytes

    def _register_user(self):
        pass


class Response2001(ResponsePayLoad):
    """
        Client list
    """
    def __init__(self, client_id, client_name):
        ResponsePayLoad.__init__(self, 1)
        self.code = 2000
        self.Clist = []
        self.Payload_size = 16
        self.Client_ID = client_id  # spoused to be 16 bytes

    def getMessageListCombo(self, DB):

