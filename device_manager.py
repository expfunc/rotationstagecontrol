from standa import Standa
from custom_positioner import CustomPositioner


class DeviceManager:
    def __init__(self, standa_device: Standa = Standa, custom_positioner_device: CustomPositioner = CustomPositioner):
        self.standa_device = standa_device
        self.custom_positioner_device = custom_positioner_device
        self.device_map = {'0x01': self.standa_device, 'STM32F103C8T6 build version 1.2': self.custom_positioner_device}

    def search_devices(self):
        self.device_map.clear()

        # search Standa
        standa_ids = Standa.search_for_standa_devices()
        if standa_ids:
            for id in standa_ids:
                id = id[id.rfind('/') + 1:]
                self.device_map[id] = self.standa_device
        else:
            self.device_map['0x01'] = self.standa_device

        # search Custom Positioner
        custom_positioner_ids = []
        for com in CustomPositioner.search_for_positioner_devices():
            com = com[0]
            temp_custom_positioner = CustomPositioner()
            temp_custom_positioner.connect(com)
            custom_positioner_ids.append(temp_custom_positioner.info().strip().replace('\n', ' '))
            temp_custom_positioner.disconnect()

        if custom_positioner_ids:
            for id in custom_positioner_ids:
                self.device_map[id] = self.custom_positioner_device

        return standa_ids, custom_positioner_ids

    def execute_command(self, device_id: str, command_id: str, *param: float):
        device_class = self.device_map.get(device_id)
        if not device_class:
            raise ValueError(f"Unknown device ID: {device_id}")

        command_map = {
            "0x0100": device_class.connect,
            "0x0101": device_class.disconnect,
            "0x0200": (device_class.move_absolute, float),
            "0x0201": (device_class.move_relative, float),
            "0x0202": (device_class.set_speed, float),
            "0x0203": (device_class.set_acceleration, float),
            "0x0204": (device_class.set_deceleration, float),
            "0x0205": device_class.set_zero,
            "0x0206": device_class.abort,
            "0x0300": device_class.get_position,
            "0x0301": device_class.get_move_settings,
            "0x0302": device_class.get_status,
            "0x0303": device_class.info
        }

        command_func = command_map.get(command_id)
        if command_id == '0x0100':
            if isinstance(device_class, Standa):
                if device_id == '0x01':
                    param = (r"xi-emu:///C:\virtual_motor\virtual_motor_controller_1.bin", )
                else:
                    param = (r'xi-com:///dev/ximc/' + device_id, )
            elif isinstance(device_class, CustomPositioner):
                param = (device_id,)

        if isinstance(command_func, tuple):
            if param:
                param = (command_func[1](param[0]), )
            command_func = command_func[0]

        if not command_func:
            raise ValueError(f"Unknown command ID: {command_id}")

        return command_func(*param)
