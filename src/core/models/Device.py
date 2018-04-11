from comms.Communication import establishConnection, establishShell, closeConnection, executeCommand
from settings.GetSettings import Server
from utility.Util import executeSql
import uuid
import datetime
import time

class Device:
    id=""
    hostname = ""
    address = ""
    vendor="unknown"

    def __init__(self, hostname, address):
        self.hostname = hostname
        self.address = address

        #Add to DB if not already there
        if not self.isInDB(address):
            self.addToDB()

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

        #Generate SQL expression
        args = [id, address, created, customerId, hostname, updated, vendor]
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

        listOfHosts = executeCommand(term, "cat /etc/ansible/hosts")
        # Check if the hosts or duplicate addresses don't currently exist on the server

        if self.hostname not in listOfHosts and self.address not in listOfHosts:
            out = executeCommand(term, 'echo \"' + hostToAdd + '\"' + ' >> /etc/ansible/hosts')

        closeConnection(ssh)