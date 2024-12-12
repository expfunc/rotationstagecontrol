import socket


class UDPServer:
    """
    A class to manage a UDP server for receiving and sending packets.

    Attributes:
        ip_address (str): The IP address of the server.
        port (int): The port on which the server operates.
        socket (socket.socket): The UDP socket for communication.
    """

    def __init__(self, ip_address, port):
        """
        Initializes the UDP server with the specified IP address and port.

        Args:
            ip_address (str): The IP address of the server.
            port (int): The port number for the server.
        """
        self.ip_address = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        """
        Starts the UDP server by binding it to the IP address and port.
        """
        self.socket.bind((self.ip_address, self.port))
        print(f"UDP server started on {self.ip_address}:{self.port}")

    def receive_packet(self):
        """
        Receives a packet from the UDP socket.

        Returns:
            tuple: The received data as a string and the address of the sender.
        """
        data, address = self.socket.recvfrom(1024)
        return data.decode('utf-8'), address

    def send_packet(self, data):
        """
        Sends a packet of data to the client.

        Args:
            data (str): The data to send.
        """
        print(f"Send packet to {self.ip_address}, {self.port}: {data}")
        self.socket.sendto(data, (self.ip_address, self.port))

    def stop(self):
        """
        Stops the UDP server by closing the socket.
        """
        self.socket.close()
