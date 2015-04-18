from PyQt4 import QtCore
from QtApp.model.Departures import FlightStatusTable


class QtModel(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

        self.data = [['Test1_0', 'Test1_2', 'Test1_3', 'Test1_4', 'Test1_5', 'Test1_6'],
                     ['Test1_0', 'Test1_2', 'Test1_3', 'Test1_4', 'Test1_5', 'Test1_6'],
                     ['Test1_0', 'Test1_2', 'Test1_3', 'Test1_4', 'Test1_5', 'Test1_6'],
                     ['Test1_0', 'Test1_2', 'Test1_3', 'Test1_4', 'Test1_5', 'Test1_6']]

        self.header = ['TYPE', 'FLIGHT', 'FROM', 'TO', 'TIME', 'VACANCY', 'GATE', 'NOTE']

        self.__departureList = FlightStatusTable(self.data, self.header)

    def getDepartureListModel(self):
        return self.__departureList