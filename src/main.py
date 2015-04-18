import sys

from PyQt4 import QtCore, QtGui
from QtApp.model.QtModel import QtModel
from QtApp.view.QtView import QtView
from QtApp.controller.QtController import QtController


def main():
    app = QtGui.QApplication(sys.argv)

    model = QtModel()
    view = QtView(model)
    controller = QtController(model, view)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()