import sys

from PyQt4 import QtCore, QtGui
from QtApp.model.QtModel import QtModel


def main():
    app = QtGui.QApplication(sys.argv)

    model = QtModel()


    # This is just for testing right now
    mainWindow = QtGui.QMainWindow()
    mainWindow.show()
    # mainWindow.showFullScreen()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()