from PyQt4 import QtCore

from QtApp.model.FlightModel import FlightStatusTable
from QtApp.database.FlightsDB import FlightsDB

# bookFlight
class QtModel(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.header = ['FLIGHT ID', 'ORIGIN', 'DEST', 'DEPART', 'ARRIVE', 'AVAIL']
        data = FlightsDB.getFlights()
        self.flights = data
        self.__departureList = FlightStatusTable(self.flights, self.header)

    def getDepartureListModel(self):
        return self.__departureList

    def addFlight(self, flight):
        self.flights.append(flight)

    def searchFlights(self, fromLocation, toLocation, fromDate, toDate, fromTime, toTime):
        flightsResult = FlightsDB.searchFlightsArrivalDeparture(fromDate, toDate)
        if fromLocation == '' and toLocation == '':
            self.__departureList.setFlightList(flightsResult)
            return

        newList = []
        for flight in flightsResult:
            if fromLocation != '' and toLocation != '':
                if flight.getFlightOrigin() == fromLocation and flight.getFlightDestination() == toLocation:
                    newList.append(flight)
            if fromLocation != '' and toLocation == '':
                if flight.getFlightOrigin() == fromLocation:
                    newList.append(flight)
            if fromLocation == '' and toLocation != '':
                if flight.getFlightDestination() == toLocation:
                    newList.append(flight)

        self.__departureList.setFlightList(newList)