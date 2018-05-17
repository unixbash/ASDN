from scapy.all import srp, conf
from scapy.layers.l2 import Ether, ARP
from models.Device import Device
import urllib.request

#check for MAC locally
from utility.Util import getAllSql


def checkMacFile(macAddr):
    macAddr = macAddr[:7]
    try:
        with open('assets/mac_addresses.csv', 'r', encoding='utf-8') as f:
            for line in f:
                comma = line.index(",")
                prefix = line[:comma]
                prefix = prefix.lower()
                if macAddr in prefix:
                    return line[comma + 1:].strip('\n')
        return "N/A"
    except FileNotFoundError:
        return "No Local Record Found"

#check for MAC remotely
def getMacVendor(macAddr):
    try:
        response = urllib.request.urlopen('http://api.macvendors.com/' + macAddr)
        vendor = str (response.read())
        return vendor[2:len(vendor) - 1]  # just cut out quotes from returned string for neatness
    except:
        return checkMacFile(macAddr)  # check locally is there was an error
    return checkMacFile(macAddr)

#Scan the network for devices
def scan(net, interface):
    devices = {}
    conf.verb = 0
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = net),
                    timeout=2, iface=interface, inter=0.1)

    for snd, rcv in ans:
        devices[rcv.sprintf(r"%ARP.psrc%")] = getMacVendor(rcv.sprintf(r"%Ether.src%"))

    return devices

def deviceAvail(devices):
    """ Online - can SSH and log into
        Offline - is in the DB and was able to SSH to, but no more
        Warning - can ssh to but has an alarm
        Unconfigured - can ssh but pwd doesn't work
        Unsupported - not a Juniper device
    """

    # Check if a device went down
    allDevices = getAllSql("device", ["address"])
    for device in allDevices:
        if device[0] not in devices:
            address = device[0]
            currentDevice = Device("asdn-"+address, address)
            currentDevice.status = "offline"
            currentDevice.addToDB(True)

    # for each Juniper device login and get device status
    for address, vendor in devices.items():

        currentDevice = Device("asdn-"+address, address)
        currentDevice.vendor = vendor

        if "Juniper" in vendor:
            status = currentDevice.getDeviceStatus()
            # Get the device configuration
            currentDevice.getDeviceConfig()

            #Check if login is possible
            if not status:
                status = "unconfigured"
            elif len(status["alarms"]) == 0:
                status = "warning"
            else:
                status= "online"
        else:
            status = "unsupported"
        currentDevice.status = status

        # Add to DB if already there else append
        if currentDevice.isInDB(address):
            currentDevice.addToDB(False)
        else:
            currentDevice.addToDB(True)