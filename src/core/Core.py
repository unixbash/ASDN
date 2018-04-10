from ansible.AddHosts import addAnsibleHost
from ansible.AnsibleGenerator import generateYaml
from comms.Communication import establishConnection, establishShell, closeConnection
from net.DeviceStatus import getDeviceStatus
from net.NetworkTopology import scan
from utility.AccountGenerator import getEncryptedPass
from utility.ConfigFileGenerator import generateConfig
from models.Device import Device
from models.Command import Command
from utility.Util import findBetween

#ssh = establishConnection(hostname, username, password)
#term = establishShell(ssh)

initialString = "show"
args1 = ["name: ge-0/0/1", "description: interface-access"]
device = Device("srx", "10.10.10.110")
command = Command("generic", "show interfaces terse")
tasks=["checkNetConf", "commitAndConfirm"]
#Add Hosts if not present
#getEncryptedPass(term, "ASDN2018")
#addAnsibleHost(device)
#generateYaml(device,command)
#getDeviceStatus(device)
#scan("10.10.10.0/24", "ens32")
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#closeConnection(ssh)

#tree = getJSON()
print("done")