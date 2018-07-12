import threading
import time
from models.Device import Device
from models.Vpn import VPN
from net.DictionaryNester import generateStructure
from net.SyntaxParser import startTree
from settings.GetSettings import Server, Asdn, Firewall
from net.NetworkTopology import scan, deviceAvail
from utility.AccountGenerator import getEncryptedPass
from comms.Communication import executeOnServer, establishConnection, establishShell
from multiprocessing import Process, Value
from utility.Util import executeSql, findBetween

#Perform a scan of all devices every 5min
firewall = Firewall()
interval = 300 #5min scan interval
subnet = firewall.getSubnet() + "0/24"

deviceAvail(subnet, interval)

"""
#Init a thread that continuously scans all networks
if __name__ == '__main__':
    t = threading.Thread(target=deviceAvail, args=(subnet,interval,))
    t.start()

#Init a thread that continuously parses a devices network topology
if __name__ == '__main__':
    ssh = establishConnection(firewall.getAddress(), firewall.getUname(), firewall.getPwd())
    term = establishShell(ssh)
    t = threading.Thread(target=startTree, args=(term,"configuration"))
    result = t.start()
    generateStructure(result)

#Send master pwd and login to the user
userPass = getEncryptedPass()

#Generate VPN - Test Network 1
#Init a thread that continuously parses a devices network topology
if __name__ == '__main__':
    vpn = VPN()
    t = threading.Thread(target=vpn.generateVPN, args=("1"))
    t.start()
"""
