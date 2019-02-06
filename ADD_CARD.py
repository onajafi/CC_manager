from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel

from pyqtgraph.Qt import QtGui, QtCore


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

        self.FirstTXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Name:'), self.FirstTXTBox)

        self.SecondTXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Bill relative deadline:'), self.SecondTXTBox)

        self.thirdTXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Minimum Credit:'), self.thirdTXTBox)

        self.HARD_D_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Bill relative hard deadline:'), self.HARD_D_TXTBox)

        self.Bill_P_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Bill period:'), self.Bill_P_TXTBox)

        self.Min_P_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Minimum payment:'), self.Min_P_TXTBox)

        self.PP_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Penalty Percent:'), self.PP_TXTBox)

        self.PP_TXTBox = QLineEdit('')
        self.main_layout.addRow(QLabel('Penalty Percent:'), self.PP_TXTBox)

        #
        # self.ThirdF_layout = QtGui.QHBoxLayout()
        # self.ThirdF_layout.addWidget(QLabel('Maximum Income:'))
        # self.ThirdTXTBox = QLineEdit('')
        # self.ThirdF_layout.addWidget(self.ThirdTXTBox)
        # self.main_layout.addLayout(self.ThirdF_layout)
        #
        # self.OKBTN = QPushButton("OK")
        # self.main_layout.addWidget(self.OKBTN)
        #
        # self.main_layout.addStretch()

    def SUB_add_fields(self):
        self.OK_BTN = QPushButton('OK')
        self.BTN_layout.addWidget(self.OK_BTN)
        self.Cancel_BTN = QPushButton('Cancel')
        self.BTN_layout.addWidget(self.Cancel_BTN)


