from comms.Communication import establishConnection, establishShell, closeConnection, execute_command

def addAnsibleHost(hostNames):
    hostname = "10.10.10.25"
    username = "asdn"
    password = "ASDN2018"

    ssh = establishConnection(hostname, username, password)
    term = establishShell(ssh)

    for hostName in hostNames:
        listOfHosts = execute_command(term, "cat /etc/ansible/hosts")
        if hostName not in listOfHosts:
            out = execute_command(term, 'echo \"' + hostName + '\"' + '>>/etc/ansible/hosts')
            print(out)

    closeConnection(ssh)