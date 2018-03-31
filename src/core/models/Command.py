class Command:
    commandType = ""
    commandAction = ""

    def __init__(self, commandType, commandAction):
        self.commandType = commandType
        self.commandAction = commandAction