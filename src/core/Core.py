from models.Device import Device
from models.Vpn import VPN
from settings.GetSettings import Server
from net.NetworkTopology import scan

#Get default server settings
server = Server()

#Generate VPN
vpn = VPN()
vpn.generateVPN("1")

#wait for new network connection
print("API Call")
subnet = "10.10.10.0/24"

#scan the subnet provided
allDevices = scan(subnet, server.getUplink())

#for each Juniper device login and get device status
for vendor, address in allDevices:
    currentDevice=Device(address)
    currentDevice.vendor = vendor

    if "Juniper" in vendor:
        currentDevice.status = currentDevice.getDeviceStatus()

    # Add to DB if not already there
    if not currentDevice.isInDB(address):
        currentDevice.addToDB()




#after getting the device status add it to the DB as online

#if login fails add it to the DB as warning

#add non-Juniper devices as unsuported

#

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