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


def send_command(term, cmd):
    term.send(cmd + "\n")
    time.sleep(3)
    # bitsize to ensure correct buffer
    output = term.recv(188388)
    # Convert byte output to string
    output = output.decode("utf-8")
    return output

def waitForTerm(term, timeToWait, promptToWaitFor):
    timesChecked = 1
    ready = False
    while (not ready):
        time.sleep(timeToWait)
        answer = send_command(term, "")
        print(answer)
        if (promptToWaitFor in answer):
            ready = True
        timesChecked = timesChecked + 1

def waitForLogin(term,pswd):
    send_command(term, "root")
    time.sleep(2)
    send_command(term, pswd)
    time.sleep(2)
    send_command(term, "cli")

def establishConnection(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, 22, username, password)
    return ssh

def establishShell(ssh):
    term = ssh.invoke_shell()
    #To allow the program to read all output at once
    send_command(term, "set cli screen-length 0")
    #To avoid the device cropping the ouptut width, which produces non-standard characters (eg )
    send_command(term, "set cli screen-width 1024")
    return term

def closeConnection(connection):
    connection.close()