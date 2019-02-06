# -*- coding: utf-8 -*-


import INCOME_PAGE_UI,MAIN_UI,ADD_CARD
from pyqtgraph.Qt import QtGui, QtCore


app = QtGui.QApplication([])



dashboard_page = MAIN_UI.MAIN_UI()

income_page = INCOME_PAGE_UI.INCOME_PAGE_UI()
income_page.initPages(dashboard_page)

add_credit_page = ADD_CARD.ADD_CARD_UI()
add_credit_page.init_page(dashboard_page)

dashboard_page.initPages(income_page,add_credit_page)




income_page.show()




if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


