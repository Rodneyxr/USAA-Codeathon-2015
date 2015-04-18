#!/usr/bin/python3
import sys
from PyQt4 import QtGui, QtCore
from QtApp.view.mainwindow import Ui_mainwindow
from QtApp.view.CalendarDialog import CalendarDialog
from QtApp.view.ReviewModify import ReviewModify
from PyQt4.QtCore import QDateTime

class QtPiMainWindow(QtGui.QMainWindow):
    #Signal for entering the from/to/dates/whatever
    #Passes a slot these parameters in this order:
    #fromString, toString, fromDateObj, toDateObj, fromTimeObj, toTimeObj
    searchSignal = QtCore.pyqtSignal(str, str, object, object, object, object)
    idSignal = QtCore.pyqtSignal(int)
    bookSignal = QtCore.pyqtSignal(int)
    def __init__(self, model):
        super(QtPiMainWindow, self).__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.whichButton = ""
        self.selectedRow = None
        self.cal = CalendarDialog()
        self.rev = ReviewModify(self.model)
        self.cal.diag.calendarWidget.clicked.connect(self.setDate)
        self.win = Ui_mainwindow()
        self.win.setupUi(self)
        self.win.flightStatusTable.setModel(self.model.getDepartureListModel())
        self.win.checkButton.clicked.connect(self.sendSearchData)
        self.win.fromDate.clicked.connect(self.wrapFrom)
        self.win.toDate.clicked.connect(self.wrapTo)
        self.win.flightStatusTable.clicked.connect(self.grabID)
        self.win.flightStatusTable.clicked.connect(self.selectRow)
        self.win.bookButton.clicked.connect(self.sendBooked)
        self.fillDropDates()
    
    #Sends the controller the id of the booked flight
    def sendBooked(self):
        if selectedRow is not None:
            self.bookSignal.emit(self.selectedRow)

    #Retrieves the ID from the selected row.
    #Emits a signal that allows for the controller to get the flight.
    def grabID(self, item):
        print((item.row())) #Adding one because row() starts at zero.
        self.idSignal.emit(item.row())
    #Selects the entire row upon mouseclick
    def selectRow(self, item):
        self.selectedRow = self.sender().selectRow(item.row())

    #Wrappers for calSelect because I'm dumb
    def wrapFrom(self):  
        self.calSelect("fromDate")

    def wrapTo(self):
        self.calSelect("toDate")
    #Display the calendar dialog
    def calSelect(self, text):
        self.whichButton = text
        self.cal.exec_()

    def setDate(self, date):
        if self.whichButton == "fromDate":
            self.fromDateObj = date
            self.win.fromDate.setText(date.toString())
        else:
            print(self.sender().objectName())
            self.toDateObj = date
            self.win.toDate.setText(date.toString())
        

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
        ###NOTE: fromDate and toDate are being changed to buttons that activate
        #dialogs
        fromTimeObj = self.win.fromTime.currentText()
        toTimeObj = self.win.toTime.currentText()
        self.searchSignal.emit(fromStr, toStr, self.fromDateObj, self.toDateObj, 
                            fromTimeObj, toTimeObj)
