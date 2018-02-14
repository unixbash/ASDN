from comms.Communication import send_command
from net.DictionaryNester import generateStructure
from utility.LinkedList import *
from utility.Util import isAscii

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
            leafs.append(leaf.strip().split(" ")[0].rstrip())

            #Check if complete
            if(">" in leaf):
                if (leafs):
                    leafs.pop()
                return leafs

#Start the tree generation process
def startTree(term, initialString):
    if(initialString==""):
        helper = "?"
    else:
        helper = " ?"

    leafs = list(filter(None, getNode(term, initialString + helper)))

    for i in range(len(leafs)):
        makeTree(term, Command(i, initialString + " " + leafs[i]))

def makeTree(term, command):
    print(command.value)
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
