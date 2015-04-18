from PyQt4 import QtCore


class QtController(QtCore.QObject):
    def __init__(self, model, view):
        QtCore.QObject.__init__(self)
        self.model = model
        self.view = view

        self.view.mainscreen.searchSignal.connect(self.searchFlights)

    def searchFlights(self, fromLocation, toLocation, fromDate, toDate, fromTime, toTime):
        self.model.searchFlights(fromLocation, toLocation, fromDate, toDate, fromTime, toTime)
        # fromDateTime = QtCore.QDateTime(fromDate, fromTime)
        # toDateTime = QtCore.QDateTime(toDate, toTime)