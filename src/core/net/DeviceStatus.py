from comms.Communication import send_command
from comms.Communication import getXML

# Test if the system is under load

def getDeviceStatus(term):


    #Device Temperature
    commandOutput = send_command(term, "show chassis routing-engine | display xml")
    deviceStatus = getXML(commandOutput, "Temperature")

    return deviceStatus