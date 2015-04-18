from PyQt4 import QtCore

class DepartureList(QtCore.QAbstractTableModel):

    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)

    def rowCount(self) -> int:
        return 0

    def columnCount(self) -> int:
        return 0