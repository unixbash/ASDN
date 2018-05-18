import threading
import time
from models.Device import Device
from models.Vpn import VPN
from settings.GetSettings import Server, Asdn
from net.NetworkTopology import scan, deviceAvail
from utility.AccountGenerator import getEncryptedPass
from comms.Communication import executeOnServer
from multiprocessing import Process, Value
from utility.Util import executeSql, findBetween

#Perform a scan of all devices every 5min
interval = 300
subnet = "10.10.10.0/24"
#Init a thread that continuously scans all networks
if __name__ == '__main__':
    t = threading.Thread(target=deviceAvail, args=(subnet,interval,))
    t.start()

#Send master pwd and login
#masterPwd = getEncryptedPass()
while True:
    print("hello")
    time.sleep(30)

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