import time
import datetime

from utility.Util import writeTextFile
from config.ConfigurationTasks import Tasks

def generateConfig(hostnames, taskList):
    for host in hostnames:

        ts = time.time()
        tStamp = datetime.datetime.fromtimestamp(ts).strftime('-%H-%M-%S_%d-%m-%Y')
        fileName = host + tStamp

        #Initiate the configuration file
        configuration = ["---"]

        #Generate the name of the batch automation process
        configuration.append("- name: " + host + tStamp)

        #Set target host
        configuration.append("  hosts: " + host)

        #Set the required roles
        configuration.append("  roles: ")
        configuration.append("    - Juniper.junos")

        #Set connection parameters
        configuration.append("  connection: local")
        configuration.append("  gather_facts: no")

        #Set configuration tasks
        allTasks = Tasks(taskList, host)
        configuration.append("  tasks:")
        configuration.append("\n".join(allTasks.get__generatedConfig()))

        #Generate the configuration File
        writeTextFile("ansible/" + fileName,  ".yaml", ("\n".join(configuration)))