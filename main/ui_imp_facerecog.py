
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import cv2

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture('security.mp4')
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)

