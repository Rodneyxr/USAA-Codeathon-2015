# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review_modify.ui'
#
# Created: Sat Apr 18 06:29:32 2015
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

class Ui_ReviewModifyForm(object):
    def setupUi(self, ReviewModifyForm):
        ReviewModifyForm.setObjectName(_fromUtf8("ReviewModifyForm"))
        ReviewModifyForm.resize(566, 367)
        self.verticalLayout = QtGui.QVBoxLayout(ReviewModifyForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cancelSelected = QtGui.QPushButton(ReviewModifyForm)
        self.cancelSelected.setObjectName(_fromUtf8("cancelSelected"))
        self.verticalLayout.addWidget(self.cancelSelected)
        self.table = QtGui.QTableView(ReviewModifyForm)
        self.table.setObjectName(_fromUtf8("table"))
        self.verticalLayout.addWidget(self.table)

        self.retranslateUi(ReviewModifyForm)
        QtCore.QMetaObject.connectSlotsByName(ReviewModifyForm)

    def retranslateUi(self, ReviewModifyForm):
        ReviewModifyForm.setWindowTitle(_translate("ReviewModifyForm", "Review & Modify flights", None))
        self.cancelSelected.setText(_translate("ReviewModifyForm", "Cancel Selected", None))

