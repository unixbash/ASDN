import unittest
from ml.DeviceStatusModelGen import Model

class TestDeviceStatusModelGen(unittest.TestCase):

    # Testing the entire ML assesment process
    def test_predict(self):
        model = Model()
        model.setFile('dataset.csv')

        self.assertEqual(model.predict([["0.27", "-0.8", "0", "1", "0", "17", "0.21", "11"]]), "Valid")

if __name__  == '__main__':
    unittest.main()