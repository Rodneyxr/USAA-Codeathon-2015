import sys
from PyQt4 import QtGui
from QtApp.view.calendardialog import Ui_calDialog

class CalendarDialog(QtGui.QDialog):
    def __init__(self):
        super(CalendarDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.diag = Ui_calDialog()
        self.diag.setupUi(self)
        self.diag.checkBox.accepted.connect(self.done)
