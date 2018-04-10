from comms.Communication import execute_command
from utility.Util import readTextFile

class StaticConfig:
    lanInterface = ""
    wanInterface = ""
    tunnelInterface = ""
    untrustZone = ""
    trustZone = ""
    vpnZone = ""

class IKE:
    data = {"name":"", "lifetime-seconds":"", "authentication-method":"",
            "authentication-algorithm":"", "encryption-algorithm":"", "dh-group":"",
            "mode":"", "pre-shared-key":""}
    def __init__(self, term):
        configData = readTextFile("settings/settings.txt")

        #Assign the above values to the ones provided by the settings file
        for param in configData:
            paramName=param.split(":")[0]
            currentParam = param.split(":")[1]
            self.data[paramName] = currentParam

    def sendIKE(self, param, term):
        proposalPrefix = "set security ike proposal"
        execute_command(term, proposalPrefix + " " +
                        self.data["name"]
                        + " " +
                        self.data[param]
                        )

    def applyIKE(self, term):

        for param in self.data:
            self.sendIKE(param, term)
