from comms.Communication import *
from net.SyntaxParser import parseDeviceSyntax

hostname = "10.10.10.110"
username = "asdn"
password = "ASDN2018"

ssh = establishConnection(hostname, username, password)
term = establishShell(ssh)

initialString = "show"

parseDeviceSyntax(term,initialString)

closeConnection(ssh)

#tree = getJSON()
print("done")