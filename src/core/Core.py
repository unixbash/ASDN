from ansible.AnsibleGenerator import addAnsibleHost
from utility.ConfigFileGenerator import generateConfig

hostname = "10.10.10.110"
username = "asdn"
password = "ASDN2018"

#ssh = establishConnection(hostname, username, password)
#term = establishShell(ssh)

initialString = "show"
hosts=["10.10.10.110"]
tasks=["checkNetConf", "commitAndConfirm"]
#Add Hosts if not present
addAnsibleHost(hosts)
generateConfig(hosts,tasks)
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#closeConnection(ssh)

#tree = getJSON()
print("done")