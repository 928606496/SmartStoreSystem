from Face import Face
from GUI import GUIQWidget
import sys
from PIL import ImageGrab
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from LoadWindow import LoadWindow
from CustomersInformationWindow import CustomersInformationWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    load = LoadWindow()
    ciw = CustomersInformationWindow()
    GUI = GUIQWidget(load,ciw)
    GUI.show()
    sys.exit(app.exec_())
