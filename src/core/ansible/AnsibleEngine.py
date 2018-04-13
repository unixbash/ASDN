import time
import datetime
from jinja2 import Environment, FileSystemLoader
from comms.Communication import executeOnServer
from utility.Util import uploadFile



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
            commandData += dataTemplate.render( type=commandType,
                                                args=command,
                                                num=no) + "\n"
        no+=1

    finalFileData = initData + commandData

    #Execute YAML
    uploadFile(finalFileData, fileName, path)
    return executeOnServer("export ANSIBLE_HOST_KEY_CHECKING=False\n" +
                           "ansible-playbook " + "/home/asdn/" + fullFileName)
