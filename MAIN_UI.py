from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel

from pyqtgraph.Qt import QtGui, QtCore

import CreditInfoWidget
from scheduling import Scheduling


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

        self.main_schedule = Scheduling(None,None,None)
        self.card_list = []# elem: [card_OBJ, plot_OBJ]

        self.MAIN_add_fields()
        self.SUB_add_field()

        self.INCOME_EDIT_BTN.clicked.connect(self.EDIT_INCOME_BTN_Event)
        self.timeFWD.clicked.connect(self.time_forward_Event)
        self.ADD_CARD_BTN.clicked.connect(self.add_card_event)


    def MAIN_add_fields(self):
        self.time_layout = QtGui.QHBoxLayout()
        self.time_layout.addWidget(QLabel("Show Time:"))
        self.disp_time = QLineEdit('0')
        self.disp_time.setEnabled(False)
        self.disp_time.setFixedWidth(50)
        self.time_layout.addWidget(self.disp_time)
        self.time_layout.addStretch()
        self.timeFWD = QPushButton("Time Go Forward")
        self.time_layout.addWidget(self.timeFWD)
        self.alertLight = QLabel("Alert Light")
        self.setAlertLightStat(True)
        self.time_layout.addWidget(self.alertLight)

        self.main_layout.addLayout(self.time_layout)

        # self.first_plot = CreditInfoWidget.CreditInfoWidget("HI",True)
        # self.main_layout.addWidget(self.first_plot)

        self.income_plot = CreditInfoWidget.CreditInfoWidget("Income", True)
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
                int(self.income_plot.income_amount.text()))
            self.income_plot.income_amount.setText('')

    def show(self):
        self.disp_time.setText(str(self.main_schedule.time))
        QtGui.QMainWindow.show(self)


    def time_forward_Event(self):
        if len(self.main_schedule.events) > 0:
            self.main_schedule.update_time(self.main_schedule.events[0].time)
            self.main_schedule.schedule()
            self.disp_time.setText(str(self.main_schedule.time))

    def add_card_event(self):
        self.close()
        self.add_credit_page.show()

    def add_new_card(self,_card):
        tmp_plot = CreditInfoWidget.CreditInfoWidget(title=_card.name)
        tmp_plot.init_main_page(self)
        tmp_plot._card_OBJ = _card
        self.main_layout.insertWidget(2,tmp_plot)
        self.card_list.append(tmp_plot)

    # def edit_card(self,_card):
    #     for idx,elem in enumerate(self.card_list):
    #         if elem[1] is _card:
    #             self.card_list[idx][0].

    # def request_card_edit(self,card_plot_widget):# Show the ADD_CARD page
    #     for elem in self.card_list:
    #         if elem[0] is card_plot_widget:
    #             self.add_credit_page.show(edit_card = elem[1])
    #             self.close()

    def request_delete(self,plot_widg):
        # TODO Call zavosh's delete function here
        plot_widg.hide()
        self.card_list.remove(plot_widg)










