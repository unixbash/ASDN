import time
import datetime
from jinja2 import Environment, FileSystemLoader
from subprocess import call


def generateYaml(device, command):

    #Set timestamp
    ts = time.time()
    tStamp = datetime.datetime.fromtimestamp(ts).strftime('-%H-%M-%S_%d-%m-%Y')
    fileName = "ansible/yaml/generated/" + device.hostname + tStamp + ".yaml"

    #Load template
    env = Environment(loader = FileSystemLoader('ansible/yaml'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('skeleton.yaml')

    #Render the template
    f = open(fileName, 'w')
    f.write(template.render(host=device.hostname,
                            name=command.commandName,
                            args=command.commandArgs,
                            commType=command.commandType))
    f.close()

    #Execute YAML
    #return call(["ansible-playbook", fileName])