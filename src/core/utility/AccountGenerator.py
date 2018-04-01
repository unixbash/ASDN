from comms.Communication import execute_command, execute_command, waitForTerm
from utility.Util import findBetween
import time

def getEncryptedPass(term, plaintext):
    execute_command(term, "configure")
    waitForTerm(term, 1, "#")

    execute_command(term, "set system login user test class super-user authentication plain-text-password")
    time.sleep(1)
    execute_command(term, plaintext)
    time.sleep(1)
    execute_command(term, plaintext)

    encryptedPass = findBetween(execute_command(term, "show system login user test"), '"')
    time.sleep(1)

    execute_command(term, "rollback")
    waitForTerm(term, 1, "#")

    execute_command(term, "quit")

    return encryptedPass