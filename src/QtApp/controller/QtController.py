from PyQt4 import QtCore


class QtController(QtCore.QObject):
    def __init__(self, model, view):
        QtCore.QObject.__init__(self)
        self.model = model
        self.view = view

        self.view.mainscreen.searchSignal.connect(self.searchFlights)
        # TODO: connect book flight
        # self.view.mainscreen.

        #TODO: connect kill flight
        # self.view.mainscreen.

    def searchFlights(self, fromLocation, toLocation, fromDate, toDate, fromTime, toTime):
        self.model.searchFlights(fromLocation, toLocation, fromDate, toDate, fromTime, toTime)

    def killFlight(self, flight_id):
        self.model.killFlight(flight_id)

    def bookFlight(self, flight_id):
        self.model.bookFlight(flight_id)