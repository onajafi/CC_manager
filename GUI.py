
import pyqtgraph
from PyQt5.QtWidgets import QPushButton, QScrollArea, QWidget, QVBoxLayout,QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel


from CreditInfoWidget import CreditInfoWidget
from pyqtgraph.Qt import QtGui, QtCore
import INCOME_PAGE_UI,MAIN_UI

app = QtGui.QApplication([])

first_page = INCOME_PAGE_UI.INCOME_PAGE_UI()
# first_page.show()

second_page = MAIN_UI.MAIN_UI()
second_page.show()




if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()








