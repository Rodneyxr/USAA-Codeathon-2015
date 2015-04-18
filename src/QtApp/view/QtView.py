#!/usr/bin/python3
"""
    QtView.py
    This is the master view class. Manages UI.
"""
import sys
from PyQt4 import QtGui, QtCore
from QtApp.view.QtPiMainWindow import QtPiMainWindow

class QtView(QtCore.QObject):
    def __init__(self):
        super(QtView, self).__init__()
        self.initUI()

    def initUI(self):
        self.mainscreen = QtPiMainWindow()
        self.mainscreen.show()
