# -*- coding: utf-8 -*-

import sys
from hw1_ui import Ui_MainWindow
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    # Write your code below
    # UI components are defined in hw1_ui.py, please take a look.
    # You can also open hw1.ui by qt-designer to check ui components.

    def onBindingUI(self):
        self.btn1_1.clicked.connect(self.on_btn1_1_click)
        self.btn1_2.clicked.connect(self.on_btn1_2_click)
        self.btn1_3.clicked.connect(self.on_btn1_3_click)
        self.btn1_4.clicked.connect(self.on_btn1_4_click)
        self.btn2_1.clicked.connect(self.on_btn2_1_click)
        self.btn3_1.clicked.connect(self.on_btn3_1_click)
        self.btn4_1.clicked.connect(self.on_btn4_1_click)
        self.btn4_2.clicked.connect(self.on_btn4_2_click)
        self.btn5_1.clicked.connect(self.on_btn5_1_click)
        self.btn5_2.clicked.connect(self.on_btn5_2_click)

    # button for problem 1.1
    def on_btn1_1_click(self):
        img1_1 = cv2.imread('images/dog.bmp')
        cv2.imshow('problm 1.1', img1_1)
        height, width, channels = img1_1.shape
        print('Height : {:d}'.format(height))
        print('Width  : {:d}'.format(width)) 
 
    def on_btn1_2_click(self):
        img1_2 = cv2.imread('images/color.png')
        b, g, r = cv2.split(img1_2)
        img1_2 = cv2.merge((g,r,b))
        cv2.imshow('problm 1.2', img1_2)

    def on_btn1_3_click(self):
        img1_3 = cv2.imread('images/dog.bmp')
        img1_3 = cv2.flip(img1_3,1)
        cv2.imshow('problm 1.3', img1_3)

    def on_btn1_4_click(self):
        def mix(self):
            origin = cv2.imread('images/dog.bmp')
            flip = cv2.flip(origin,1)
            a = cv2.getTrackbarPos('blending', 'blend')/10000
            b = 1-a
            cv2.addWeighted(origin, a, flip, b, 0.0, origin)
            cv2.imshow('problm 1.4', origin)

        cv2.namedWindow('blend')
        cv2.createTrackbar('blending', 'blend', 0, 10000, mix)
        
    def on_btn2_1_click(self):
        img2 = cv2.imread('images/M8.jpg') 
        img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
        cv2.imshow('hi',img2)

    def on_btn3_1_click(self):
        pass

    def on_btn4_1_click(self):
        pass

    def on_btn4_2_click(self):
        pass

    def on_btn5_1_click(self):
        # edtAngle, edtScale. edtTx, edtTy to access to the ui object
        pass

    def on_btn5_2_click(self):
        pass

    ### ### ###


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
