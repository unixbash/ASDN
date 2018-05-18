#Different SSH command Execution pattern than networking devices
import xmltodict
import subprocess

def executeOnServer(command):
    result = str('')
    try:
        with open("settings/settings.xml") as file:
            settingsDict = xmltodict.parse(file.read())
        host = (settingsDict['settings']['server-details']['address'])
        uname = (settingsDict['settings']['server-details']['uname'])
        pwd = (settingsDict['settings']['server-details']['pwd'])
        file.close()

        command = command.split(' ')
        result += subprocess.check_output([command[0], command[1]])

        return result.decode('utf-8')

    except Exception as e:
        print(e)
        return "Could not execute ansible-playbook - " + str(e)