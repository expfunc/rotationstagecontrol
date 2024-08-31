class UDPConfig:
    """
    A class to store UDP server configuration.

    Attributes:
        ip_address (str): The IP address of the server.
        port (int): The port on which the server will operate.
    """

    def __init__(self, ip_address, port):
        """
        Initializes the configuration object with the specified IP address and port.

        Args:
            ip_address (str): The IP address of the server.
            port (int): The port number for the server.
        """
        self.ip_address = ip_address
        self.port = port
