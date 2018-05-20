import os
import io
import unittest
import utility.Util
from mock.mock import self
from unittest.mock import patch

class TestUtil(unittest.TestCase):

    def test_isAscii(self):
        self.assertTrue(utility.Util.isAscii("ABC"))
        self.assertFalse(utility.Util.isAscii("şABCş"))

    def test_dictToKeyList(self):
        self.assertEqual(utility.Util.dictToKeyList({"key": "value"}), ["key"])
        self.assertEqual(utility.Util.dictToKeyList({"key1": "value1", "key2": "value2"}), ["key1", "key2"])

    def test_readAndWriteFile(self):
        fileName = "test"
        ext = ".txt"
        data = "data"
        utility.Util.writeTextFile(fileName, ext, data)
        content = utility.Util.readTextFile(fileName+ext)
        #Clean up after testing
        os.remove(fileName+ext)
        #Run the test
        self.assertEqual(content, [data])

    def test_findBetween(self):
        string = '!word!'
        delimeter = '!'
        result = utility.Util.findBetween(string, delimeter)
        self.assertEqual(result, 'word')

    def test_removeNonAlphaNum(self):
        string = '!word!'
        result = utility.Util.removeNonAlphaNum(string)
        self.assertEqual(result, 'word')

    def test_executeSql(self):
        sql = "SELECT (%s) FROM device"
        args = "id"
        result=""

        def setUp():
            self.oldFunc = utility.Util.executeSql
            utility.Util.executeSql = self.executeSqlNewFunc

        def tearDown():
            utility.Util.executeSql = self.oldFunc

        def executeSqlNewFunc(self, sql, args):
            return result

        self.assertEqual(executeSqlNewFunc(self, sql, args), result)

    def test_getAllSql(self):
        sql = "SELECT * FROM device"
        args = "id"
        result = ""

        def setUp():
            self.oldFunc = utility.Util.getAllSql()
            utility.Util.getAllSql = self.executeSqlNewFunc

        def tearDown():
            utility.Util.getAllSql = self.oldFunc

        def executeSqlNewFunc(self, sql, args):
            return result

        self.assertEqual(executeSqlNewFunc(self, sql, args), result)

    def test_uploadFile(self):
        fileName = "test.txt"
        path=""
        file = io.BytesIO(b'test.txt')

        def setUp():
            self.oldFunc = utility.Util.uploadFile
            utility.Util.uploadFile = self.executeNewUpload

        def tearDown():
            utility.Util.uploadFile = self.oldFunc

        def executeNewUpload(file, fileName, path):
            return type(file.read())

        self.assertEqual(executeNewUpload(file, fileName, path), type(file.read()))

    def test_replaceTabsWithSpaces(self):
        string="\tABC\t"
        result="  ABC  "
        self.assertEqual(utility.Util.replaceTabsWithSpaces(string), result)

    def test_getLatestOS(self):
        #Correct OS
        modelOne="EX3400"
        expectedOne="15.1X53-D58"
        self.assertEqual(utility.Util.getLatestOS(modelOne), expectedOne)

        #Incorrect OS
        modelTwo = "EX3400"
        expectedTwo = "15.1X53-D55"
        self.assertNotEqual(utility.Util.getLatestOS(modelTwo), expectedTwo)

    def test_callPy(self):
        version = "2.7"
        module = "py2Exec"
        func = "executeOnServer"
        args = "echo hello"

        return utility.Util.callPy(version, module, func, args)

    with patch('utility.Util.callPy') as mock:
        instance = mock.return_value
        instance.method.return_value = False
        result = test_callPy(self)

    def test_isExecOnServer(self):
        #Should throw an error as it is not executed on the server
        self.assertEqual(utility.Util.isExecOnServer(), False)

if __name__  == '__main__':
    unittest.main()