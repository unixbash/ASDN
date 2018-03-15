from comms.Communication import *
from net.SyntaxParser import parseDeviceSyntax
from net.DictionaryNester import generateStructure
from net.VpnGenerator import IKE
from utility.ConfigFileGenerator import generateConfig

hostname = "10.10.10.110"
username = "asdn"
password = "ASDN2018"

#ssh = establishConnection(hostname, username, password)
#term = establishShell(ssh)

initialString = "show"
hosts=["SRX300"]
tasks=["checkNetConf", "commitAndConfirm"]
generateConfig(hosts,tasks )
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#closeConnection(ssh)

#tree = getJSON()
print("done")