#Different SSH command Execution pattern than networking devices
import time
import paramiko
import xmltodict
from paramiko import SSHClient

def executeOnServer(command):
    result = str('')
    try:
        with open("settings/settings.xml") as file:
            settingsDict = xmltodict.parse(file.read())

        host = (settingsDict['settings']['server-details']['host'])
        uname = (settingsDict['settings']['server-details']['uname'])
        pwd = (settingsDict['settings']['server-details']['pwd'])

        file.close()

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=uname, password=pwd, port=22, look_for_keys=False)

        ssh_transp = ssh.get_transport()
        chan = ssh_transp.open_session()
        chan.exec_command(command)

        # Continuous reading of data output
        while True:
            time.sleep(3)
            while chan.recv_ready():
                result += chan.recv(18388)
            while chan.recv_stderr_ready():
                result += chan.recv_stderr(18388)
            if chan.exit_status_ready():
                break
        ssh_transp.close()

        return result.decode('utf-8')
    except Exception as e:
        print(e)
        return False