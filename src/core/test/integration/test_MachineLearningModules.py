import unittest
from comms.Communication import establishConnection, establishShell
from net.DictionaryNester import generateStructure
from net.SyntaxParser import startTree, data
from utility.Util import dictToKeyList

class TestUtil(unittest.TestCase):

    def test_parseDeviceSyntax(self):
        ssh = establishConnection("10.10.10.110", "asdn", "ASDN2018") #Not real login information
        term = establishShell(ssh, False)
        initialString = "configuration"
        startTree(term, initialString)

        self.assertTrue(generateStructure())
