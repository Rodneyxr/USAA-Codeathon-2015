# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendardialog.ui'
#
# Created: Sat Apr 18 06:22:55 2015
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

class Ui_calDialog(object):
    def setupUi(self, calDialog):
        calDialog.setObjectName(_fromUtf8("calDialog"))
        calDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(calDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.calendarWidget = QtGui.QCalendarWidget(calDialog)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.verticalLayout.addWidget(self.calendarWidget)
        self.checkBox = QtGui.QDialogButtonBox(calDialog)
        self.checkBox.setOrientation(QtCore.Qt.Horizontal)
        self.checkBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)

        self.retranslateUi(calDialog)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("accepted()")), calDialog.accept)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("rejected()")), calDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(calDialog)

    def retranslateUi(self, calDialog):
        calDialog.setWindowTitle(_translate("calDialog", "Dialog", None))

