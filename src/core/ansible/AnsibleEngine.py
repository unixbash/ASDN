import time
import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from utility.Util import uploadFile, replaceTabs, callPy


def generateYaml(device, commands):

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
    no=1
    for commandLIst in commands.commands:
        for commandType, command in commandLIst.items():
            command = replaceTabs(command)
            commandData += dataTemplate.render( type=commandType,
                                                args=command,
                                                num=no) + "\n"
        no+=1

    finalFileData = initData + commandData

    #Execute YAML
    uploadFile(finalFileData, fileName, path)

    command = "export ANSIBLE_HOST_KEY_CHECKING=False " + "&& ansible-playbook " + "/home/asdn/" + fullFileName
    print('\'' + command + '\'')
    yamlFile = Path(fullFileName)

    ftpWait=0
    fileAvail = False
    while not yamlFile.is_file() and ftpWait < 10:
        ftpWait+=1
        time.sleep(1)
        if yamlFile.is_file():
            fileAvail = True

    if fileAvail:
        py2Command = '\'' + command + '\''# launch python2 script using bash
        result = callPy("2.7", "py2Exec", "executeOnServer", [py2Command])
        if "AuthenticationException" in result:
            return False
        else:
            return result
    else:
        return False