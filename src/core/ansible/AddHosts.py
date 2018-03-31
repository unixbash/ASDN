from comms.Communication import establishConnection, establishShell, closeConnection, execute_command

def addAnsibleHost(device):
    hostname = "10.10.10.25"
    username = "asdn"
    password = "ASDN2018"

    ssh = establishConnection(hostname, username, password)
    term = establishShell(ssh)

    hostToAdd = device.hostname + " ansible_port=22 ansible_host=" + device.address + " ansible_user=asdn ansible_ssh_pass=ASDN2018"
    listOfHosts = execute_command(term, "cat /etc/ansible/hosts")
    #Check if the hosts or duplicate addresses don't currently exist on the server
    if device.hostname not in listOfHosts and device.address not in listOfHosts:
        out = execute_command(term, 'echo \"' + hostToAdd + '\"' + ' >> /etc/ansible/hosts')

    closeConnection(ssh)