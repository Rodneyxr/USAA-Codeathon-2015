#!/usr/bin/python3
"""
    QtView.py
    This is the master view class. Manages UI.
"""
import sys
from PyQt4 import QtGui, QtCore
from QtApp.view.QtPiMainWindow import QtPiMainWindow
from QtApp.view.ReviewModify import ReviewModify

class QtView(QtCore.QObject):
    def __init__(self, model):
        super(QtView, self).__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.mainscreen = QtPiMainWindow(self.model)
        self.modifyscreen = ReviewModify(self.model)
        self.mainscreen.show()
        self.mainscreen.swapMod.connect(self.toModify)
        self.mainscreen.swapMain.connect(self.toMain)
        self.modifyscreen.review.backToMain.clicked.connect(self.toMain)
        # self.mainscreen.win.flightStatusTable.setModel(self.model.getDepartureListModel())

    def toModify(self):
        print("in toModify")
        self.mainscreen.hide()
        self.modifyscreen.show()

    def toMain(self):
        print("in toMain")
        self.modifyscreen.hide()
        self.mainscreen.show()
