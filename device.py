class Device:
    def __init__(self, id):
        self.id = id
        self.commands = {}

    def add_command(self, name, func):
        self.commands[name] = func

    def execute_command(self, name, *args, **kwargs):
        if name in self.commands:
            return self.commands[name](*args, **kwargs)
        else:
            raise ValueError(f"Command '{name}' not found for device {self.id}")

    def list_commands(self):
        return list(self.commands.keys())
