# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ac_button = QtWidgets.QPushButton(self.centralwidget)
        self.ac_button.setGeometry(QtCore.QRect(40, 30, 111, 32))
        self.ac_button.setCheckable(True)
        self.ac_button.setObjectName("ac_button")
        self.bpm_slider = QtWidgets.QSlider(self.centralwidget)
        self.bpm_slider.setGeometry(QtCore.QRect(310, 80, 171, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bpm_slider.sizePolicy().hasHeightForWidth())
        self.bpm_slider.setSizePolicy(sizePolicy)
        self.bpm_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bpm_slider.setObjectName("bpm_slider")
        self.bpm_label = QtWidgets.QLabel(self.centralwidget)
        self.bpm_label.setGeometry(QtCore.QRect(50, 80, 121, 16))
        self.bpm_label.setObjectName("bpm_label")
        self.simv_button = QtWidgets.QPushButton(self.centralwidget)
        self.simv_button.setGeometry(QtCore.QRect(180, 30, 111, 32))
        self.simv_button.setCheckable(True)
        self.simv_button.setObjectName("simv_button")
        self.tv_label = QtWidgets.QLabel(self.centralwidget)
        self.tv_label.setGeometry(QtCore.QRect(50, 140, 121, 16))
        self.tv_label.setObjectName("tv_label")
        self.tv_slider = QtWidgets.QSlider(self.centralwidget)
        self.tv_slider.setGeometry(QtCore.QRect(310, 140, 171, 22))
        self.tv_slider.setOrientation(QtCore.Qt.Horizontal)
        self.tv_slider.setObjectName("tv_slider")
        self.ie_label = QtWidgets.QLabel(self.centralwidget)
        self.ie_label.setGeometry(QtCore.QRect(50, 200, 121, 16))
        self.ie_label.setObjectName("ie_label")
        self.ie_slider = QtWidgets.QSlider(self.centralwidget)
        self.ie_slider.setGeometry(QtCore.QRect(310, 200, 171, 22))
        self.ie_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ie_slider.setObjectName("ie_slider")
        self.fio2_label = QtWidgets.QLabel(self.centralwidget)
        self.fio2_label.setGeometry(QtCore.QRect(50, 260, 121, 16))
        self.fio2_label.setObjectName("fio2_label")
        self.fio2_slider = QtWidgets.QSlider(self.centralwidget)
        self.fio2_slider.setGeometry(QtCore.QRect(310, 260, 171, 22))
        self.fio2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fio2_slider.setObjectName("fio2_slider")
        self.bpm_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.bpm_lcd.setGeometry(QtCore.QRect(200, 80, 64, 23))
        self.bpm_lcd.setObjectName("bpm_lcd")
        self.tv_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.tv_lcd.setGeometry(QtCore.QRect(200, 140, 64, 23))
        self.tv_lcd.setObjectName("tv_lcd")
        self.ie_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.ie_lcd.setGeometry(QtCore.QRect(200, 200, 64, 23))
        self.ie_lcd.setObjectName("ie_lcd")
        self.fio2_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.fio2_lcd.setGeometry(QtCore.QRect(200, 260, 64, 23))
        self.fio2_lcd.setObjectName("fio2_lcd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuAqualung = QtWidgets.QMenu(self.menubar)
        self.menuAqualung.setObjectName("menuAqualung")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAqualung.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ac_button.setText(_translate("MainWindow", "AC OFF"))
        self.bpm_label.setText(_translate("MainWindow", "BPM"))
        self.simv_button.setText(_translate("MainWindow", "SIMV OFF"))
        self.tv_label.setText(_translate("MainWindow", "Tidal Volume"))
        self.ie_label.setText(_translate("MainWindow", "I/E ratio"))
        self.fio2_label.setText(_translate("MainWindow", "FIO2"))
        self.menuAqualung.setTitle(_translate("MainWindow", "Oregon Volunteer Ventilator Project"))
