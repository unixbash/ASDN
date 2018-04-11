from ansible.AnsibleEngine import generateYaml
from models.Device import Device
from models.Command import Command

args = ["name: ge-0/0/1", "description: interface-access"]
device = Device("srx", "10.10.10.110")
command = Command("generic", "show interfaces terse")

generateYaml(device, command)

#getEncryptedPass(term, "ASDN2018")
#scan("10.10.10.0/24", "ens32")
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#tree = getJSON()
print("done")