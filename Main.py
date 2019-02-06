# -*- coding: utf-8 -*-


import INCOME_PAGE_UI,MAIN_UI,ADD_CARD
from pyqtgraph.Qt import QtGui, QtCore


app = QtGui.QApplication([])



dashboard_page = MAIN_UI.MAIN_UI()

income_page = INCOME_PAGE_UI.INCOME_PAGE_UI()
income_page.initPages(dashboard_page)

income_page.show()




if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


