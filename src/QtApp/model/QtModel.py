from PyQt4 import QtCore

from QtApp.model.FlightModel import FlightStatusTable
from QtApp.model.FlightClass import Flight
from QtApp.database.FlightsTable import FlightQueryNames
from QtApp.database.FlightsDB import FlightsDB


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

    def createFlight(self, id, origin, dest, depart, arrive, avail):
        kwargs = {
            FlightQueryNames.flightIDField: id,
            FlightQueryNames.originField: origin,
            FlightQueryNames.destField: dest,
            FlightQueryNames.departTimeField: depart,
            FlightQueryNames.arriveTimeField: arrive,
            FlightQueryNames.availSeatsField: avail
        }
        return Flight(**kwargs)