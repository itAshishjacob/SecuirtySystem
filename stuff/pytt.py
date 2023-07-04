from PyQt6.QtWidgets import QApplication, QWidget , QLabel, QVBoxLayout
import sys
from PyQt6 import uic

class MyApp(QWidget):
    def __init__(self) :
        super().__init__()
        uic.loadUi('untitled.ui',self)


app = QApplication(sys.argv)

myApp = MyApp()
myApp.show()

sys.exit(app.exec())