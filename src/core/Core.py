from ansible.AnsibleEngine import generateYaml
from models.Device import Device
from models.Commands import Commands

args = ["name: ge-0/0/1", "description: interface-access"]
device = Device("srx", "10.10.10.110")
commands = []

result = device.getDeviceStatus()
#status = device.getDeviceStatus(device)

#getEncryptedPass(term, "ASDN2018")
#scan("10.10.10.0/24", "ens32")
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#tree = getJSON()
print("done")