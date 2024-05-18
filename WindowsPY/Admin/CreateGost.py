# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateGost.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateGOST(object):
    def setupUi(self, CreateGOST):
        CreateGOST.setObjectName("CreateGOST")
        CreateGOST.resize(1047, 614)
        CreateGOST.setStyleSheet("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 160, 81, 255), stop:1 rgba(255, 120, 161, 255))qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(136, 160, 152, 255), stop:1 rgba(248, 255, 198, 255))")
        self.centralwidget = QtWidgets.QWidget(CreateGOST)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 60))
        self.label_4.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.pushButtonCreate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCreate.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButtonCreate.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.gridLayout_2.addWidget(self.pushButtonCreate, 5, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(286, 80))
        self.pushButtonBack.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.gridLayout.addWidget(self.pushButtonBack, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 70))
        self.label_3.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.pushButtonSelectFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSelectFile.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonSelectFile.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonSelectFile.setObjectName("pushButtonSelectFile")
        self.gridLayout.addWidget(self.pushButtonSelectFile, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        CreateGOST.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateGOST)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 21))
        self.menubar.setObjectName("menubar")
        CreateGOST.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateGOST)
        self.statusbar.setObjectName("statusbar")
        CreateGOST.setStatusBar(self.statusbar)

        self.retranslateUi(CreateGOST)
        QtCore.QMetaObject.connectSlotsByName(CreateGOST)

    def retranslateUi(self, CreateGOST):
        _translate = QtCore.QCoreApplication.translate
        CreateGOST.setWindowTitle(_translate("CreateGOST", "MainWindow"))
        self.label_4.setText(_translate("CreateGOST", "<html><head/><body><p><span style=\" font-size:16pt;\">Наименование</span></p></body></html>"))
        self.pushButtonCreate.setText(_translate("CreateGOST", "Создать"))
        self.pushButtonBack.setText(_translate("CreateGOST", "Назад"))
        self.pushButtonSelectFile.setText(_translate("CreateGOST", "Выбрать файл"))
        self.label_2.setText(_translate("CreateGOST", "<html><head/><body><p><span style=\" font-size:16pt;\">Путь до файла</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateGOST = QtWidgets.QMainWindow()
    ui = Ui_CreateGOST()
    ui.setupUi(CreateGOST)
    CreateGOST.show()
    sys.exit(app.exec_())