import time
import paramiko
import xmltodict

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


def execute_command(term, cmd):
    term.send(cmd + "\n")
    time.sleep(3)
    # bitsize to ensure correct buffer
    output = term.recv(188388)
    # Convert byte output to string
    output = output.decode("utf-8")
    return output

def send_command(term, cmd):
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
    execute_command(term, '\x18')

def waitForTerm(term, timeToWait, promptToWaitFor):
    timesChecked = 1
    ready = False
    while (not ready):
        time.sleep(timeToWait)
        answer = execute_command(term, "")
        print(answer)
        if (promptToWaitFor in answer):
            ready = True
        timesChecked = timesChecked + 1

def waitForLogin(term,pswd):
    execute_command(term, "root")
    time.sleep(2)
    execute_command(term, pswd)
    time.sleep(2)
    execute_command(term, "cli")

def establishConnection(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, 22, username, password)
    return ssh

def establishShell(ssh):
    term = ssh.invoke_shell()
    #To allow the program to read all output at once
    execute_command(term, "set cli screen-length 0")
    #To avoid the device cropping the ouptut width, which produces non-standard characters (eg )
    execute_command(term, "set cli screen-width 1024")
    return term

def closeConnection(connection):
    connection.close()