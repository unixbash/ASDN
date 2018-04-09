class Command:
    allCommandTypes = {"generic":"junos_command", "aggregation":"junos_linkagg",
                       "config":"junos_config", "interfaceL1":"junos_interface",
                       "interfaceL2":"junos_l2_interface", "interfaceL3":"junos_l3_interface",
                       "install":"junos_package", "lldp":"junos_lldp_interface",
                       "routing":"junos_static_route", "services":"junos_system",
                       "account":"junos_user", "vlan":"junos_vlan"}
    commandName = ""
    commandType = ""
    commandArgs = []

    def __init__(self, commandType, commandArgs):
        self.commandName = commandType
        self.commandType = self.allCommandTypes.get(commandType)
        self.commandArgs = commandArgs