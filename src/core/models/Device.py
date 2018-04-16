from comms.Communication import establishConnection, establishShell, closeConnection, executeCommand, executeOnServer
from ansible.AnsibleEngine import generateYaml
from settings.GetSettings import Server
from utility.Util import executeSql
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
    vendor="unknown"
    status="unsupported"

    def __init__(self, hostname, address):
        self.address = address
        self.hostname = hostname
        #Add to list of hosts if not present
        self.addAnsibleHost()

    #Add device to the database
    def addToDB(self):
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

        #Generate SQL expression
        args = [id, address, created, customerId, hostname, status, updated, vendor]
        sql = 'INSERT INTO device VALUES (%s)'

        executeSql(sql, args)

    #Check if the device is in the database
    def isInDB(self, address):
        sql = 'SELECT id FROM device WHERE address=%s'
        isPresent = executeSql(sql, [address])

        if isPresent== 1:
            return True
        else:
            return False

    #Add the Device to the list of Ansible hosts if it doesn't exist
    def addAnsibleHost(self):
        server = Server()

        ssh = establishConnection(server.getHost(), server.getUname(), server.getPwd())
        term = establishShell(ssh, False)

        hostToAdd = self.hostname + " ansible_port=22 ansible_host=" + self.address + " ansible_user=" \
                    + server.getUname() + " ansible_ssh_pass=" + server.getPwd()

        listOfHosts = executeOnServer("cat /etc/ansible/hosts")
        # Check if the hosts or duplicate addresses don't currently exist on the server

        if not (self.hostname in listOfHosts and self.address in listOfHosts):
            out = executeCommand(term, 'echo \"' + hostToAdd + '\"' + ' >> /etc/ansible/hosts')

        closeConnection(ssh)

    def getDeviceStatus(self, device):

        parameters = {"temp": "", "mem-usage": "", "cpu-usage": "", "uptime": "",
                      "alarms": "", "interfaces": []}

        # All fullCommand
        commands = Commands()
        commands.genericFunc("show chassis routing-engine")
        commands.genericFunc("show chassis alarms")
        commands.genericFunc("show system alarms")
        commands.genericFunc("show interfaces terse")

        commandOutput = generateYaml(device, commands)

        # Device Temperature
        parameters["temp"] = find(commandOutput, "CPU temperature", False).split(" ")[0] + "C"

        # Memory usage
        parameters["mem-usage"] = find(commandOutput, "Total memory", False).split(" ")[-2] + "%"

        # CPU usage
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