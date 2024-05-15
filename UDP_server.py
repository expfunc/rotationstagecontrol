import socket

UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 5005     # Port to listen on

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
sock.bind((UDP_IP, UDP_PORT))  # Bind socket to IP and port

while True:
    data, addr = sock.recvfrom(1024)  # Receive up to 1024 bytes
    print("received message:", data)