import sys
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget , QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from face_rec import runcam2
from ui_imp_facerecog import VideoThread
import numpy as np
import cv2

class MyApp(QWidget):
    def __init__(self) :
        super().__init__()
        uic.loadUi('GUI.ui',self)
        
        self.cams.clicked.connect(self.runcam)
        self.cams.clicked.connect(runcam2)

    def runcam(self):
            runcam2
            cams.show()
            

class MyCam(QWidget):
    def __init__(self):
         super().__init__()
         uic.loadUi('cams.ui',self)
         runcam2
    #      width = 640
    #      height = 480
    #      self.image_label = QLabel(self)
    #      self.textlabel = QLabel('demo')

    #      vbox = QVBoxLayout()
    #      vbox.addWidget(self.image_label)
    #      vbox.addWidget(self.textlabel)

    #      self.setLayout(vbox)

    #      self.thread = VideoThread()
    #      self.thread.change_pixmap_signal.connect(self.update_image)
    #      self.thread.start()

    # def closeEvent(self, event):
    #     self.thread.stop()
    #     event.accept()



    # @pyqtSlot(np.ndarray)
    # def update_image(self, cv_img):
    #     """Updates the image_label with a new opencv image"""
    #     qt_img = self.convert_cv_qt(cv_img)
    #     self.image_label.setPixmap(qt_img)
    
    # def convert_cv_qt(self, cv_img):
    #     """Convert from an opencv image to QPixmap"""
    #     rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    #     h, w, ch = rgb_image.shape
    #     bytes_per_line = ch * w
    #     convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
    #     p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
    #     return QPixmap.fromImage(p)

app = QApplication(sys.argv)

myApp = MyApp()
myApp.show()

cams = MyCam()

sys.exit(app.exec())