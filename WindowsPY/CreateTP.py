# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateTP.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateTp(object):
    def setupUi(self, CreateTp):
        CreateTp.setObjectName("CreateTp")
        CreateTp.resize(1184, 701)
        CreateTp.setStyleSheet("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 160, 81, 255), stop:1 rgba(255, 120, 161, 255))qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(136, 160, 152, 255), stop:1 rgba(248, 255, 198, 255))")
        self.centralwidget = QtWidgets.QWidget(CreateTp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSelectFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSelectFile.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonSelectFile.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonSelectFile.setObjectName("pushButtonSelectFile")
        self.horizontalLayout.addWidget(self.pushButtonSelectFile)
        self.pushButtonDownloadTp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDownloadTp.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonDownloadTp.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonDownloadTp.setObjectName("pushButtonDownloadTp")
        self.horizontalLayout.addWidget(self.pushButtonDownloadTp)
        self.pushButtonAgreement = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAgreement.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonAgreement.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonAgreement.setObjectName("pushButtonAgreement")
        self.horizontalLayout.addWidget(self.pushButtonAgreement)
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButtonBack.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.horizontalLayout.addWidget(self.pushButtonBack)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 70))
        self.label_3.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        self.label_4.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditPathDownload = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPathDownload.setMinimumSize(QtCore.QSize(0, 70))
        self.lineEditPathDownload.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.lineEditPathDownload.setObjectName("lineEditPathDownload")
        self.gridLayout_2.addWidget(self.lineEditPathDownload, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditComment = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditComment.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.lineEditComment.setObjectName("lineEditComment")
        self.gridLayout.addWidget(self.lineEditComment, 2, 2, 1, 1)
        self.labelComment = QtWidgets.QLabel(self.centralwidget)
        self.labelComment.setMinimumSize(QtCore.QSize(100, 25))
        self.labelComment.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.labelComment.setObjectName("labelComment")
        self.gridLayout.addWidget(self.labelComment, 2, 0, 1, 1)
        self.label_Name = QtWidgets.QLabel(self.centralwidget)
        self.label_Name.setMinimumSize(QtCore.QSize(100, 25))
        self.label_Name.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.label_Name.setObjectName("label_Name")
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 1, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 300))
        self.scrollArea.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 927, 298))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        CreateTp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateTp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 21))
        self.menubar.setObjectName("menubar")
        CreateTp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateTp)
        self.statusbar.setObjectName("statusbar")
        CreateTp.setStatusBar(self.statusbar)

        self.retranslateUi(CreateTp)
        QtCore.QMetaObject.connectSlotsByName(CreateTp)

    def retranslateUi(self, CreateTp):
        _translate = QtCore.QCoreApplication.translate
        CreateTp.setWindowTitle(_translate("CreateTp", "MainWindow"))
        self.label_2.setText(_translate("CreateTp", "<html><head/><body><p><span style=\" font-size:16pt;\">Путь до файла</span></p></body></html>"))
        self.pushButtonSelectFile.setText(_translate("CreateTp", "Выбрать файл"))
        self.pushButtonDownloadTp.setText(_translate("CreateTp", "Загрузить шаблон ТП"))
        self.pushButtonAgreement.setText(_translate("CreateTp", "Отправить на согласование"))
        self.pushButtonBack.setText(_translate("CreateTp", "Назад"))
        self.label_4.setText(_translate("CreateTp", "Путь для выгрузки"))
        self.label.setText(_translate("CreateTp", "Выберите ГОСТ для ТП"))
        self.labelComment.setText(_translate("CreateTp", "<html><head/><body><p><span style=\" font-size:16pt;\">Комментарий</span></p></body></html>"))
        self.label_Name.setText(_translate("CreateTp", "<html><head/><body><p><span style=\" font-size:16pt;\">Наименование</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateTp = QtWidgets.QMainWindow()
    ui = Ui_CreateTp()
    ui.setupUi(CreateTp)
    CreateTp.show()
    sys.exit(app.exec_())
