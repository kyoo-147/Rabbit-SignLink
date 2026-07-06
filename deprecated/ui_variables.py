# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'last_ui_rabbitTcIXtd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import test_rc
import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1382, 793)
        font = QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        MainWindow.setIconSize(QSize(30, 30))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_tutorialView = QLabel(self.centralwidget)
        self.label_tutorialView.setObjectName(u"label_tutorialView")
        self.label_tutorialView.setGeometry(QRect(360, 370, 301, 191))
        self.label_tutorialView.setStyleSheet(u"background-color: transparent;")
        self.label_tutorialView.setAlignment(Qt.AlignCenter)
        self.label_camView = QLabel(self.centralwidget)
        self.label_camView.setObjectName(u"label_camView")
        self.label_camView.setGeometry(QRect(10, 120, 801, 411))
        self.label_camView.setStyleSheet(u"background-color: rgba(180,180,180,0.6);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 580, 1051, 41))
        self.progressBar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.progressBar.setValue(24)
        self.label_doneTutorial = QLabel(self.centralwidget)
        self.label_doneTutorial.setObjectName(u"label_doneTutorial")
        self.label_doneTutorial.setGeometry(QRect(10, 120, 801, 411))
        self.label_doneTutorial.setStyleSheet(u"background-color: rgba(217,217,217);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.label_doneTutorial.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(820, 120, 251, 411))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"border-top-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.button_A = QPushButton(self.groupBox)
        self.button_A.setObjectName(u"button_A")
        self.button_A.setGeometry(QRect(0, 30, 50, 50))
        self.button_A.setAutoFillBackground(False)
        self.button_A.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_B = QPushButton(self.groupBox)
        self.button_B.setObjectName(u"button_B")
        self.button_B.setGeometry(QRect(50, 30, 50, 50))
        self.button_B.setAutoFillBackground(False)
        self.button_B.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_C = QPushButton(self.groupBox)
        self.button_C.setObjectName(u"button_C")
        self.button_C.setGeometry(QRect(100, 30, 50, 50))
        self.button_C.setAutoFillBackground(False)
        self.button_C.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_D = QPushButton(self.groupBox)
        self.button_D.setObjectName(u"button_D")
        self.button_D.setGeometry(QRect(150, 30, 50, 50))
        self.button_D.setAutoFillBackground(False)
        self.button_D.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_E = QPushButton(self.groupBox)
        self.button_E.setObjectName(u"button_E")
        self.button_E.setGeometry(QRect(200, 30, 50, 50))
        self.button_E.setAutoFillBackground(False)
        self.button_E.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_F = QPushButton(self.groupBox)
        self.button_F.setObjectName(u"button_F")
        self.button_F.setGeometry(QRect(0, 90, 50, 50))
        self.button_F.setAutoFillBackground(False)
        self.button_F.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_G = QPushButton(self.groupBox)
        self.button_G.setObjectName(u"button_G")
        self.button_G.setGeometry(QRect(50, 90, 50, 50))
        self.button_G.setAutoFillBackground(False)
        self.button_G.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_H = QPushButton(self.groupBox)
        self.button_H.setObjectName(u"button_H")
        self.button_H.setGeometry(QRect(100, 90, 50, 50))
        self.button_H.setAutoFillBackground(False)
        self.button_H.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_I = QPushButton(self.groupBox)
        self.button_I.setObjectName(u"button_I")
        self.button_I.setGeometry(QRect(150, 90, 50, 50))
        self.button_I.setAutoFillBackground(False)
        self.button_I.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_J = QPushButton(self.groupBox)
        self.button_J.setObjectName(u"button_J")
        self.button_J.setGeometry(QRect(200, 90, 50, 50))
        self.button_J.setAutoFillBackground(False)
        self.button_J.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_K = QPushButton(self.groupBox)
        self.button_K.setObjectName(u"button_K")
        self.button_K.setGeometry(QRect(0, 150, 50, 50))
        self.button_K.setAutoFillBackground(False)
        self.button_K.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_L = QPushButton(self.groupBox)
        self.button_L.setObjectName(u"button_L")
        self.button_L.setGeometry(QRect(50, 150, 50, 50))
        self.button_L.setAutoFillBackground(False)
        self.button_L.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_M = QPushButton(self.groupBox)
        self.button_M.setObjectName(u"button_M")
        self.button_M.setGeometry(QRect(100, 150, 50, 50))
        self.button_M.setAutoFillBackground(False)
        self.button_M.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_N = QPushButton(self.groupBox)
        self.button_N.setObjectName(u"button_N")
        self.button_N.setGeometry(QRect(150, 150, 50, 50))
        self.button_N.setAutoFillBackground(False)
        self.button_N.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_O = QPushButton(self.groupBox)
        self.button_O.setObjectName(u"button_O")
        self.button_O.setGeometry(QRect(200, 150, 50, 50))
        self.button_O.setAutoFillBackground(False)
        self.button_O.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_P = QPushButton(self.groupBox)
        self.button_P.setObjectName(u"button_P")
        self.button_P.setGeometry(QRect(0, 210, 50, 50))
        self.button_P.setAutoFillBackground(False)
        self.button_P.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_Q = QPushButton(self.groupBox)
        self.button_Q.setObjectName(u"button_Q")
        self.button_Q.setGeometry(QRect(50, 210, 50, 50))
        self.button_Q.setAutoFillBackground(False)
        self.button_Q.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_R = QPushButton(self.groupBox)
        self.button_R.setObjectName(u"button_R")
        self.button_R.setGeometry(QRect(100, 210, 50, 50))
        self.button_R.setAutoFillBackground(False)
        self.button_R.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_S = QPushButton(self.groupBox)
        self.button_S.setObjectName(u"button_S")
        self.button_S.setGeometry(QRect(150, 210, 50, 50))
        self.button_S.setAutoFillBackground(False)
        self.button_S.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_T = QPushButton(self.groupBox)
        self.button_T.setObjectName(u"button_T")
        self.button_T.setGeometry(QRect(200, 210, 50, 50))
        self.button_T.setAutoFillBackground(False)
        self.button_T.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_U = QPushButton(self.groupBox)
        self.button_U.setObjectName(u"button_U")
        self.button_U.setGeometry(QRect(0, 270, 50, 50))
        self.button_U.setAutoFillBackground(False)
        self.button_U.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_V = QPushButton(self.groupBox)
        self.button_V.setObjectName(u"button_V")
        self.button_V.setGeometry(QRect(50, 270, 50, 50))
        self.button_V.setAutoFillBackground(False)
        self.button_V.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_W = QPushButton(self.groupBox)
        self.button_W.setObjectName(u"button_W")
        self.button_W.setGeometry(QRect(100, 270, 50, 50))
        self.button_W.setAutoFillBackground(False)
        self.button_W.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_X = QPushButton(self.groupBox)
        self.button_X.setObjectName(u"button_X")
        self.button_X.setGeometry(QRect(150, 270, 50, 50))
        self.button_X.setAutoFillBackground(False)
        self.button_X.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_Y = QPushButton(self.groupBox)
        self.button_Y.setObjectName(u"button_Y")
        self.button_Y.setGeometry(QRect(200, 270, 50, 50))
        self.button_Y.setAutoFillBackground(False)
        self.button_Y.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.button_Z = QPushButton(self.groupBox)
        self.button_Z.setObjectName(u"button_Z")
        self.button_Z.setGeometry(QRect(0, 330, 50, 50))
        self.button_Z.setAutoFillBackground(False)
        self.button_Z.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 540, 81, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 630, 291, 71))
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"border-top-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.label_recognizedText = QLabel(self.groupBox_2)
        self.label_recognizedText.setObjectName(u"label_recognizedText")
        self.label_recognizedText.setGeometry(QRect(50, 30, 191, 31))
        self.label_recognizedText.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_recognizedText.setAlignment(Qt.AlignCenter)
        self.label_recognizedText.setWordWrap(False)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(440, 730, 551, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.label_7.setFont(font2)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1361, 61))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1290, 10, 41, 41))
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/OIP.jpeg);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 41, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"image: url(:/newPrefix/logo_com.png);\n"
"")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1170, 20, 111, 25))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 20, 111, 21))
        font3 = QFont()
        font3.setFamily(u"Ubuntu")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color:rgb(78, 154, 6)")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 80, 121, 31))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(1080, 120, 291, 581))
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"border-top-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.label_recognizedText_2 = QLabel(self.groupBox_3)
        self.label_recognizedText_2.setObjectName(u"label_recognizedText_2")
        self.label_recognizedText_2.setGeometry(QRect(20, 20, 251, 511))
        self.label_recognizedText_2.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_recognizedText_2.setAlignment(Qt.AlignCenter)
        self.label_recognizedText_2.setWordWrap(False)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1090, 80, 121, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(320, 630, 751, 71))
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setStyleSheet(u"border-top-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.label_recognizedText_4 = QLabel(self.groupBox_4)
        self.label_recognizedText_4.setObjectName(u"label_recognizedText_4")
        self.label_recognizedText_4.setGeometry(QRect(20, 30, 491, 31))
        self.label_recognizedText_4.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_recognizedText_4.setAlignment(Qt.AlignCenter)
        self.label_recognizedText_4.setWordWrap(False)
        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(680, 30, 61, 31))
        self.pushButton_5.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(610, 30, 61, 31))
        self.pushButton_6.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(520, 30, 81, 31))
        self.pushButton_7.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox.raise_()
        self.label_camView.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        self.groupBox_2.raise_()
        self.label_tutorialView.raise_()
        self.label_doneTutorial.raise_()
        self.label_7.raise_()
        self.frame.raise_()
        self.label_8.raise_()
        self.groupBox_3.raise_()
        self.label_10.raise_()
        self.groupBox_4.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_tutorialView.setText("")
        self.label_camView.setText("")
        self.label_doneTutorial.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea3ng K\u00ed Hi\u1ec7u Ng\u00f4n Ng\u1eef", None))
        self.button_A.setText("")
        self.button_B.setText("")
        self.button_C.setText("")
        self.button_D.setText("")
        self.button_E.setText("")
        self.button_F.setText("")
        self.button_G.setText("")
        self.button_H.setText("")
        self.button_I.setText("")
        self.button_J.setText("")
        self.button_K.setText("")
        self.button_L.setText("")
        self.button_M.setText("")
        self.button_N.setText("")
        self.button_O.setText("")
        self.button_P.setText("")
        self.button_Q.setText("")
        self.button_R.setText("")
        self.button_S.setText("")
        self.button_T.setText("")
        self.button_U.setText("")
        self.button_V.setText("")
        self.button_W.setText("")
        self.button_X.setText("")
        self.button_Y.setText("")
        self.button_Z.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"V\u0103n B\u1ea3n Nh\u1eadn Di\u1ec7n:", None))
        self.label_recognizedText.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"We may make mistakes, but we will try to fix them.", None))
        self.pushButton.setText("")
        self.label_3.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"LogIn/LogOut", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RabbitAI", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Camera View", None))
        self.groupBox_3.setTitle("")
        self.label_recognizedText_2.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Chat View", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Chu\u1ed7i V\u0103n B\u1ea3n Hi\u1ec7n T\u1ea1i Nh\u1eadn \u0110\u01b0\u1ee3c:", None))
        self.label_recognizedText_4.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"G\u1eedi", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ec9nh s\u1eeda", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

