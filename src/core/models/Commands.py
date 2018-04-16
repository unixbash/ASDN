class Commands:
    allCommandTypes = {"generic":"junos_command", "aggregation":"junos_linkagg",
                       "config":"junos_config", "interfaceL1":"junos_interface",
                       "interfaceL2":"junos_l2_interface", "interfaceL3":"junos_l3_interface",
                       "install":"junos_package", "lldp":"junos_lldp_interface",
                       "routing":"junos_static_route", "services":"junos_system",
                       "account":"junos_user", "vlan":"junos_vlan"}
    commands = [{}]

    #Generic comand
    def genericFunc(self, command):
        type="junos_command"
        select="commands"
        fullCommand = {}
        fullCommand[type] = select + ": " + command

        self.commands.append(fullCommand)

    #Configure interface aggregation
    def aggFunc(self, name, members, lacp):
        type = "junos_linkagg"
        args = []
        args.append(name)
        args.append("members:")
        for member in members:
            args.append("\t- " + member)
        if lacp:
            args.append("lacp: active")
        args.append("device_count: " + len(members))

        self.interL1Func(members,"AE-Interfaces","1g","full",False,True)

        self.fullCommand[type] = args

    #Configuration specific fullCommand
    def configFunc(self, zeroize, rollback, confID, command):
        fullCommand = {}
        type = "junos_config"

        if command is not None:
            select = "lines"
            fullCommand[type] = select + ": " + command

        elif zeroize:
            select = "zeroize"
            fullCommand[type] = select + ": " + command
            print("WARNING - Device zeroized!")

        elif rollback:
            select = "rollback"
            fullCommand[type] = select + ": " + confID

        self.commands.append(fullCommand)

    #Layer 1 interface configuration
    def interL1Func(self, interfaces, description, speed, duplex, delete, agg):
        type = "junos_interface"
        args = []

        for interface in interfaces:
            if agg:
                args.append("aggregate:")
                args.append("\t- name: " + interface)
                args.append("\t"+ "description: " + description)
            else:
                args.append("name: " + interface)
                args.append("description: " + description)

        if(not delete):
            #Below arguements do not have to be set
            if speed is not None and duplex is not None:
                args.append("speed: " + speed)
                args.append("duplex: " + duplex)
        else:
            args.append("state: absent")
        self.fullCommand[type] = args

    def interL2Func(self):
        args = []

        self.fullCommand = args

    def interL3Func(self):
        args = []

        self.fullCommand = args

    def installFunc(self):
        args = []

        self.fullCommand = args

    def lldpFunc(self):
        args = []

        self.fullCommand = args

    def routingFunc(self):
        args = []

        self.fullCommand = args

    def servicesFunc(self):
        args = []

        self.fullCommand = args

    def accountFunc(self):
        args = []

        self.fullCommand = args

    def vlanFunc(self):
        args = []

        self.fullCommand = args
