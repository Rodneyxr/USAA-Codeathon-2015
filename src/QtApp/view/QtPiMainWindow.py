#!/usr/bin/python3
import sys
from PyQt4 import QtGui, QtCore
from QtApp.view.mainwindow import Ui_mainwindow
from PyQt4.QtCore import QDateTime

class QtPiMainWindow(QtGui.QMainWindow):
    #Signal for entering the from/to/dates/whatever
    #Passes a slot these parameters in this order:
    #fromString, toString, fromDateObj, toDateObj, fromTimeObj, toTimeObj
    searchSignal = QtCore.pyqtSignal(str, str, object, object, object, object)
    def __init__(self, model):
        super(QtPiMainWindow, self).__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.win = Ui_mainwindow()
        self.win.setupUi(self)
        self.win.flightStatusTable.setModel(self.model.getDepartureListModel())
        self.win.findButton.clicked.connect(self.sendSearchData)
        self.fillDropDates()

    #Fills in the times for the dropdown menu, from 12:00AM to 12:00PM, 
    #in 30 minute intervals.
    def fillDropDates(self):
        #Use 24 hour format for simplicity with displaying AM/PM.
        minute = 0
        hour = 0
        self.timeList = []
        hourList = [i for i in range(0, 25)]
        #Append QTime objects to the timeList.
        for h in hourList:
            dateObj1 = QtCore.QTime(h, 0)
            dateObj2 = QtCore.QTime(h, 30)
            self.timeList.append(dateObj1)
            self.timeList.append(dateObj2)
        #Hook up the timeList to the dropdown layout objects.
        self.win.fromTime.insertItems(0, 
        [i.toString("hh:mm") for i in self.timeList if i is not None])
        self.win.toTime.insertItems(0, 
        [i.toString("hh:mm") for i in self.timeList if i is not None])
    #TODO: create slot for listening to "Find" buttonclicked signal.
    def sendSearchData(self):
        fromStr = self.win.fromCity.text()
        toStr = self.win.toCity.text()
        fromDateObj = self.win.fromDate.date
        toDateObj = self.win.toDate.date
        fromTimeObj = self.win.fromTime.currentText()
        toTimeObj = self.win.toTime.currentText()
        self.searchSignal.emit(fromStr, toStr, fromDateObj, toDateObj, 
                            fromTimeObj, toTimeObj)
