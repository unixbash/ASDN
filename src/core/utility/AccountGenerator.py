from comms.Communication import executeCommand, executeCommand, waitForTerm
from utility.Util import findBetween
import time

def getEncryptedPass(term, plaintext):
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

    return encryptedPass