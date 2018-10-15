# -*- coding: utf-8 -*-

import sys
from hw1_ui import Ui_MainWindow
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np

dst = None

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
        gray = cv2.GaussianBlur(img2,(3,3),0)
        cv2.imshow('Gray image', gray)

        #edge detection
        x = cv2.Sobel(gray,cv2.CV_16S,1,0)
        y = cv2.Sobel(gray,cv2.CV_16S,0,1)
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        cv2.imshow("Vertical edges", absX)
        cv2.imshow("Horizontal edges", absY)

        #magnitude
        def threshold_f(self):
            global dst
            threshold_val = cv2.getTrackbarPos('threshold', 'magnitude')
            ret, magnitude = cv2.threshold(dst, threshold_val, 255, cv2.THRESH_TOZERO)
            cv2.imshow("Magnitude_result", magnitude)
        
        global dst
        dst = cv2.addWeighted(absX,0.5,absY,0.5,0)
        cv2.namedWindow('magnitude')
        cv2.createTrackbar('threshold', 'magnitude', 0, 255, threshold_f)
        
        

    def on_btn3_1_click(self):
        img3 = cv2.imread('images/pyramids_Gray.jpg')

        #level 1 gaussian
        G1 = cv2.GaussianBlur(img3,(5,5),0)
        G1 = cv2.pyrDown(G1)
        cv2.imshow('level 1 Gaussian', G1)

        #level 0 laplacian
        G1_Up = cv2.pyrUp(G1)
        G1_Up = cv2.GaussianBlur(G1_Up,(5,5),0)
        L0 = cv2.subtract(img3, G1_Up)
        cv2.imshow('level 0 Laplace', L0)

        #level 1 inverse
        G2 = cv2.GaussianBlur(G1, (5,5), 0)
        G2 = cv2.pyrDown(G2)
        G2_Up = cv2.pyrUp(G2)
        G2_Up = cv2.GaussianBlur(G2_Up, (5,5), 0)
        L1 = cv2.subtract(G1, G2_Up)
        Inv1 = cv2.add(L1,G2_Up)
        cv2.imshow('level 1 inverse', Inv1)

        #level 0 inverse
        Inv1_Up = cv2.pyrUp(Inv1)
        Inv1_Up = cv2.GaussianBlur(Inv1_Up, (5,5), 0)
        Inv0 = cv2.add(L0,Inv1_Up)
        cv2.imshow('level 0 inverse', Inv0)

    def on_btn4_1_click(self):
        #load origin pic and convert to gray space
        img4_1 = cv2.imread('images/QR.png')
        cv2.imshow('origin', img4_1)
        img4_1 = cv2.cvtColor(img4_1, cv2.COLOR_RGB2GRAY)
        ret,dst4_1 = cv2.threshold(img4_1, 80, 255, cv2.THRESH_TOZERO)
        cv2.imshow('problem 4.1', dst4_1)

    def on_btn4_2_click(self):
        #load origin pic and convert to gray space
        img4_2 = cv2.imread('images/QR.png')
        cv2.imshow('origin', img4_2)
        img4_2 = cv2.cvtColor(img4_2, cv2.COLOR_RGB2GRAY)
        dst4_2 = cv2.adaptiveThreshold(img4_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
        cv2.THRESH_BINARY, 19, -1)
        cv2.imshow('problem 4.2', dst4_2)

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
