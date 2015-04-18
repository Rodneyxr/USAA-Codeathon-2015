from PyQt4 import QtCore

from QtApp.model.FlightModel import FlightStatusTable
from QtApp.model.FlightClass import Flight
from QtApp.database.FlightsTable import FlightQueryNames
from QtApp.database.FlightsDB import FlightsDB


class QtModel(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

        self.header = ['FLIGHT ID', 'ORIGIN', 'DEST', 'DEPART', 'ARRIVE', 'AVAIL']
        # self.data = [['ID01', 'San Antonio', 'Dallas', QtCore.QDateTime(2015, 1, 26, 11, 0),
        #               QtCore.QDateTime(2015, 1, 26, 11, 0), 42],
        #              ['ID02', 'San Fran', 'Las Vegas', QtCore.QDateTime(2015, 2, 27, 9, 0),
        #               QtCore.QDateTime(2015, 2, 27, 3, 0), 99],
        #              ['ID03', 'Hawaii', 'New York', QtCore.QDateTime(2015, 11, 1, 10, 0),
        #               QtCore.QDateTime(2015, 11, 1, 5, 0), 128],
        #              ['ID04', 'Tokyo', 'Houston', QtCore.QDateTime(2015, 12, 16, 14, 0),
        #               QtCore.QDateTime(2015, 12, 16, 20, 0), 42]]

        data = FlightsDB.getFlights()
        self.flights = list()

        for i in range(len(data)):
            tmpFlight = self.createFlight(
                self.data[i][0],
                self.data[i][1],
                self.data[i][2],
                self.data[i][3],
                self.data[i][4],
                self.data[i][5])
            self.addFlight(tmpFlight)

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