from ansible.AnsibleEngine import generateYaml
from settings.GetSettings import Firewall
from utility.Util import executeSql
from models.Device import Device
from models.Commands import Commands

class VPN:

    data = {"id":"","customer_id":"","dh_group":"","ike_al":"","ike_auth":"","ike_life":"","ike_secret":"",
            "ike_version":"","ipsec_al":"","ipsec_enc":"","ipsec_life":"","ipsec_secret":"","net_id":"",
            "private_subnet":"","public_ip":""}

    #Attempt to generate the VPN connection on the internal firewall
    def generateVPN(self, netId):

        try:
            vpnParameters = executeSql("SELECT * FROM vpn WHERE net_id=(%s)", netId)

            firewall = Firewall()
            commands = Commands()
            device = Device(firewall.getHostname(), firewall.getAddress())

            for value, (k2, v2) in zip(vpnParameters, self.data.items()):
                self.data[k2] = value

            genCommands = self.generateCommands(firewall)
            genCommands.append("\n\t\t\t\tcomment: Add VPN - " + str(int(netId) + 100))
            genCommands = ''.join(genCommands)

            commands.configFunc(False, False, None, genCommands)

            result = generateYaml(device, commands)

            #Check if all commands have executed
            if "ok="+len(genCommands) in result:
                return True
            else:
                return False

        except Exception as e:
            print(e)
            return False

    def generateCommands(self, firewall):
        commands = []
        #Set commands
        set="\n\t\t\t\t\t- set "
        interfaces= set + "interfaces "
        routing= set + "routing-options static "
        secZones= set + "security zones security-zone "
        addrBook= set + "security address-book "
        ike= set + "security ike "
        ipsec= set + "security ipsec "

        #Set variables
        st = str(executeSql("SELECT COUNT(id) FROM vpn", [])[0] + 100)

        #Interface, routing and security changes
        commands.append(interfaces + "st0 unit " + st + " family inet address " + firewall.getSubnet() + st +"/24")
        commands.append(routing + "route " + self.data.get("private_subnet") + " next-hop st0." + st)
        commands.append(secZones + "vpn-" + st + " interfaces st0." + st)
        commands.append(addrBook + "book-" + st + " address " + self.data.get("private_subnet") + " " + self.data.get("private_subnet"))
        commands.append(addrBook + "book-" + st + " attach zone " + "vpn-" + st)

        """"dh_group":"","ike_al":"","ike_auth":"","ike_life":"","ike_secret":"",
            "ike_version":"","ipsec_al":"","ipsec_enc":"","ipsec_life":"","ipsec_secret":"","net_id":"",
            "private_subnet":"","public_ip":"""""
        #IKE Configuration
        commands.append(ike + "proposal ike-phase1-proposal authentication-method pre-shared-keys")
        commands.append(ike + "proposal ike-phase1-proposal dh-group " + self.data.get("dh_group"))
        commands.append(ike + "proposal ike-phase1-proposal authentication-algorithm " + self.data.get("ike_auth"))
        commands.append(ike + "proposal ike-phase1-proposal encryption-algorithm " + self.data.get("ike_al"))
        commands.append(ike + "policy ike-phase1-policy mode main")
        commands.append(ike + "policy ike-phase1-policy proposals ike-phase1-proposal")
        commands.append(ike + "policy ike-phase1-policy pre-shared-key ascii-text " + "\"" + self.data.get("ike_secret") + "\"")
        commands.append(ike + "gateway gw-" + st + " external-interface " + firewall.getWanInterface())
        commands.append(ike + "gateway gw-" + st + " ike-policy ike-phase1-policy")
        commands.append(ike + "gateway gw-" + st + " address " + self.data.get("public_ip"))

        #IPSec Configuration
        commands.append(ipsec + "proposal ipsec-phase2-proposal protocol esp")
        commands.append(ipsec + "proposal ipsec-phase2-proposal authentication-algorithm " + self.data.get("ipsec_al"))
        commands.append(ipsec + "proposal ipsec-phase2-proposal encryption-algorithm " + self.data.get("ipsec_enc"))
        commands.append(ipsec + "policy ipsec-phase2-policy proposals ipsec-phase2-proposal")
        commands.append(ipsec + "policy ipsec-phase2-policy perfect-forward-secrecy keys " + self.data.get("dh_group"))
        commands.append(ipsec + "vpn ike-vpn-" + st + " ike gateway gw-" + st)
        commands.append(ipsec + "vpn ike-vpn-" + st + " ike ipsec-policy ipsec-phase2-policy")
        commands.append(ipsec + "vpn ike-vpn-" + st + " bind-interface st0." + st)

        return commands