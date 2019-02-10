# -*- coding: utf-8 -*-

import pyqtgraph
from PyQt5.QtWidgets import QPushButton, QScrollArea, QWidget, QVBoxLayout,QHBoxLayout, QLineEdit
from PyQt5 import QtCore

CreditInfoWidgetOBJ_LIST = []

class CreditInfoWidget(QWidget):
    reScaling = False

    def __init__(self,title = None,isIncome = False):
        QWidget.__init__(self)
        CreditInfoWidgetOBJ_LIST.append(self)

        self.setFixedHeight(150)
        self.plot_widget = pyqtgraph.PlotWidget(title = title)
        # self.plot_widget.mousePressEvent.connect(self.click_on_plot_event)
        # self.plot_widget.setFixedWidth(400)

        self.hLayout = QHBoxLayout()
        self.plot_widget.setMouseEnabled(x=True, y=False)
        self.hLayout.addWidget(self.plot_widget)
        btn_Layout = QVBoxLayout()
        self.hLayout.addLayout(btn_Layout)

        self.setLayout(self.hLayout)
        self.plot_widget.sigRangeChanged.connect(self.axis_changed)

        self.arrow_list = []
        self.is_income = isIncome
        if isIncome:
            self.draw_income(range(0,10))
            self.GIVE_MONEY_BTN = QPushButton("Give Money")
            self.income_amount = QLineEdit('')
            btn_Layout.addWidget(self.GIVE_MONEY_BTN)
            btn_Layout.addWidget(self.income_amount)
            btn_Layout.addStretch()

            self.plot_Xpoints = []
            self.plot_Ypoints = []
            self.auto_scroll = True
            self.income_amount_label = pyqtgraph.TextItem("")
            self.plot_widget.addItem(self.income_amount_label)
        else:
            self.EDIT_BTN = QPushButton("Edit")
            # self.EDIT_BTN.clicked.connect(self.edit_card_info_event)
            # btn_Layout.addWidget(self.EDIT_BTN)
            self.DELETE_BTN = QPushButton("Delete")
            self.DELETE_BTN.clicked.connect(self.delete_plot_event)
            btn_Layout.addWidget(self.DELETE_BTN)
            # self.add_REL_time(2)
            # self.add_SOFT_deadline(5)
            # self.add_HARD_deadline(6)

    def click_on_plot_event(self):
        print("clicked")

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

    def add_HARD_deadline(self,time,amount = None):
        if amount:
            label = pyqtgraph.TextItem("%.2f" % amount, fill=(0, 0, 0))
            label.setPos(time, 110)
            self.plot_widget.addItem(label)

        arrow = pyqtgraph.ArrowItem(angle=270, tipAngle=30,
                                  baseAngle=10, headLen=20,
                                  tailLen=100, tailWidth=1,
                                  pen=None, brush='r')
        arrow.setPos(time, 0)
        self.plot_widget.addItem(arrow)
        self.arrow_list.append(arrow)
        if amount:
            label = pyqtgraph.TextItem("%.2f" % amount)
            label.setPos(time,110)
            self.plot_widget.addItem(label)
        self.plot_widget.setRange(yRange=(0,100))

    def add_SOFT_deadline(self,time,amount = None):
        if amount:
            label = pyqtgraph.TextItem("%.2f" % amount, fill=(0, 0, 0))
            label.setPos(time, 110)
            self.plot_widget.addItem(label)

        arrow = pyqtgraph.ArrowItem(angle=270, tipAngle=30,
                                  baseAngle=10, headLen=20,
                                  tailLen=100, tailWidth=1,
                                  pen=None, brush='y')
        arrow.setPos(time, 0)
        self.plot_widget.addItem(arrow)
        self.arrow_list.append(arrow)
        if amount:
            label = pyqtgraph.TextItem("%.2f" % amount)
            label.setPos(time,110)
            self.plot_widget.addItem(label)
        self.plot_widget.setRange(yRange=(0,100))

    def add_REL_time(self,time,amount = None):
        if amount:
            label = pyqtgraph.TextItem("%.2f" % amount,fill=(0,0,0))
            label.setPos(time,110)
            self.plot_widget.addItem(label)

        arrow = pyqtgraph.ArrowItem(angle=90, tipAngle=30,
                                  baseAngle=10, headLen=20,
                                  tailLen=100, tailWidth=1,
                                  pen=None, brush='g')
        arrow.setPos(time, 100)
        self.plot_widget.addItem(arrow)
        self.arrow_list.append(arrow)
        self.plot_widget.setRange(yRange=(0,100))

    def draw_income(self,list):
        self.green_line_plot = self.plot_widget.plot(list, fillLevel=-0.3, brush=(50,200,50,100),pen=(100,255,100,200))

    def init_main_page(self,_main_page):
        self.main_page = _main_page

    def delete_plot_event(self):
        self.main_page.request_delete(self)
        CreditInfoWidgetOBJ_LIST.remove(self)

    def redraw_plot(self):
        if(self.is_income):
            if self.auto_scroll:
                if(len(self.plot_Ypoints) >= 10):
                    new_range = range(self.plot_Xpoints[-1] - 4,self.plot_Xpoints[-1] + 6)
                    self.plot_widget.setRange(xRange=new_range)
                    # self.auto_scroll = False
                else:
                    new_range = range(1,10)
                    self.plot_widget.setRange(xRange=new_range)

            self.green_line_plot.setData(x=self.plot_Xpoints,
                                  y=self.plot_Ypoints)
            self.income_amount_label.setText("%.2f" % self.plot_Ypoints[-1])
            self.income_amount_label.setPos(self.plot_Xpoints[-1],self.plot_Ypoints[-1])


    def add_point_to_income_plot(self,_x,_y):
        if(len(self.plot_Ypoints) > 0):
            self.plot_Xpoints.append(_x)
            self.plot_Ypoints.append(self.plot_Ypoints[-1])
        self.plot_Xpoints.append(_x)
        self.plot_Ypoints.append(_y)