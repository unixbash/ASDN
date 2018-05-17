from models.Device import Device
from models.Vpn import VPN
from settings.GetSettings import Server, Asdn
from net.NetworkTopology import scan, deviceAvail
from utility.AccountGenerator import getEncryptedPass
from comms.Communication import executeOnServer

#Send master pwd and login
#masterPwd = getEncryptedPass()

#Get default server settings
server = Server()
subnet = "10.10.10.0/24"

#scan the subnet provided
allDevices = scan(subnet, server.getUplink())
print(allDevices)
deviceAvail(allDevices)

#Generate VPN
vpn = VPN()
#vpn.generateVPN("1")

#wait for new network connection
print("API Call")

#scan("10.10.10.0/24", "ens32")
#parseDeviceSyntax(term,initialString)
#generateStructure(parseDeviceSyntax)

#ike = IKE(term)

#tree = getJSON()
print("done")