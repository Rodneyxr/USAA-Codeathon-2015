from PyQt4 import QtCore


class QtController(QtCore.QObject):
    def __init__(self, model, view):
        QtCore.QObject.__init__(self)
        self.model = model
        self.view = view
