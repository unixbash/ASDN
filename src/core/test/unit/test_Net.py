import unittest
import utility.Util
from net.NetworkTopology import getMacVendor

class TestNet(unittest.TestCase):

    def test_isAscii(self):
        self.assertTrue(utility.Util.isAscii("ABC"))
        self.assertFalse(utility.Util.isAscii("şABCş"))

    def test_getMacVendor(self):
        mac="f4:cc:55:2e:d5:b0"
        self.assertEquals(getMacVendor(mac), "Juniper Networks")

if __name__  == '__main__':
    unittest.main()