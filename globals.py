from standa import Standa
from positioner import Positioner

standa_device = Standa()
positioner_device = Positioner()

command_dict_ids = {'0x0100': standa_device.connect,
                    '0x0101': standa_device.disconnect,
                    '0x0200': (standa_device.move_absolute, float),
                    '0x0201': (standa_device.move_relative, float),
                    '0x0202': (standa_device.set_speed, float),
                    '0x0203': (standa_device.set_acceleration, float),
                    '0x0204': (standa_device.set_deceleration, float),
                    '0x0205': standa_device.set_zero,
                    '0x0206': standa_device.abort,
                    '0x0300': standa_device.get_current_position,
                    # '0x0301': standa_device.get_move_settings,
                    '0x0302': standa_device.get_status}
devices_dict = {'0x01': r'xi-emu:///C:/virtual_motor/virtual_motor_controller_1.bin'}
