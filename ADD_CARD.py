from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel

from pyqtgraph.Qt import QtGui, QtCore

from card import Card


class ADD_CARD_UI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(300,200)

        self.MainWid = QtGui.QWidget()
        self.setCentralWidget(self.MainWid)
        self.setWindowTitle('Add Credit Card')
        self.main_main_layout = QtGui.QVBoxLayout()
        self.main_layout = QtGui.QFormLayout()
        self.main_main_layout.addLayout(self.main_layout)
        self.BTN_layout = QtGui.QHBoxLayout()
        self.main_main_layout.addLayout(self.BTN_layout)
        self.MainWid.setLayout(self.main_main_layout)

        self.MAIN_add_fields()
        self.SUB_add_fields()


    def MAIN_add_fields(self):

        self.name_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Name:'), self.name_TXTBox)

        self.bill_rel_dead_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Bill relative deadline:'), self.bill_rel_dead_TXTBox)

        self.max_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Maximum Credit:'), self.max_TXTBox)

        self.HARD_D_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Bill relative hard deadline:'), self.HARD_D_TXTBox)

        self.Bill_P_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Bill period:'), self.Bill_P_TXTBox)

        self.Min_P_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Minimum payment:'), self.Min_P_TXTBox)

        self.PP_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Penalty Percent:'), self.PP_TXTBox)

    def SUB_add_fields(self):
        self.OK_BTN = QPushButton('OK')
        self.BTN_layout.addWidget(self.OK_BTN)
        self.OK_BTN.clicked.connect(self.OK_click_event)

        self.cancel_BTN = QPushButton('Cancel')
        self.BTN_layout.addWidget(self.cancel_BTN)
        self.cancel_BTN.clicked.connect(self.cancel_BTN_Event)

    def init_page(self,main_page):
        self.main_page = main_page

    def OK_click_event(self):
        if (self.name_TXTBox.text() == '' or
            self.Bill_P_TXTBox.text() == '' or
            self.bill_rel_dead_TXTBox.text() == '' or
            self.Min_P_TXTBox.text() == '' or
            self.max_TXTBox.text() == '' or
            self.PP_TXTBox.text() == '' or
            self.HARD_D_TXTBox.text() == ''):
            return

        tmp_card = Card(
            self.name_TXTBox.text(),
            float(self.Bill_P_TXTBox.text()),
            float(self.bill_rel_dead_TXTBox.text()),
            float(self.Min_P_TXTBox.text()),
            float(self.max_TXTBox.text()),
            float(self.PP_TXTBox.text()),
            float(self.HARD_D_TXTBox.text())
        )

        self.main_page.add_new_card(tmp_card)

        self.main_page.show()
        self.close()

        # self.name_TXTBox.setText('') TODO uncomment this in the release time
        # self.Bill_P_TXTBox.setText('')
        # self.bill_rel_dead_TXTBox.setText('')
        # self.Min_P_TXTBox.setText('')
        # self.max_TXTBox.setText('')
        # self.PP_TXTBox.setText('')
        # self.HARD_D_TXTBox.setText('')

    def cancel_BTN_Event(self):
        self.main_page.show()
        self.close()

    def show(self,edit_card = None):


        # self.name_TXTBox.setText(edit_card.name)
        # self.Bill_P_TXTBox.setText(edit_card.bill_period)
        # self.bill_rel_dead_TXTBox.setText(edit_card.bill_relative_deadline)
        # self.Min_P_TXTBox.setText(edit_card.minimum_paying_first)
        # self.max_TXTBox.setText(edit_card.maximum_credit)
        # self.PP_TXTBox.setText(edit_card.penalty_percent)
        # self.HARD_D_TXTBox.setText(edit_card.bill_relative_hard_deadline)
        #
        # self.editing_card = edit_card

        QtGui.QMainWindow.show(self)


