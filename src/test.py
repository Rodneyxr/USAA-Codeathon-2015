import unittest
import sys

from PyQt4 import QtCore, QtGui
from hashlib import sha256
import datetime

class Test(unittest.TestCase):
    """
     This class will test all kinds of functionality for this application.
     All test method names should follow the naming convention of all lower-case
     letters delimited by underscores and must begin with 'test_'
     ex: def test_login(self):
     """

    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        mainWindow = QtGui.QMainWindow()
        mainWindow.show()

    def tearDown(self):
        sys.exit(self.app.exec())

    def test_hash(self):
        password = "password01"
        print(sha256(str(password).encode('utf-8')).hexdigest())

if __name__ == '__main__':
    unittest.main()