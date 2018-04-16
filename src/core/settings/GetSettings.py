import xmltodict

#Connection to the Database
class Database:
    __host=""
    __port=""
    __db=""
    __uname=""
    __pwd=""

    def __init__(self):
        try:
            with open("settings/settings.xml") as file:
                settingsDict = xmltodict.parse(file.read())

            self.__host = (settingsDict['settings']['db-details']['host'])
            self.__port = (settingsDict['settings']['db-details']['port'])
            self.__db = (settingsDict['settings']['db-details']['db'])
            self.__uname = (settingsDict['settings']['db-details']['uname'])
            self.__pwd = (settingsDict['settings']['db-details']['pwd'])

            file.close()
        except Exception as e:
            print(e)

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def getDb(self):
        return self.__db

    def getUname(self):
        return self.__uname

    def getPwd(self):
        return self.__pwd

class Server:
    __host = ""
    __uname = ""
    __pwd = ""
    __uplink = ""

    def __init__(self):
        try:
            with open("settings/settings.xml") as file:
                settingsDict = xmltodict.parse(file.read())

            self.__host = (settingsDict['settings']['server-details']['host'])
            self.__uname = (settingsDict['settings']['server-details']['uname'])
            self.__pwd = (settingsDict['settings']['server-details']['pwd'])
            self.__uplink = (settingsDict['settings']['server-details']['uplink'])

            file.close()
        except Exception as e:
            print(e)

    def getHost(self):
        return self.__host

    def getUname(self):
        return self.__uname

    def getPwd(self):
        return self.__pwd

    def getUplink(self):
        return self.__uplink

class FtpServer:
    __host = ""
    __uname = ""
    __pwd = ""

    def __init__(self):
        try:
            with open("settings/settings.xml") as file:
                settingsDict = xmltodict.parse(file.read())

            self.__host = (settingsDict['settings']['ftp-details']['host'])
            self.__uname = (settingsDict['settings']['ftp-details']['uname'])
            self.__pwd = (settingsDict['settings']['ftp-details']['pwd'])

            file.close()
        except Exception as e:
            print(e)

    def getHost(self):
        return self.__host

    def getUname(self):
        return self.__uname

    def getPwd(self):
        return self.__pwd

class Firewall:
    __hostname = ""
    __uname = ""
    __pwd = ""

    def __init__(self):
        try:
            with open("settings/settings.xml") as file:
                settingsDict = xmltodict.parse(file.read())

            self.__hostname = (settingsDict['settings']['firewall-details']['hostname'])
            self.__address = (settingsDict['settings']['firewall-details']['address'])
            self.__lanInterface = (settingsDict['settings']['firewall-details']['lan-interface'])
            self.__wanInterface = (settingsDict['settings']['firewall-details']['wan-interface'])
            self.__subnet = (settingsDict['settings']['firewall-details']['subnet'])
            self.__publicIp = (settingsDict['settings']['firewall-details']['publicIP'])

            file.close()
        except Exception as e:
            print(e)

    def getHostname(self):
        return self.__hostname

    def getAddress(self):
        return self.__address

    def getLanInterface(self):
        return self.__lanInterface

    def getWanInterface(self):
        return self.__wanInterface

    def getSubnet(self):
        return self.__subnet

    def getPublicIp(self):
        return self.__publicIp

