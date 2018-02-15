from comms.Communication import send_command
from net.DictionaryNester import generateStructure
from utility.LinkedList import *
from utility.Util import *

#Command class
class Command:
    value = ""
    isExecutable = False

    def __init__(self, value):
        self.value = value
        self.isExecutable = False

#Global Variables
data = {}
commandTree = UnorderedList()

#Gets formatted output from the device
def getNode(term, initialString):
    commandOutput = send_command(term, initialString)
    leafs = []
    parsedOutput = commandOutput.splitlines()
    for leaf in parsedOutput:
        if not ("?" in leaf
                or "Possible" in leaf
                or "|" in leaf
                or '^' in leaf
                or '<' in leaf
                or 'syntax' in leaf
                or 'missing' in leaf
                or 'valid' in leaf
                or not isAscii(leaf)
                or len(leaf) < 1):
                commandValue = leaf.strip().split(" ")[0].rstrip()
                leafs.append(Command(commandValue))

        if("<[Enter]>" in leaf):
            setExecutable(initialString)

        #Check if complete
        if(">" in leaf):
            if (leafs):
                leafs.pop()
            return leafs

def setExecutable(command):
    currentCommand = data[command]
    currentCommand.isExecutable = True
    data[command] = currentCommand

#Start the tree generation process
def startTree(term, initialString):
    leafs = list(filter(None, getNode(term, initialString)))

    for i in range(len(leafs)):
         data[leafs[i].value]=leafs[i]
         makeTree(term, Command(initialString + " " + leafs[i].value))

def makeTree(term, command):
    leafs = list(filter(None, getNode(term, command.value)))

    if len(leafs) < 1:
        return command
    else:
        for i in range(len(leafs)):
            currentCommand = Command(command.value + " " + leafs[i].value)
            data[currentCommand.value]=currentCommand
            newCommand = makeTree(term, currentCommand)
            commandTree.add(newCommand)
            data[newCommand.value]=newCommand
            print(newCommand.value + ": " + str(newCommand.isExecutable))

        commandTree.clear()
        return command


def parseDeviceSyntax(term, initialString):

    startTree(term, initialString)
    generateStructure(dictToList(data))