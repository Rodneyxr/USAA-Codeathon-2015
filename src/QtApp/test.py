import unittest
import sys

from PyQt4 import QtCore, QtGui

class Test(unittest):

    def __init__(self, unittest):
        unittest.__init__(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)


    sys.exit(app.exec_())