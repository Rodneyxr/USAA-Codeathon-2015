from PyQt4 import QtCore


class QtController(QtCore.QObject):
    def __init__(self, model, view):
        QtCore.QObject.__init__(self)
        self.model = model
        self.view = view

        self.view.mainscreen.searchSignal.connect(self.searchFlights)
        # TODO: connect book flight
        self.view.mainscreen.bookSignal.connect(self.bookFlight)

        #TODO: connect kill flight

    def searchFlights(self, fromLocation, toLocation, fromDate, toDate, fromTime, toTime):
        self.model.searchFlights(fromLocation, toLocation, fromDate, toDate, fromTime, toTime)

    def killFlight(self, flight_id):
        print("kill")
        self.model.killFlight(flight_id)

    def bookFlight(self, flight_id):
        print("book")
        self.model.bookFlight(flight_id)