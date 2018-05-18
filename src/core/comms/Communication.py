import time
import paramiko
import xmltodict
from paramiko import SSHClient, AutoAddPolicy

from settings.GetSettings import Server

def checkConsoleConnection(conAddr,conUsr,pwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(conAddr, 22, conUsr, pwd)
        ssh.close()
        return True
    except:
        return False

def getXML(xml, attr):
    try:
        xml = xml.split("<rpc-reply")[1]
        xml = "<rpc-reply" + xml
        xml = xml.split("</rpc-reply>")[0]
        xml += "</rpc-reply>"
        xmlDict = xmltodict.parse(xml)
        for elem in xmlDict:
            return elem[attr]
    except:
        return "Parsing error."


def executeCommand(term, cmd):
    term.send(cmd + "\n")
    time.sleep(2)
    # bitsize to ensure correct buffer
    output = term.recv(188388)
    # Convert byte output to string
    output = output.decode("utf-8")
    return output

def sendCommand(term, cmd):
    if (cmd == "" or cmd[-1] == "/"):
        helper = "?"
    else:
        helper = " ?"

    term.send(cmd + helper)
    time.sleep(1)
    # bitsize to ensure correct buffer
    output = term.recv(188388)
    # Convert byte output to string
    output = output.decode("utf-8")
    clearScreen(term)
    return output

def clearScreen(term):
    executeCommand(term, '\x18')

def waitForTerm(term, timeToWait, promptToWaitFor):
    timesChecked = 1
    ready = False
    while (not ready):
        time.sleep(timeToWait)
        answer = executeCommand(term, "")
        print(answer)
        if (promptToWaitFor in answer):
            ready = True
        timesChecked = timesChecked + 1

def waitForLogin(term,pswd):
    executeCommand(term, "root")
    time.sleep(2)
    executeCommand(term, pswd)
    time.sleep(2)
    executeCommand(term, "cli")

def establishConnection(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, 22, username, password, look_for_keys=False)
    return ssh

def establishShell(ssh, server):
    term = ssh.invoke_shell()
    if not server:
        #To allow the program to read all output at once
        executeCommand(term, "set cli screen-length 0")
        #To avoid the device cropping the ouptut width, which produces non-standard characters (eg )
        executeCommand(term, "set cli screen-width 1024")
    return term

def closeConnection(connection):
    connection.close()

#Different SSH command Execution pattern than networking devices
def executeOnServer(command):
    result = bytes('', 'utf-8')
    server = Server()
    ssh = establishConnection(server.getAddress(), server.getUname(), server.getPwd())

    connection = ssh.get_transport()
    chan = connection.open_session()
    chan.exec_command(command)

    #Continuous reading of data output
    while True:
        time.sleep(3)
        while chan.recv_ready():
            result += chan.recv(18388)
        while chan.recv_stderr_ready():
            result += chan.recv_stderr(18388)
        if chan.exit_status_ready():
            break

    closeConnection(connection)

    return result.decode('utf-8')