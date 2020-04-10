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
from LoadWindow import LoadWindow
from FaceDetection import FaceDetection
from DrawChart import DrawChart
from CustomersInformationWindow import CustomersInformationWindow
from OutputFlowrateRecord import OutputFlowrateRecord
import time
import cv2 as cv

class GUIQWidget(QMainWindow):

    def __init__(self,load,ciw):
        super().__init__()

        self.initUI()
        self.database = Database()
        self.load = load
        self.ciw = ciw

        self.currentId = None
        self.currentAge = None
        self.currentName = None
        self.currentSex = None
        self.currentTelephone = None
        self.currentConsumption = None

        self.c_name = None

    def initUI(self):

        #MainWindow
        self.setGeometry(500, 50, 1100, 1000)
        self.setWindowTitle('Smart store')
        self.move(800,0)
        self.setWindowIcon(QIcon('./Pictures/Icon.png'))
        #Buttons
        qbtn = QPushButton('Search', self)
        qbtn.clicked.connect(self.search)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(600, 900)       

        btn3 = QPushButton('Capture',self)
        btn3.clicked.connect(self.capture)
        btn3.resize(btn3.sizeHint())
        btn3.move(500,900)

        btn4 = QPushButton('Settle',self)
        btn4.clicked.connect(self.settleAccount)
        btn4.resize(btn4.sizeHint())
        btn4.move(100,800)

        btn5 = QPushButton('Detect',self)
        btn5.clicked.connect(self.faceDetect)
        btn5.resize(btn5.sizeHint())
        btn5.move(300,800)

        btn6 = QPushButton('CreateChart',self)
        btn6.clicked.connect(self.createChart)
        btn6.resize(150,30)
        btn6.move(275,900)

        btn7 = QPushButton('ShowCustomers',self)
        btn7.clicked.connect(self.showCustomersInformation)
        btn7.resize(150,30)
        btn7.move(700,900)

        btn8 = QPushButton('OutputFlowrate',self)
        btn8.clicked.connect(self.outputFlowrateRecord)
        btn8.resize(150,30)
        btn8.move(900,900)
        
        #CheckBox
        self.commodities = ['Coke','Sprite','Hambuger','Cake','Coffee','Steak']
        self.price = [3,3,12,20,20,100]
        self.cbs = []
        # self.cbAll = QCheckBox('All',self)
        for com in self.commodities:
            self.cbs.append(QCheckBox(com,self))
        for cb in self.cbs:
            cb.setChecked(False)
        # self.cbAll.move(0,650)
        self.cbs[0].move(0,700)
        self.cbs[1].move(100,700)
        self.cbs[2].move(200,700)
        self.cbs[3].move(0,750)
        self.cbs[4].move(100,750)
        self.cbs[5].move(200,750)
        
        # self.cbAll.stateChanged.connect(self.checkAll)
        # for cb in self.cbs:
        #     cb.stateChanged.connect(self.cbChange)

        #Picture
        self.customer = QLabel(self)
        self.customer.setFixedSize(500, 500)
        self.showCurrentCustomer("User.jpg")
        self.customer.move(0, 0)

        #Labels
        #Show Labels
        self.text1 = QLabel(self)
        self.text2 = QLabel(self)
        self.text3 = QLabel(self)
        self.text4 = QLabel(self)
        self.text5 = QLabel(self)
        self.text6 = QLabel(self)
        self.text1.setText("ID        :")
        self.text2.setText("Age:     ")
        self.text3.setText("Name   :")
        self.text4.setText("Sex      :")
        self.text5.setText("Telephone:")
        self.text6.setText("Consumption:")
        self.text1.setFont(QFont("Microsoft Yahei",20))
        self.text2.setFont(QFont("Microsoft Yahei",20))
        self.text3.setFont(QFont("Microsoft Yahei",20))
        self.text4.setFont(QFont("Microsoft Yahei",20))
        self.text5.setFont(QFont("Microsoft Yahei",20))
        self.text6.setFont(QFont("Microsoft Yahei",20))
        self.text1.resize(300,50)
        self.text2.resize(300,50)
        self.text3.resize(300,50)
        self.text4.resize(300,50)
        self.text5.resize(300,50)
        self.text6.resize(300,50)
        self.text1.move(500,0)
        self.text2.move(500,50)
        self.text3.move(500,100)
        self.text4.move(500,150)
        self.text5.move(500,200)
        self.text6.move(500,250)


        #Customer information
        self.customerId = QLabel(self)
        self.customerAge = QLabel(self)
        self.customerName = QLabel(self)
        self.customerSex = QLabel(self)
        self.customerTelephone = QLabel(self)
        self.customerConsumption = QLabel(self)
        self.customerId.setText("-----")
        self.customerAge.setText("-----")
        self.customerName.setText("-----")
        self.customerSex.setText("-----")
        self.customerTelephone.setText("-----")
        self.customerConsumption.setText("-----")
        self.customerId.setFont(QFont("Microsoft Yahei",20))
        self.customerAge.setFont(QFont("Microsoft Yahei",20))
        self.customerName.setFont(QFont("Microsoft Yahei",20))
        self.customerSex.setFont(QFont("Microsoft Yahei",20))
        self.customerTelephone.setFont(QFont("Microsoft Yahei",20))
        self.customerConsumption.setFont(QFont("Microsoft Yahei",20))
        self.customerId.resize(300,50)
        self.customerAge.resize(300,50)
        self.customerName.resize(300,50)
        self.customerSex.resize(300,50)
        self.customerTelephone.resize(300,50)
        self.customerConsumption.resize(300,50)
        self.customerId.move(750,0)
        self.customerAge.move(750,50)
        self.customerName.move(750,100)
        self.customerSex.move(750,150)
        self.customerTelephone.move(750,200)
        self.customerConsumption.move(750,250)


        #Operation Tips
        self.captureLabel = QLabel(self)
        self.captureLabel.setText("Wait to capture")
        self.captureLabel.move(600,800)
        self.captureLabel.resize(200,40)
        self.captureLabel.setFont(QFont("Microsoft Yahei",12))
        self.commoditiesLabel = QLabel(self)
        self.commoditiesLabel.setText("Commodities")
        self.commoditiesLabel.move(100,650)
        self.commoditiesLabel.resize(200,40)
        self.commoditiesLabel.setFont((QFont("Microsoft Yahei",12)))

        #Number of faces
        self.faceNumber = QLabel(self)
        self.faceNumber.setText("The number of faces is ")
        self.faceNumber.move(600,850)
        self.faceNumber.resize(400,40)
        self.faceNumber.setFont(QFont("Microsoft Yahei",12))

        #Show camera
        self.timer_camera = QTimer()
        self.timer_camera.timeout.connect(self.showCamera)
        self.timer_camera.start(30)
        self.cap = cv.VideoCapture(0)
        self.camera = QLabel(self)
        self.camera.setText("Waiting to open the camera...")
        self.camera.resize(600,300)
        self.camera.move(500,400)
        self.showCamera()

    
    def search(self):
        faceTest = Face()
        JPG = "Capture.png"
        path = faceTest.search(JPG)
        # If this customer has been existed in the faces directory

        if path != None:
            #Show the picture of current customer
            self.getCustomerInfor(path)
            
        # If not,load into the directory
        else:
            extensive_name = JPG[len(JPG)-4:len(JPG)]
            self.loadEvent(extensive_name)
            print("Loaded successfully!")

    def showCurrentCustomer(self,path):
        
        pic = QPixmap(path).scaled(self.customer.width(), self.customer.height())
        self.customer.setPixmap(pic)

    def capture(self):
        bbox = (800+500,400,800+1100,800)

        im = ImageGrab.grab(bbox)

        im.save("Capture.png")

        self.captureLabel.setText("Caputured successfully!")

    def loadEvent(self,extensive_name):
        self.load.show()
        self.load.getInformation(self.database,extensive_name)

    def getCustomerInfor(self, path):
        self.showCurrentCustomer(path)
        self.currentName = path[8:len(path) - 4]
        print(self.currentName)
        items = self.database.get(self.currentName)
        self.currentId = str(items[0][0])
        self.currentAge = str(items[0][1])
        self.currentName = items[0][2]
        self.currentSex = items[0][3]
        self.currentTelephone = items[0][4]
        self.currentConsumption = items[0][5]
        self.customerId.setText(str(items[0][0] + 100000))
        self.customerAge.setText(str(items[0][1]))
        self.customerName.setText(items[0][2])
        self.customerSex.setText(items[0][3])
        self.customerTelephone.setText(items[0][4])
        self.customerConsumption.setText(items[0][5])


    def settleAccount(self):
        account = 0
        i = 0
        for cb in self.cbs:
            if cb.isChecked() == True:
                account +=  self.price[i]
                cb.setChecked(False)
            i += 1
        items = self.database.get(self.currentName)
        self.currentId = str(items[0][0])
        self.currentAge = str(items[0][1])
        self.currentName = items[0][2]
        self.currentSex = items[0][3]
        self.currentTelephone = items[0][4]
        self.currentConsumption = items[0][5]
        self.database.update(str(account + int(self.currentConsumption)),self.currentId)
        tip = ('Settle successfully!\n Total price:' + str(account) +"\nAccount id:" + str(int(self.currentId) + 100000) + "\nCustomer name:" + self.currentName)
        QMessageBox.information(self,'Tip',tip)

    def faceDetect(self):
        faceDetection = FaceDetection()
        bbox = (0,0,800,1080)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print(current_time)
        im = ImageGrab.grab(bbox)

        im.save("Detection.png")

        faceNum = faceDetection.detect()
        self.database.flowrate_insert(str(faceNum),current_time)
        print(faceNum)
        self.faceNumber.setText("The number of faces is " + str(faceNum))

        self.captureLabel.setText("Detected successfully!")

    def createChart(self):
        dc = DrawChart(self.database)
        dc.draw()
        os.system('.\Flowrate_Chart.svg')

    def showCamera(self):
        flag,image = self.cap.read()  # Read from the video stream
 
        show = cv.resize(image,(640,480))     #reset the size of the frame to (640,480)
        show = cv.cvtColor(show,cv.COLOR_BGR2RGB) #set RGB,true color
        showImage = QImage(show.data,show.shape[1],show.shape[0],QImage.Format_RGB888) #Change the video data read into QImage form
        self.camera.setPixmap(QPixmap.fromImage(showImage))  #Show QImage in the Label

    def showCustomersInformation(self):
        self.ciw.refresh()
        self.ciw.show()

    def outputFlowrateRecord(self):
        ofr = OutputFlowrateRecord()
        ofr.output()
        os.system('FlowrateRecord.txt')
