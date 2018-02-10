from net.SyntaxParser import *
from comms.Communication import *

hostname = "10.10.10.110"
username = "asdn"
password = "ASDN2018"

ssh = establishConnection(hostname, username, password)
term = establishShell(ssh)

initialString = "show"

parseDeviceSyntax(term,initialString)

closeConnection(ssh)