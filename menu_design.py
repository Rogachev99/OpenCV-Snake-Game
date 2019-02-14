# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 234)
        MainWindow.setMinimumSize(QtCore.QSize(244, 234))
        MainWindow.setMaximumSize(QtCore.QSize(244, 234))
        MainWindow.setBaseSize(QtCore.QSize(244, 234))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 30, 141, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btStartGame = QtWidgets.QPushButton(self.widget)
        self.btStartGame.setObjectName("btStartGame")
        self.verticalLayout.addWidget(self.btStartGame)
        self.btSettings = QtWidgets.QPushButton(self.widget)
        self.btSettings.setObjectName("btSettings")
        self.verticalLayout.addWidget(self.btSettings)
        self.btAbout = QtWidgets.QPushButton(self.widget)
        self.btAbout.setObjectName("btAbout")
        self.verticalLayout.addWidget(self.btAbout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btStartGame.setText(_translate("MainWindow", "Start"))
        self.btSettings.setText(_translate("MainWindow", "Settings"))
        self.btAbout.setText(_translate("MainWindow", "About"))
