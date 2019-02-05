from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel

from pyqtgraph.Qt import QtGui, QtCore

import CreditInfoWidget


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

        self.MAIN_add_fields()

        self.SUB_add_field()

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

        self.first_plot = CreditInfoWidget.CreditInfoWidget("HI")
        self.main_layout.addWidget(self.first_plot)

        self.second_plot = CreditInfoWidget.CreditInfoWidget("HI again")
        self.main_layout.addWidget(self.second_plot)

        self.main_layout.addStretch()

    def SUB_add_field(self):
        self.INCOME_EDIT_BTN = QPushButton("Edit Income")
        self.sub_layout.addWidget(self.INCOME_EDIT_BTN)

        self.GIVE_MONEY_BTN = QPushButton("Give Money")
        self.sub_layout.addWidget(self.GIVE_MONEY_BTN)

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


















