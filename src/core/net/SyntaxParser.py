from comms.Communication import send_command
from lxml import etree
from xml.etree.ElementTree import ElementTree

def getRootNode(commandOutput):
    leafs = []
    for leaf in commandOutput.splitlines():
        if not ("show" in leaf or "Possible" in leaf):
            leafs.append(leaf.strip().split(" ")[0].rstrip())
            if('^' in leaf or "asdn" in leaf):
                leafs.pop()
                leafs.remove('')
                return leafs

def parseDeviceSyntax(term, initialString):

    searchCommand = "show "
    helper = " | display xml"
    commandOutput = send_command(term, initialString)
    leafs = getRootNode(commandOutput)

    #Generate the XML structure
    root = etree.Element('root')
    tree = ElementTree(root)

    # pretty string
    s = etree.tostring(root, pretty_print=True)

    for leaf in leafs:
        comand = searchCommand + leaf + " ?"
        # node = getRootNode(send_command(term,comand)).encode("utf-8")
        root.append(etree.Element(leaf))

    #s = etree.tostring(root, pretty_print=True)
    tree.write(open('person.xml', 'wb'))
    #print(s)