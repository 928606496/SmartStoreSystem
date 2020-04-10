# A class to load information of new customer into database
import sys
from PIL import ImageGrab
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import ImageGrab
import os
from Face import Face
from Database import Database

class LoadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.database = None
        self.extensive_name = None
        self.file_name = None

    def initUI(self):
        #UI
        self.setGeometry(800, 400, 400, 400)
        self.setWindowTitle('Load information')
        self.setWindowIcon(QIcon('./Pictures/Upload.ico'))

        #Buttons
        btn = QPushButton("Load",self)
        btn.clicked.connect(self.register)
        btn.resize(btn.sizeHint())
        btn.move(150,350)

        #Editors' Labels
        self.edit2Label = QLabel(self)
        self.edit3Label = QLabel(self)
        self.edit4Label = QLabel(self)
        self.edit5Label = QLabel(self)
        self.edit6Label = QLabel(self)
        self.edit2Label.setText("Age:")
        self.edit3Label.setText("Name:")
        self.edit4Label.setText("Sex    :")
        self.edit5Label.setText("Telephone:")
        self.edit6Label.setText("Consumption:")
        self.edit2Label.move(0,50)
        self.edit3Label.move(0,100)
        self.edit4Label.move(0,150)
        self.edit5Label.move(0,200)
        self.edit6Label.move(0,250)
        self.edit2Label.setFont(QFont("Microsoft Yahei",12))
        self.edit3Label.setFont(QFont("Microsoft Yahei",12))
        self.edit4Label.setFont(QFont("Microsoft Yahei",12))
        self.edit5Label.setFont(QFont("Microsoft Yahei",12))
        self.edit6Label.setFont(QFont("Microsoft Yahei",12))

        self.edit2 = QTextEdit(self)
        self.edit3 = QTextEdit(self)
        self.edit4 = QTextEdit(self)
        self.edit5 = QTextEdit(self)
        self.edit6 = QTextEdit(self)
        self.edit2.setFont(QFont("Microsoft Yahei",12))
        self.edit3.setFont(QFont("Microsoft Yahei",12))
        self.edit4.setFont(QFont("Microsoft Yahei",12))
        self.edit5.setFont(QFont("Microsoft Yahei",12))
        self.edit6.setFont(QFont("Microsoft Yahei",12))
        self.edit2.resize(200,40)
        self.edit3.resize(200,40)
        self.edit4.resize(200,40)
        self.edit5.resize(200,40)
        self.edit6.resize(200,40)
        self.edit2.move(150,50)
        self.edit3.move(150,100)
        self.edit4.move(150,150)
        self.edit5.move(150,200)
        self.edit6.move(150,250)

        self.registerLabel = QLabel(self)
        self.registerLabel.setText("Input please!")
        self.registerLabel.move(150,300)
        self.registerLabel.resize(200,40)
        self.registerLabel.setFont(QFont("Microsoft Yahei",12))

    def getInformation(self,database,extensive_name):
        self.database = database
        self.extensive_name = extensive_name


    def register(self):
        self.database.insert(self.edit2.toPlainText(),self.edit3.toPlainText(),self.edit4.toPlainText(),self.edit5.toPlainText(),self.edit6.toPlainText())
        self.registerLabel.setText("Input successfully!")
        file_name = self.edit3.toPlainText() + self.extensive_name
        os.system("ren Capture.png " + file_name)
        print(file_name)
        os.system("move " + file_name + " .\Faces")
        