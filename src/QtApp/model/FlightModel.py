from PyQt4 import QtCore


class FlightStatusTable(QtCore.QAbstractTableModel):
    def __init__(self, data_in, header_data, parent=None):
        """
        This AbstractTableModel implementation will contain all data to be
        displayed by a TableWidget.

        :param data_in: a list of flights
        :param header_data: a list of strings
        :param parent: None
        :return: None
        """
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.array_data = data_in
        self.header_data = header_data

    def rowCount(self, parent) -> int:
        return len(self.array_data)

    def columnCount(self, parent) -> int:
        if (len(self.array_data) == 0):
            return 0
        return len(self.array_data[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.array_data[index.row()].data[index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header_data[col]

    def setFlightList(self, flightList):
        self.array_data = flightList
        self.reset()

    def getFlightList(self):
        return self.array_data