from ansible.AnsibleEngine import generateYaml
from comms.Communication import executeCommand
from comms.Communication import getXML
from utility.Util import find

# Test if the system is under load
from models.Command import Command

def getDeviceStatus(device):

    parameters={"temp":"", "mem-usage":"", "cpu-usage":"", "uptime":"",
                "alarms":"", "interfaces":[]}

    #Chassis commands
    chassisCommand = Command("generic", "show chassis routing-engine")
    chassisOutput = generateYaml(device, chassisCommand)

    #Device Temperature
    parameters["temp"] = find(chassisOutput, "CPU temperature", False)

    #Memory usage
    parameters["mem-usage"] = find(chassisOutput, "Total memory", False)

    # CPU usage
    parameters["cpu-usage"] = 100 - int(find(chassisOutput, "Idle", False).split()[0])

    # Uptime
    parameters["uptime"] = find(chassisOutput, "Uptime", False)

    #Alarms commands
    chassisAlarmCommand = Command("generic", "show chassis alarms")
    systemAlarmCommand = Command("generic", "show system alarms")
    chassisAlarmOutput = generateYaml(device, chassisAlarmCommand)
    systemAlarmOutput = generateYaml(device, systemAlarmCommand)

    if "No alarms" in chassisAlarmOutput and "No alarms" in systemAlarmCommand:
        parameters["alarms"] = "No alarms"
    else:
        parameters["alarms"] += chassisAlarmOutput + systemAlarmOutput

    #Get interface statistics
    interfaceCommand = Command("generic", "show interfaces terse")
    interfaceOutput = generateYaml(device, interfaceCommand)
    parameters["interfaces"] = find(interfaceOutput, "ge-", True)

    return parameters