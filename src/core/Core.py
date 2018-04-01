from ansible.AddHosts import addAnsibleHost
from ansible.AnsibleGenerator import generateYaml
from net.NetworkTopology import scan
from utility.ConfigFileGenerator import generateConfig
from models.Device import Device
from models.Command import Command

hostname = "10.10.10.110"
username = "asdn"
password = "ASDN2018"

#ssh = establishConnection(hostname, username, password)
#term = establishShell(ssh)

initialString = "show"
device = Device("srx", "10.10.10.110")
command = Command("show", "version")
tasks=["checkNetConf", "commitAndConfirm"]
#Add Hosts if not present
#addAnsibleHost(device)
generateYaml(device,command)
#scan("10.10.10.0/24", "ens32")
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#closeConnection(ssh)

#tree = getJSON()
print("done")