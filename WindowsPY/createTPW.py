# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateTP.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateTP(object):
    def setupUi(self, CreateTP):
        CreateTP.setObjectName("CreateTP")
        CreateTP.resize(809, 635)
        self.centralwidget = QtWidgets.QWidget(CreateTP)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        CreateTP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateTP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        CreateTP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateTP)
        self.statusbar.setObjectName("statusbar")
        CreateTP.setStatusBar(self.statusbar)

        self.retranslateUi(CreateTP)
        QtCore.QMetaObject.connectSlotsByName(CreateTP)

    def retranslateUi(self, CreateTP):
        _translate = QtCore.QCoreApplication.translate
        CreateTP.setWindowTitle(_translate("CreateTP", "MainWindow"))
        self.label.setText(_translate("CreateTP", "Крутота"))
        self.pushButton.setText(_translate("CreateTP", "PushButton"))
