from scapy.all import srp, conf
from scapy.layers.l2 import Ether, ARP
import urllib.request

#check for MAC locally
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
        devices[getMacVendor(rcv.sprintf(r"%Ether.src%"))] = rcv.sprintf(r"%ARP.psrc%")
        print (getMacVendor(rcv.sprintf(r"%Ether.src%")) + rcv.sprintf(r" - %Ether.src% - %ARP.psrc%"))

    return devices