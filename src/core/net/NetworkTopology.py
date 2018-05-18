from scapy.all import srp, conf
from scapy.layers.l2 import Ether, ARP
from models.Device import Device
import urllib.request
import time

#check for MAC locally
from settings.GetSettings import Server
from utility.Util import getAllSql, executeSql


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

def deviceAvail(subnet, interval):
    """ Online - can SSH and log into
        Offline - is in the DB and was able to SSH to, but no more
        Warning - can ssh to but has an alarm
        Unconfigured - can ssh but pwd doesn't work
        Unsupported - not a Juniper device
    """

    #Constantly monitor the customer's networks
    while True:

        #Get all devices found on the network:
        server = Server()
        allNetDevices = scan(subnet, server.getUplink())
        allDbDevices = getAllSql("device", ["address"])

        #Update the status of devices that went offline
        for address in allDbDevices:
            if(address[0] not in allNetDevices):
                device = Device("asdn-"+address[0], address[0])
                device.status = "offline"
                device.addToDB(True)

        #Check if a device is operational
        for address, vendor in allNetDevices.items():
            device = Device("asdn-"+address, address)
            device.vendor = vendor

            #Check if the vendor is Juniper
            if "Juniper" in vendor:
                status = device.getDeviceStatus()

                # Get the device configuration
                #device.getDeviceConfig()

                #Check if login is possible
                if not status:
                    status = "unconfigured"
                elif len(status["alarms"]) == 0:
                    status = "warning"
                else:
                    status= "online"
            else:
                status = "unsupported"

            #Assign the status to the device
            device.status = status

            # Add to DB if already there else append
            if device.isInDB():
                device.addToDB(True)
            else:
                device.addToDB(False)

        #Pause the polling for the desired duration
        time.sleep(interval)