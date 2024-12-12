from standa import Standa
from custom_positioner import CustomPositioner


class DeviceManager:
    """
    A class to manage and execute commands on various devices.

    Attributes:
        standa_device (Standa): The Standa device instance.
        custom_positioner_device (CustomPositioner): The custom positioner device instance.
        device_map (dict): A map of device IDs to device instances.
    """

    def __init__(self, standa_device, custom_positioner_device, device_map):
        """
        Initializes the DeviceManager with devices and a device map.

        Args:
            standa_device (Standa): The Standa device instance.
            custom_positioner_device (CustomPositioner): The custom positioner device instance.
            device_map (dict): A map of device IDs to device instances.
        """
        self.standa_device = standa_device
        self.custom_positioner_device = custom_positioner_device
        self.device_map = device_map

    def search_devices(self):
        """
        Searches for connected devices and updates the device map.

        Returns:
            tuple: A tuple containing lists of Standa and custom positioner device IDs found.
        """
        self.device_map.clear()

        # search Standa
        standa_ids = Standa.search_for_standa_devices()
        standa_ids = list(map(lambda standa_com: (standa_com[standa_com.rfind('/') + 1:], standa_com), standa_ids))
        if standa_ids:
            for standa_com in standa_ids:
                standa_name, standa_com = standa_com
                self.device_map[standa_name] = (self.standa_device, standa_com)
        else:
            self.device_map['0x01'] = (self.standa_device, r"xi-emu:///home/expfunc/Downloads/rotationstagecontrol/virtual_motor_controller_1.bin")

        # search Custom Positioner
        expected_first_word = "MPSU-Rotator." # Expected first word from the positioner answer on the "info" command
        custom_positioner_ids = []
        for com in CustomPositioner.search_for_positioner_devices():
            com = com[0]
            if com[com.rfind('/') + 1:] not in self.device_map:
                try:
                    temp_custom_positioner = CustomPositioner()
                    temp_custom_positioner.connect(com)
                    temp_custom_positioner.DropMessage() # First message drop. Cause for some reason, it appends data from some buffer, that distorts the first command.
                    custom_positioner_answer = temp_custom_positioner.info().strip().split()
                    if len(custom_positioner_answer) != 0:
                        if custom_positioner_answer[0] == expected_first_word:
                            device_id = custom_positioner_answer[3]
                            custom_positioner_ids.append((device_id, com))
                    temp_custom_positioner.disconnect()
                except Exception as e:
                    pass

        if custom_positioner_ids:
            for id in custom_positioner_ids:
                self.device_map[id[0]] = (self.custom_positioner_device, id[1])

        print(self.device_map)
        return standa_ids, custom_positioner_ids

    def execute_command(self, device_id: str, command_id: str, *param: float):
        """
        Executes a command on a specified device.

        Args:
            device_id (str): The ID of the device to execute the command on.
            command_id (str): The ID of the command to execute.
            *param (float): Optional parameters for the command.

        Returns:
            Any: The result of the command execution.

        Raises:
            ValueError: If the device ID or command ID is unknown.
        """
        device_class = self.device_map.get(device_id)
        if not device_class:
            raise ValueError(f"Unknown device ID: {device_id}")
        else:
            device_class = self.device_map.get(device_id)[0]

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
            param = (self.device_map[device_id][1], )

        if isinstance(command_func, tuple):
            if param:
                try:
                    param = tuple(map(command_func[1], param))
                except ValueError:
                    raise ValueError(f"{param} must be '{command_func[1].__name__}'")
            command_func = command_func[0]

        if not command_func:
            raise ValueError(f"Unknown command ID: {command_id}")

        return command_func(*param)
