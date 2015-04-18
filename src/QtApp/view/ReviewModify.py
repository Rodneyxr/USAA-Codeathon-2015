import sys
from PyQt4 import QtGui, QtCore
from QtApp.view.review_modify import Ui_ReviewModifyForm

class ReviewModify(QtGui.QWidget):

    signalClear = QtCore.pyqtSignal(int)
    def __init__(self, model):
        super(ReviewModify, self).__init__()
        self.initUI(model)

    def initUI(self, model):
        self.review = Ui_ReviewModifyForm()
        self.review.setupUi(self)
        self.review.cancelSelected.clicked.connect(self.clearSelected)
        self.review.table.setModel(model.getBookedListModel())
    
    def clearSelected(self, item):
        self.signalClear.emit(self.review.table.clearSelection())
