import paramiko

from comms.Communication import executeCommand, waitForTerm, closeConnection, checkConsoleConnection, \
    establishConnection, establishShell
from settings.GetSettings import Asdn, Firewall
from utility.Util import findBetween
import time

def getEncryptedPass():
    asdn = Asdn()
    firewall = Firewall()
    plaintext = asdn.getPwd()
    # Connect to the console server
    deviceAvailable = checkConsoleConnection(firewall.getAddress(), 22, firewall.getUname(), firewall.getPwd())

    if deviceAvailable:
        ssh = establishConnection(firewall.getAddress(), 22, firewall.getUname(), firewall.getPwd())
        term = establishShell(ssh, False)

        waitForTerm(term, 1, ">")
        executeCommand(term, "configure")
        waitForTerm(term, 1, "#")

        executeCommand(term, "set system login user test class super-user authentication plain-text-password")
        time.sleep(1)
        executeCommand(term, plaintext)
        time.sleep(1)
        executeCommand(term, plaintext)

        encryptedPass = findBetween(executeCommand(term, "show system login user test"), '"')
        time.sleep(1)

        executeCommand(term, "rollback")
        waitForTerm(term, 1, "#")

        executeCommand(term, "quit")

        closeConnection(ssh)

        return encryptedPass
    else:
        False