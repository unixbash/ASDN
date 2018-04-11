import time
import datetime
from jinja2 import Environment, FileSystemLoader
from comms.Communication import executeOnServer
from utility.Util import uploadFile



def generateYaml(device, command):

    #Set timestamp
    ts = time.time()
    tStamp = datetime.datetime.fromtimestamp(ts).strftime('-%H-%M-%S_%d-%m-%Y')
    path = "ansible/yaml/generated/"
    fileName = device.hostname + tStamp + ".yaml"
    fullFileName = path + fileName

    #Load template
    env = Environment(loader = FileSystemLoader('ansible/yaml'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('skeleton.yaml')

    file = template.render( host=device.hostname,
                            name=command.commandName,
                            args=command.commandArgs,
                            commType=command.commandType)

    #Execute YAML
    uploadFile(file, fileName, path)
    return executeOnServer("export ANSIBLE_HOST_KEY_CHECKING=False\n" +
                           "ansible-playbook " + "/home/asdn/" + fullFileName)
