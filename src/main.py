import sys

from PyQt4 import QtCore, QtGui


def main():
    app = QtGui.QApplication(sys.argv)

    # This is just for testing right now
    mainWindow = QtGui.QMainWindow()
    mainWindow.show()
    # mainWindow.showFullScreen()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()