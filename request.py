
class Response:
    """
        BaseClass for respones
    """
    def __init__(self, Version):
        self.Version = Version
        self.Code = 0
        self.Payload_size = 0


class Respones2000(Response):
    """
        Accept Registration
    """
    def __init__(self, client_id):
        Response.__init__(self, 1)
        self.code = 2000
        self.Payload_size = 16
        self.Client_ID = client_id # spoused to be 16 bytes


class Response2001(Response):
    """
        Client list
    """
    def __init__(self, client_id, client_name):
        Response.__init__(self, 1)
        self.code = 2000
        self.Payload_size = 16
        self.Client_ID = client_id  # spoused to be 16 bytes