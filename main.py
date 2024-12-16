#!/home/expfunc/Downloads/rotationstagecontrol/rotationstagecontrolvenv/bin/python

import UDP_server
import UDP_config
from UDP_packet_handler import UDPPacketHandler
from standa import Standa
from custom_positioner import CustomPositioner
import time


class MainApp:
    """
    The main application class that sets up and runs the UDP server.

    Attributes:
        udp_server (UDPServer): The UDP server instance.
        standa_device (Standa): The Standa device instance.
        custom_positioner_device (CustomPositioner): The custom positioner device instance.
        device_map (dict): A map of device IDs to device instances.
    """

    def __init__(self, udp_config):
        """
        Initializes the MainApp with a UDP configuration.

        Args:
            udp_config (UDPConfig): The UDP configuration instance.
        """
        self.udp_server = UDP_server.UDPServer(udp_config.ip_address, udp_config.port)
        self.standa_device = Standa()
        self.custom_positioner_device = CustomPositioner()
        self.device_map = {'0x01': (self.standa_device, r"xi-emu:///home/expfunc/Downloads/rotationstagecontrol/virtual_motor_controller_1.bin"),
                           'STM32F103C8T6_build_version_1.2': (self.custom_positioner_device, '/dev/ttyACM0'),
                           }

    def start(self):
        """
        Starts the UDP server and begins handling incoming packets.
        """
        self.udp_server.start()
        while True:
            packet, address = self.udp_server.receive_packet()
            print(f"packet:{packet}, address:{address}")
            UDPPacketHandler(self.udp_server).handle_packet(packet, address,
                                                            self.standa_device, self.custom_positioner_device, self.device_map)


# Main execution
# time.sleep(5)
try:
    config = UDP_config.UDPConfig("raspberrypi.local", 50005)
    # config = UDP_config.UDPConfig("127.0.0.1", 50005)
    server = MainApp(config)
    server.start()
except Exception as e:
    print(e)
