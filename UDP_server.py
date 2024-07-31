import socket


class UDPServer:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        self.socket.bind((self.ip_address, self.port))
        print(f"UDP server started on {self.ip_address}:{self.port}")

    def receive_packet(self):
        data, address = self.socket.recvfrom(1024)
        return data.decode('utf-8'), address

    def send_packet(self, data):
        self.socket.sendto(data, (self.ip_address, self.port))

    def stop(self):
        self.socket.close()
