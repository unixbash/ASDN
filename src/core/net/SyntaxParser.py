from comms.Communication import send_command
from utility.util import *

import json

def getNode(term, initialString):
    commandOutput = send_command(term, initialString)
    leafs = []
    parsedOutput = commandOutput.splitlines()
    for leaf in parsedOutput:
        if not ("show" in leaf or "Possible" in leaf):
            leafs.append(leaf.strip().split(" ")[0].rstrip())
            #Check if valid
            if ('<[Enter]>' in leaf or "|" in leaf):
                leafs.pop()
                leafs.remove('')

            #Check if complete
            if('^' in leaf or ">" in leaf):
                leafs.pop()
                leafs.remove('')
                return leafs

def parseDeviceSyntax(term, initialString):

    data = {}
    list_append(data, expandList(term, initialString, data))

    # Generate the JSON structure
    with open('structure.txt', 'w') as outfile:
        json_data = json.dump(data, outfile)

#Recursive function --> parsing the entire device operational hierarchy
def expandList(term, initialString, data):
    leafs = list(filter(None, getNode(term, initialString + " ?")))

    if (len(leafs) > 0):
        for leaf in leafs:
            return expandList(term, initialString + " " + leaf, data)