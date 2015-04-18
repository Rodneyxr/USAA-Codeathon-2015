from PyQt4 import QtCore

from QtApp.model.FlightModel import FlightStatusTable
from QtApp.database.FlightsDB import FlightsDB
from QtApp.database.CustomerDB import CustomerDB

# bookFlight
class QtModel(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.header = ['FLIGHT ID', 'ORIGIN', 'DEST', 'DEPART', 'ARRIVE', 'AVAIL']
        data = FlightsDB.getFlights()
        self.flights = data
        self.__departureList = FlightStatusTable(self.flights, self.header)

        data = CustomerDB.getFlights()
        self.cust_flights = data
        self.__customerList = FlightStatusTable(self.cust_flights, self.header)

    def getDepartureListModel(self):
        return self.__departureList

    def getBookedListModel(self):
        return self.__customerList

    def addFlight(self, flight_id):
        id = self.__customerList.getFlightList()[flight_id].getFlightID()
        FlightsDB.bookFlight(id)
        self.__customerList.reset()

    def bookFlight(self, flight_id):
        id = self.__departureList.getFlightList()[flight_id].getFlightID()
        FlightsDB.bookFlight(id)

    def killFlight(self, flight_id):
        FlightsDB.killFlight(flight_id)

    def searchFlights(self, fromLocation, toLocation, fromDate, toDate, fromTime, toTime):
        if toDate is None and fromDate is None:
            print("You must select a date!")
            return
        if toDate is None:
            flightsResult = FlightsDB.searchFlightsArrival(fromDate)
        elif fromDate is None:
            flightsResult = FlightsDB.searchFlightsDeparture(toDate)
        else:
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