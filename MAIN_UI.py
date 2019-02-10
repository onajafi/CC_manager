from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel

from pyqtgraph.Qt import QtGui, QtCore

import CreditInfoWidget
from scheduling import Scheduling, Event
import random


class MAIN_UI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(800,600)

        self.MainWid = QtGui.QWidget()
        self.setCentralWidget(self.MainWid)
        self.setWindowTitle('Dashboard')
        self.main_layout = QtGui.QVBoxLayout()
        self.sub_layout = QtGui.QVBoxLayout()

        self.main_main_layout = QtGui.QHBoxLayout()
        self.main_main_layout.addLayout(self.main_layout)
        self.main_main_layout.addLayout(self.sub_layout)

        self.MainWid.setLayout(self.main_main_layout)
        self.timer_enable = False

        self.main_schedule = None
        self.card_list = []# elem: [card_OBJ, plot_OBJ]

        self.MAIN_add_fields()
        self.SUB_add_field()

        self.INCOME_EDIT_BTN.clicked.connect(self.EDIT_INCOME_BTN_Event)
        self.time_pause.clicked.connect(self.time_pause_BTN_event)
        self.ADD_CARD_BTN.clicked.connect(self.add_card_event)

        self.time = 0



    def MAIN_add_fields(self):
        self.time_layout = QtGui.QHBoxLayout()
        self.time_layout.addWidget(QLabel("Show Time:"))
        self.disp_time = QLineEdit('0')
        self.disp_time.setEnabled(False)
        self.disp_time.setFixedWidth(50)
        self.time_layout.addWidget(self.disp_time)
        self.time_layout.addStretch()
        self.time_pause = QPushButton("Pause Time")
        self.time_layout.addWidget(self.time_pause)
        self.alertLight = QLabel("Alert Light")
        self.setAlertLightStat(True)
        self.time_layout.addWidget(self.alertLight)

        self.main_layout.addLayout(self.time_layout)

        # self.first_plot = CreditInfoWidget.CreditInfoWidget("HI",True)
        # self.main_layout.addWidget(self.first_plot)

        self.income_plot = CreditInfoWidget.CreditInfoWidget("income", True)
        self.main_layout.addWidget(self.income_plot)
        self.income_plot.GIVE_MONEY_BTN.clicked.connect(self.give_money_Event)

        # self.second_plot = CreditInfoWidget.CreditInfoWidget("HI again")
        # self.main_layout.addWidget(self.second_plot)

        self.main_layout.addStretch()

    def SUB_add_field(self):
        self.INCOME_EDIT_BTN = QPushButton("Edit Income")
        self.sub_layout.addWidget(self.INCOME_EDIT_BTN)

        # self.GIVE_MONEY_BTN = QPushButton("Give Money")
        # self.sub_layout.addWidget(self.GIVE_MONEY_BTN)

        self.ADD_CARD_BTN = QPushButton("Add Card")
        self.sub_layout.addWidget(self.ADD_CARD_BTN)

        self.sub_layout.addStretch()

    def setAlertLightStat(self, isOK):
        if isOK:
            self.alertLight.setStyleSheet("QLabel { background-color : #00FF00; "
                                    "font-size:12pt; font-weight:600; "
                                    "color:#000000;"
                                    "qproperty-alignment: AlignCenter }")
        else:
            self.alertLight.setStyleSheet("QLabel { background-color : #ff0000; "
                                    "font-size:12pt; font-weight:600; "
                                    "color:#000000;"
                                    "qproperty-alignment: AlignCenter }")

    def initPages(self,income_page, add_credit_page):
        self.income_page = income_page
        self.add_credit_page = add_credit_page

    def EDIT_INCOME_BTN_Event(self):
        self.income_page.show(self.main_schedule.income_period,
                              self.main_schedule.minimum_income,
                              self.main_schedule.maximum_income)

        self.close()

    def give_money_Event(self):
        if(self.income_plot.income_amount.text()):
            self.main_schedule.get_money_from_a_friend(
                float(self.income_plot.income_amount.text()))
            self.income_plot.income_amount.setText('')

    def show(self):
        self.timer_enable = True
        self.disp_time.setText(str(self.main_schedule.time))
        QtGui.QMainWindow.show(self)

    def close(self):
        self.timer_enable = False
        QtGui.QMainWindow.close(self)
    #
    # def time_forward_Event(self):
    #     if len(self.main_schedule.events) > 0:
    #         self.main_schedule.update_time(self.main_schedule.events[0].time)
    #         self.main_schedule.schedule()
    #         self.disp_time.setText(str(self.main_schedule.time))

    def time_pause_BTN_event(self):
        self.timer_enable = not self.timer_enable
        if(self.timer_enable):
            self.time_pause.setText("Pause Time")
        else:
            self.time_pause.setText("Play Time")

    def add_card_event(self):
        self.close()
        self.add_credit_page.show()

    def add_new_card(self,_card):
        tmp_plot = CreditInfoWidget.CreditInfoWidget(title=_card.name)
        tmp_plot.init_main_page(self)
        tmp_plot._card_OBJ = _card

        self.main_schedule.add_event(Event(self.time,"3-release",_card))
        self.main_layout.insertWidget(2,tmp_plot)
        self.card_list.append(tmp_plot)

        self.main_schedule.schedule()
        for _bill in _card.bills:
            tmp_plot.add_REL_time(_bill.release_time,_bill.debt)
            tmp_plot.add_SOFT_deadline(_bill.deadline,_bill.debt)
            tmp_plot.add_HARD_deadline(_bill.hard_deadline,_bill.debt)


    def request_delete(self,plot_widg):
        self.main_schedule.delete_card(plot_widg._card_OBJ)
        plot_widg.hide()
        self.card_list.remove(plot_widg)

    def time_tigger(self):
        print("timer triggered")
        if self.income_plot and self.main_schedule and self.timer_enable:
            print("Entered here!!!")

            current_income = self.main_schedule.money
            self.income_plot.add_point_to_income_plot(self.time,current_income)
            self.income_plot.redraw_plot()

            # self.main_schedule.

            self.time += 1
            self.disp_time.setText(str(self.time))
            self.main_schedule.update_time(self.time)

            self.main_schedule.schedule()
            self.setAlertLightStat(not self.main_schedule.alert)

            for _card_plot in self.card_list:
                for _bill in _card_plot._card_OBJ.bills:
                    _card_plot.add_REL_time(_bill.release_time,_bill.debt)
                    _card_plot.add_SOFT_deadline(_bill.deadline,_bill.debt)
                    _card_plot.add_HARD_deadline(_bill.hard_deadline,_bill.debt)










