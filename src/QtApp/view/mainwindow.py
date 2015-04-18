# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Apr 18 02:42:22 2015
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

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName(_fromUtf8("mainwindow"))
        mainwindow.resize(841, 464)
        mainwindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtGui.QWidget(mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.fromCity = QtGui.QLineEdit(self.groupBox)
        self.fromCity.setObjectName(_fromUtf8("fromCity"))
        self.gridLayout.addWidget(self.fromCity, 0, 1, 1, 1)
        self.fromDate = QtGui.QDateEdit(self.groupBox)
        self.fromDate.setObjectName(_fromUtf8("fromDate"))
        self.gridLayout.addWidget(self.fromDate, 0, 2, 1, 1)
        self.fromTime = QtGui.QComboBox(self.groupBox)
        self.fromTime.setObjectName(_fromUtf8("fromTime"))
        self.gridLayout.addWidget(self.fromTime, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.toCity = QtGui.QLineEdit(self.groupBox)
        self.toCity.setObjectName(_fromUtf8("toCity"))
        self.gridLayout.addWidget(self.toCity, 1, 1, 1, 1)
        self.toDate = QtGui.QDateEdit(self.groupBox)
        self.toDate.setObjectName(_fromUtf8("toDate"))
        self.gridLayout.addWidget(self.toDate, 1, 2, 1, 1)
        self.toTime = QtGui.QComboBox(self.groupBox)
        self.toTime.setObjectName(_fromUtf8("toTime"))
        self.gridLayout.addWidget(self.toTime, 1, 3, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.flightNumber = QtGui.QLineEdit(self.groupBox_2)
        self.flightNumber.setObjectName(_fromUtf8("flightNumber"))
        self.horizontalLayout.addWidget(self.flightNumber)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.modifyFlights = QtGui.QPushButton(self.groupBox_3)
        self.modifyFlights.setDefault(False)
        self.modifyFlights.setFlat(False)
        self.modifyFlights.setObjectName(_fromUtf8("modifyFlights"))
        self.verticalLayout.addWidget(self.modifyFlights)
        self.checkIn = QtGui.QPushButton(self.groupBox_3)
        self.checkIn.setObjectName(_fromUtf8("checkIn"))
        self.verticalLayout.addWidget(self.checkIn)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.flightStatusTable = QtGui.QTableView(self.centralwidget)
        self.flightStatusTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.flightStatusTable.setFrameShadow(QtGui.QFrame.Raised)
        self.flightStatusTable.setObjectName(_fromUtf8("flightStatusTable"))
        self.verticalLayout_2.addWidget(self.flightStatusTable)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("mainwindow", "Book", None))
        self.label.setText(_translate("mainwindow", "From", None))
        self.label_2.setText(_translate("mainwindow", "To", None))
        self.groupBox_2.setTitle(_translate("mainwindow", "Check Status", None))
        self.label_3.setText(_translate("mainwindow", "Flight #", None))
        self.groupBox_3.setTitle(_translate("mainwindow", "My Account", None))
        self.modifyFlights.setText(_translate("mainwindow", "Modify my flights", None))
        self.checkIn.setText(_translate("mainwindow", "Check In", None))

