from comms.Communication import establishConnection, establishShell, closeConnection, executeCommand, executeOnServer, \
    checkConsoleConnection, waitForTerm
from ansible.AnsibleEngine import generateYaml
from settings.GetSettings import Server, Asdn
from utility.Util import executeSql, outputTrim, findBetween
from utility.Util import find
import uuid
import datetime
import time

# Test if the system is under load
from models.Commands import Commands

class Device:
    id=""
    hostname = ""
    address = ""
    vendor = "unknown"
    status = "unsupported"
    config = "null"
    configOld = "null"
    latestOS = "N/A"

    def __init__(self, hostname, address):
        self.address = address
        self.hostname = hostname

    #Add device to the database
    def addToDB(self, update):
        #Generate device details
        ts = time.time()
        timeSt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        id = str(uuid.uuid4())
        address = self.address
        created = timeSt
        customerId = "TMP"
        hostname = self.hostname
        updated = timeSt
        vendor=self.vendor
        status = self.status
        config = self.config
        configOld = self.configOld
        latestOS = self.latestOS

        #Generate SQL expression
        args = [id, address, config, configOld, created, customerId, hostname, latestOS, status, updated, vendor]
        if update:
            sql = 'SELECT id FROM device WHERE address=(%s)'
            args[0] = executeSql(sql, [address])[0]

            sql = 'DELETE FROM device WHERE address=(%s)'
            executeSql(sql, [address])

            sql = 'INSERT INTO device VALUES (%s)'
            executeSql(sql, args)
        else:
            sql = 'INSERT INTO device VALUES (%s)'
            executeSql(sql, args)

    #Check if the device is in the database
    def isInDB(self):
        sql = 'SELECT id FROM device WHERE address=(%s)'
        isPresent = executeSql(sql, [self.address])

        #The id should be a randomly generated 36 char value
        if isPresent is None:
            return False
        else:
            return True

    #Add the Device to the list of Ansible hosts if it doesn't exist
    def addAnsibleHost(self):
        server = Server()

        ssh = establishConnection(server.getAddress(), server.getUname(), server.getPwd())
        term = establishShell(ssh, False)

        hostToAdd = self.hostname + " ansible_port=22 ansible_host=" + self.address + " ansible_user=" \
                    + server.getUname() + " ansible_ssh_pass=" + server.getPwd()

        listOfHosts = executeOnServer("cat /etc/ansible/hosts")
        # Check if the hosts or duplicate addresses don't currently exist on the server

        if not (self.hostname in listOfHosts and self.address in listOfHosts):
            out = executeCommand(term, 'echo \"' + hostToAdd + '\"' + ' >> /etc/ansible/hosts')

        closeConnection(ssh)

    def getDeviceStatus(self):

        parameters = {"temp": "", "mem-usage": "", "cpu-usage": "", "uptime": "",
                      "alarms": "", "interfaces": []}

        # All fullCommand
        commands = Commands()
        commands.genericFunc("show chassis routing-engine")
        commands.genericFunc("show chassis alarms")
        commands.genericFunc("show system alarms")
        commands.genericFunc("show interfaces terse")

        commandOutput = generateYaml(self, commands)

        print(commandOutput)

        if commandOutput:
            # Device Temperature
            parameters["temp"] = find(commandOutput, "CPU temperature", False).split(" ")[0] + "C"

            # Memory usage
            try:
                parameters["mem-usage"] = find(commandOutput, "Total memory", False).split(" ")[-2] + "%"
            except:
                parameters["mem-usage"] = find(commandOutput, "Memory utilization", False).split(" ")[0] + "%"

            # CPU usage
            print(str(100 - int(find(commandOutput, "Idle", False).split()[0])) + "%")
            parameters["cpu-usage"] = str(100 - int(find(commandOutput, "Idle", False).split()[0])) + "%"

            # Uptime
            parameters["uptime"] = find(commandOutput, "Uptime", False)

            # Alarms
            if "No alarms" in commandOutput and "No alarms" in commandOutput:
                parameters["alarms"] = "No alarms"
            else:
                parameters["alarms"] = commandOutput

            # Get interface statistics
            parameters["interfaces"] = find(commandOutput, "ge-", True)

            return parameters

        else:
            return False

    #Get current, active device configuration
    def getDeviceConfig(self):
        deviceDetails = Asdn()
        deviceAvailable = checkConsoleConnection(self.address, deviceDetails.getUname(), deviceDetails.getPwd())

        if deviceAvailable:
            ssh = establishConnection(self.address, deviceDetails.getUname(), deviceDetails.getPwd())
            term = establishShell(ssh, False)
            waitForTerm(term, 3, ">")
            current = "show configuration"
            prev = "show system rollback 1"
            config = outputTrim(executeCommand(term, current), current)
            waitForTerm(term, 1, ">")
            prevConfig = outputTrim(executeCommand(term, prev), prev)

            closeConnection(ssh)

            self.config = config
            self.configOld = prevConfig
        else:
            self.config = "Configuration not reachable."
            self.configOld = "Configuration not reachable."

    def configChangeDeltas(self):
        result = {"cpu":"", "memory":"", "interfaces":"", "reachable-roots":"",
                  "reachable-vlans":"", "wan-pps":"", "load":"", "wan-latency":""}