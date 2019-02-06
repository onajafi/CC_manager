from PyQt5.QtWidgets import QPushButton, QScrollArea, QLineEdit, QLabel

from pyqtgraph.Qt import QtGui, QtCore

from scheduling import Scheduling

class INCOME_PAGE_UI(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(300,200)

        self.MainWid = QtGui.QWidget()
        self.setCentralWidget(self.MainWid)
        self.setWindowTitle('Enter Income Info')
        self.main_layout = QtGui.QVBoxLayout()
        self.MainWid.setLayout(self.main_layout)

        self.add_fields()
        self.OKBTN.clicked.connect(self.OK_clicked)


    def add_fields(self):
        self.firstF_layout = QtGui.QHBoxLayout()
        self.firstF_layout.addWidget(QLabel('Income Period:'))
        self.FirstTXTBox = QLineEdit('')
        self.firstF_layout.addWidget(self.FirstTXTBox)
        self.main_layout.addLayout(self.firstF_layout)

        self.SecondF_layout = QtGui.QHBoxLayout()
        self.SecondF_layout.addWidget(QLabel('Minimum Income:'))
        self.SecondTXTBox = QLineEdit('')
        self.SecondF_layout.addWidget(self.SecondTXTBox)
        self.main_layout.addLayout(self.SecondF_layout)

        self.ThirdF_layout = QtGui.QHBoxLayout()
        self.ThirdF_layout.addWidget(QLabel('Maximum Income:'))
        self.ThirdTXTBox = QLineEdit('')
        self.ThirdF_layout.addWidget(self.ThirdTXTBox)
        self.main_layout.addLayout(self.ThirdF_layout)

        self.OKBTN = QPushButton("OK")
        self.main_layout.addWidget(self.OKBTN)

        self.main_layout.addStretch()

    def OK_clicked(self):
        if(self.FirstTXTBox.text() == '' or
           self.SecondTXTBox.text() == '' or
           self.ThirdTXTBox.text() == ''):
            return

        self.close()
        self.main_page.show()
        # Making the Schedule OBJ
        self.main_page.main_schedule = Scheduling(int(self.FirstTXTBox.text()),
                                                  int(self.SecondTXTBox.text()),
                                                  int(self.ThirdTXTBox.text()))


    def initPages(self,MainPage):
        self.main_page = MainPage




