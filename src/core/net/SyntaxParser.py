from comms.Communication import send_command
from net.DictionaryNester import generateStructure
from utility.LinkedList import *

#Command class
class Command:
    index = 0
    value = ""

    def __init__(self, index, value):
        self.index = index
        self.value = value

#Global Variables
data = []
commandTree = UnorderedList()

#Gets formatted output from the device
def getNode(term, initialString):
    commandOutput = send_command(term, initialString)
    leafs = []
    parsedOutput = commandOutput.splitlines()
    for leaf in parsedOutput:
        if not ("show" in leaf or "Possible" in leaf):
            leafs.append(leaf.strip().split(" ")[0].rstrip())
            #Check if valid
            if ('<[Enter]>' in leaf
                    or "|" in leaf
                    or '^' in leaf
                    or 'syntax' in leaf):
                if(leafs):
                    leafs.pop()

            #Check if complete
            if(">" in leaf):
                if (leafs):
                    leafs.pop()
                return leafs

#Start the tree generation process
def startTree(term, initialString):
    leafs = list(filter(None, getNode(term, initialString + " ?")))

    for i in range(len(leafs)):
        makeTree(term, Command(i, initialString + " " + leafs[i]))

def makeTree(term, command):
    leafs = list(filter(None, getNode(term, command.value + " ?")))

    if len(leafs) < 1:
        return command
    else:
        for i in range(len(leafs)):
            newCommand = makeTree(term, Command(i, command.value + " " + leafs[i]))
            commandTree.add(newCommand)
            data.append(newCommand.value)

        commandTree.clear()
        return command


def parseDeviceSyntax(term, initialString):

    startTree(term, initialString)
    generateStructure(data)
