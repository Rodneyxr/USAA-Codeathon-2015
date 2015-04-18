#!/usr/bin/python3
import sys
from PyQt4 import QtGui
from QtApp.view.mainwindow import Ui_MainWindow

class QtPiMainWindow(QtGui.None):
    def __init__(self):
        super(View, self).__init__()
        self.initUI()

    def initUI(self):
        self.win = Ui_MainWindow()
        self.win.setupUi(self)
