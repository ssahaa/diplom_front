# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(834, 736)
        AdminWindow.setStyleSheet("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 160, 81, 255), stop:1 rgba(255, 120, 161, 255))qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(136, 160, 152, 255), stop:1 rgba(248, 255, 198, 255))")
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelFIO = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.labelFIO.setFont(font)
        self.labelFIO.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size: 13pt;")
        self.labelFIO.setObjectName("labelFIO")
        self.horizontalLayout.addWidget(self.labelFIO)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.labelDATE = QtWidgets.QLabel(self.centralwidget)
        self.labelDATE.setMinimumSize(QtCore.QSize(0, 30))
        self.labelDATE.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.labelDATE.setFont(font)
        self.labelDATE.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 13pt;")
        self.labelDATE.setObjectName("labelDATE")
        self.labelDATE.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size: 13pt;")
        self.horizontalLayout.addWidget(self.labelDATE)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_Users = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Users.sizePolicy().hasHeightForWidth())
        self.pushButton_Users.setSizePolicy(sizePolicy)
        self.pushButton_Users.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_Users.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_Users.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_Users.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 13pt;")
        self.pushButton_Users.setObjectName("pushButton_Users")
        self.verticalLayout.addWidget(self.pushButton_Users)
        self.pushButton_GOST = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_GOST.sizePolicy().hasHeightForWidth())
        self.pushButton_GOST.setSizePolicy(sizePolicy)
        self.pushButton_GOST.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_GOST.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_GOST.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_GOST.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 13pt;")
        self.pushButton_GOST.setObjectName("pushButton_GOST")
        self.verticalLayout.addWidget(self.pushButton_GOST)
        self.pushButton_TP = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_TP.sizePolicy().hasHeightForWidth())
        self.pushButton_TP.setSizePolicy(sizePolicy)
        self.pushButton_TP.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_TP.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_TP.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_TP.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 13pt;")
        self.pushButton_TP.setObjectName("pushButton_TP")
        self.verticalLayout.addWidget(self.pushButton_TP)
        self.pushButton_Agreement = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Agreement.sizePolicy().hasHeightForWidth())
        self.pushButton_Agreement.setSizePolicy(sizePolicy)
        self.pushButton_Agreement.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_Agreement.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_Agreement.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_Agreement.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 13pt;")
        self.pushButton_Agreement.setObjectName("pushButton_Agreement")
        self.verticalLayout.addWidget(self.pushButton_Agreement)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_Exit.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 13pt;")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.verticalLayout.addWidget(self.pushButton_Exit)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 21))
        self.menubar.setObjectName("menubar")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.labelFIO.setText(_translate("AdminWindow", "ФИО"))
        self.labelDATE.setText(_translate("AdminWindow", "Дата"))
        self.pushButton_Users.setText(_translate("AdminWindow", "Пользователи"))
        self.pushButton_GOST.setText(_translate("AdminWindow", "ГОСТ"))
        self.pushButton_TP.setText(_translate("AdminWindow", "ТП"))
        self.pushButton_Agreement.setText(_translate("AdminWindow", "Согласование"))
        self.pushButton_Exit.setText(_translate("AdminWindow", "Выход"))


