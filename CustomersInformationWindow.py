import sys
from PIL import ImageGrab
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import ImageGrab
import os
from Database import Database

class CustomersInformationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        db = Database()
        #UI
        self.setGeometry(500, 400, 1000, 800)
        self.setWindowIcon(QIcon('./Pictures/Customers.ico'))
        self.resize(1200,500)
        self.setWindowTitle('Customers information')
        items = db.getAll()
        self.informationLabels = []
        i = 0
        for item in items:
            self.informationLabels.append([QLabel(self),QLabel(self),QLabel(self),QLabel(self),QLabel(self),QLabel(self)])
            self.informationLabels[i][0].setText(str(item[0] + 100000))
            self.informationLabels[i][1].setText(str(item[1]))
            self.informationLabels[i][2].setText(item[2])
            self.informationLabels[i][3].setText(item[3])
            self.informationLabels[i][4].setText(item[4])
            self.informationLabels[i][5].setText(item[5])
            self.informationLabels[i][0].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][1].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][2].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][3].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][4].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][5].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][0].move(0,50 + i * 50)
            self.informationLabels[i][1].move(200,50 + i * 50)
            self.informationLabels[i][2].move(400,50 + i * 50)
            self.informationLabels[i][3].move(600,50 + i * 50)
            self.informationLabels[i][4].move(800,50 + i * 50)
            self.informationLabels[i][5].move(1000,50 + i * 50)
            i += 1
        #Buttons
        # btn = QPushButton("Load",self)
        # btn.clicked.connect(self.register)
        # btn.resize(btn.sizeHint())
        # btn.move(150,350)

        #Editors' Labels
        self.show1Label = QLabel(self)
        self.show2Label = QLabel(self)
        self.show3Label = QLabel(self)
        self.show4Label = QLabel(self)
        self.show5Label = QLabel(self)
        self.show6Label = QLabel(self)
        self.show1Label.setText("ID")
        self.show2Label.setText("Age")
        self.show3Label.setText("Name")
        self.show4Label.setText("Sex")
        self.show5Label.setText("Telephone")
        self.show6Label.setText("Consumption")
        self.show1Label.move(0,0)
        self.show2Label.move(200,0)
        self.show3Label.move(400,0)
        self.show4Label.move(600,0)
        self.show5Label.move(800,0)
        self.show6Label.move(1000,0)
        self.show1Label.setFont(QFont("Microsoft Yahei",12))
        self.show2Label.setFont(QFont("Microsoft Yahei",12))
        self.show3Label.setFont(QFont("Microsoft Yahei",12))
        self.show4Label.setFont(QFont("Microsoft Yahei",12))
        self.show5Label.setFont(QFont("Microsoft Yahei",12))
        self.show6Label.setFont(QFont("Microsoft Yahei",12))


    def refresh(self):
        db = Database()
        items = db.getAll()
        i = 0
        for item in items:
            if i >= len(self.informationLabels):
                self.informationLabels.append([QLabel(self),QLabel(self),QLabel(self),QLabel(self),QLabel(self),QLabel(self)])
            self.informationLabels[i][0].setText(str(item[0] + 100000))
            self.informationLabels[i][1].setText(str(item[1]))
            self.informationLabels[i][2].setText(item[2])
            self.informationLabels[i][3].setText(item[3])
            self.informationLabels[i][4].setText(item[4])
            self.informationLabels[i][5].setText(item[5])
            self.informationLabels[i][0].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][1].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][2].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][3].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][4].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][5].setFont(QFont("Microsoft Yahei",12))
            self.informationLabels[i][0].move(0,50 + i * 50)
            self.informationLabels[i][1].move(200,50 + i * 50)
            self.informationLabels[i][2].move(400,50 + i * 50)
            self.informationLabels[i][3].move(600,50 + i * 50)
            self.informationLabels[i][4].move(800,50 + i * 50)
            self.informationLabels[i][5].move(1000,50 + i * 50)
            i += 1
