from ansible.AnsibleGenerator import generateYaml
from comms.Communication import execute_command
from comms.Communication import getXML
from utility.Util import find

# Test if the system is under load
from models.Command import Command

def getDeviceStatus(device):

    parameters={"temp":"", "mem-usage":"", "cpu-usage":"", "uptime":"",
                "alarms":"", "interfaces":[]}

    tmpCommand = """ 
PLAY [srx] *****************************************************************************************

TASK [generic] *************************************************************************************
ok: [srx]

TASK [debug] ***************************************************************************************
ok: [srx] => {
    "response.stdout_lines": [
        [
            "Routing Engine status:", 
            "    Temperature                 40 degrees C / 104 degrees F", 
            "    CPU temperature             56 degrees C / 132 degrees F", 
            "    Total memory              4096 MB Max   942 MB used ( 23 percent)", 
            "      Control plane memory    2624 MB Max   604 MB used ( 23 percent)", 
            "      Data plane memory       1472 MB Max   324 MB used ( 22 percent)", 
            "    5 sec CPU utilization:", 
            "      User                       9 percent", 
            "      Background                 0 percent", 
            "      Kernel                     6 percent", 
            "      Interrupt                  0 percent", 
            "      Idle                      85 percent", 
            "    Model                          RE-SRX300", 
            "    Serial ID                      CV4416AF0564", 
            "    Start time                     2018-03-29 09:17:21 UTC", 
            "    Uptime                         11 days, 11 hours, 44 minutes", 
            "    Last reboot reason             0x200:normal shutdown", 
            "    Load averages:                 1 minute   5 minute  15 minute", 
            "                                       0.21       0.16       0.10"
        ]
    ]
}

PLAY RECAP *****************************************************************************************
srx                        : ok=2    changed=0    unreachable=0    failed=0   

"""

    #Chassis commands

    #Device Temperature
    chassisCommand = Command("generic", "show chassis routing-engine")
    chassisOutput= generateYaml(device, tmpCommand)
    #parameters["temp"] = find(chassisOutput, "CPU temperature")
    parameters["temp"] = find(tmpCommand, "CPU temperature", False)

    #Memory usage
    #parameters["mem-usage"] = find(chassisOutput, "Total memory")
    parameters["mem-usage"] = find(tmpCommand, "Total memory", False)

    # CPU usage
    # parameters["cpu-usage"] = 100 - int(chassisOutput, "Idle")
    parameters["cpu-usage"] = 100 - int(find(tmpCommand, "Idle", False).split()[0])

    # Uptime
    # parameters["uptime"] = find(chassisOutput, "Uptime")
    parameters["uptime"] = find(tmpCommand, "Uptime", False)


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
    interfaceCommand = Command("generic", "show chassis alarms")
    interfaceOutput = generateYaml(device, interfaceCommand)
    parameters["interfaces"] = find(tmpCommand, "ge-", True)

    return parameters