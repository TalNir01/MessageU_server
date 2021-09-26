
def read_port_number():
    """
    reading port number from port.info
    :return: port number
    """
    with open("port.info", "r") as port_file:
        try:
            port_str = port_file.readlines()
            port_number = int(port_str)
        except:
            port_number = 0
        port_file.close()
    return port_number
