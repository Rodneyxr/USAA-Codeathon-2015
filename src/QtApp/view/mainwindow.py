# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Apr 17 21:49:40 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName(_fromUtf8("mainwindow"))
        mainwindow.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.centralwidget = QtGui.QWidget(mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

