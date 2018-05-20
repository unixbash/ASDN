import time
import datetime
from jinja2 import Environment, FileSystemLoader
from utility.Util import uploadFile, replaceTabsWithSpaces, callPy


def generateYaml(device, commands):

    # Add to list of hosts if not present
    device.addAnsibleHost()
    #Set timestamp
    ts = time.time()
    tStamp = datetime.datetime.fromtimestamp(ts).strftime('-%H-%M-%S_%d-%m-%Y')
    path = "ansible/yaml/generated/"
    fileName = device.hostname + tStamp + ".yaml"
    fullFileName = path + fileName

    #Load templates
    env = Environment(loader = FileSystemLoader('ansible/yaml'), trim_blocks=True, lstrip_blocks=True)
    initTemplate = env.get_template('initTemplate.yaml')
    dataTemplate = env.get_template('commandTemplate.yaml')

    initData = initTemplate.render( host=device.hostname)
    commandData = "\n"

    #Generate configuration file from all given fullCommand
    no=0
    for commandLIst in commands.commands:
        for commandType, command in commandLIst.items():
            command = replaceTabsWithSpaces(command)
            commandData += dataTemplate.render( type=commandType,
                                                args=command,
                                                num=no) + "\n"
        no+=1

    finalFileData = initData + commandData

    #Execute YAML
    fileAvail =  uploadFile(finalFileData, fileName, path)
    command = "ansible-playbook " + "ansible/yaml/generated/" + fileName

    if fileAvail:
        result = callPy("2.7", "py2Exec", "executeOnServer", [command])
        if not result:
            print("Python2 script AuthenticationException")
            return False
        else:
            return str(result)
    else:
        print("Ansible Execution Failed")
        return False