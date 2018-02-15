from comms.Communication import execute_command
from comms.Communication import getXML

# Test if the system is under load

def getDeviceStatus(term):


    #Device Temperature
    commandOutput = execute_command(term, "show chassis routing-engine | display xml")
    deviceStatus = getXML(commandOutput, "Temperature")

    return deviceStatus