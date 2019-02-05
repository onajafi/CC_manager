# -*- coding: utf-8 -*-

import pyqtgraph
from PyQt5.QtWidgets import QPushButton, QScrollArea, QWidget, QVBoxLayout,QHBoxLayout
from PyQt5 import QtCore

CreditInfoWidgetOBJ_LIST = []

class CreditInfoWidget(QWidget):
    reScaling = False

    def __init__(self,title = None):
        QWidget.__init__(self)
        CreditInfoWidgetOBJ_LIST.append(self)

        self.setFixedHeight(150)
        self.plot_widget = pyqtgraph.PlotWidget(title = title)
        # self.plot_widget.setFixedWidth(400)

        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(self.plot_widget)
        self.EDIT_BTN = QPushButton("Edit")
        self.DELETE_BTN = QPushButton("Delete")
        btn_Layout = QVBoxLayout()
        btn_Layout.addWidget(self.EDIT_BTN)
        btn_Layout.addWidget(self.DELETE_BTN)
        self.hLayout.addLayout(btn_Layout)

        self.setLayout(self.hLayout)
        self.plot_widget.sigRangeChanged.connect(self.axis_changed)



    def eventFilter(self, object, event):
        print("AnEVENT")
        if event.type() == QtCore.QEvent.MouseButtonPress:
            print("You leaved the Widget")
            return True

    # def mouseMoveEvent(self, event):
    #     print("AnEVENT")

    def plot(self):
        return self.plot_widget.plot()


    def axis_changed(self,r):
        if not CreditInfoWidget.reScaling:
            CreditInfoWidget.reScaling = True
            for elem in CreditInfoWidgetOBJ_LIST:
                if elem is not self:
                    pass
                    elem.plot_widget.setRange(xRange=r.getAxis('bottom').range)

            # self.plot_widget.setRange(xRange=r.getAxis('bottom').range)

            CreditInfoWidget.reScaling = False





