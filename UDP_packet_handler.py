class UDPPacketHandler:
    def __init__(self, udp_server):
        self.udp_server = udp_server

    def handle_packet(self, packet, address):
        # Process the packet and extract commands and parameters
        # For now, just print the packet
        print(f"Received packet from {address}: {packet}")