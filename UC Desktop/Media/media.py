# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'media.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(320, 40, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.label_nota1 = QtWidgets.QLabel(self.centralwidget)
        self.label_nota1.setGeometry(QtCore.QRect(260, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nota1.setFont(font)
        self.label_nota1.setObjectName("label_nota1")
        self.lineEdit_nota1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nota1.setGeometry(QtCore.QRect(330, 110, 181, 22))
        self.lineEdit_nota1.setObjectName("lineEdit_nota1")
        self.label_nota2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nota2.setGeometry(QtCore.QRect(260, 150, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nota2.setFont(font)
        self.label_nota2.setObjectName("label_nota2")
        self.lineEdit_nota2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nota2.setGeometry(QtCore.QRect(330, 150, 181, 22))
        self.lineEdit_nota2.setObjectName("lineEdit_nota2")
        self.label_nota4 = QtWidgets.QLabel(self.centralwidget)
        self.label_nota4.setGeometry(QtCore.QRect(260, 230, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nota4.setFont(font)
        self.label_nota4.setObjectName("label_nota4")
        self.label_nota3 = QtWidgets.QLabel(self.centralwidget)
        self.label_nota3.setGeometry(QtCore.QRect(260, 190, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nota3.setFont(font)
        self.label_nota3.setObjectName("label_nota3")
        self.lineEdit_nota4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nota4.setGeometry(QtCore.QRect(330, 230, 181, 22))
        self.lineEdit_nota4.setObjectName("lineEdit_nota4")
        self.lineEdit_nota3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nota3.setGeometry(QtCore.QRect(330, 190, 181, 22))
        self.lineEdit_nota3.setObjectName("lineEdit_nota3")
        self.pushButton_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calcular.setGeometry(QtCore.QRect(360, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_calcular.setFont(font)
        self.pushButton_calcular.setObjectName("pushButton_calcular")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(250, 400, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titulo.setText(_translate("MainWindow", "Calculo de Média"))
        self.label_nota1.setText(_translate("MainWindow", "Nota 1:"))
        self.label_nota2.setText(_translate("MainWindow", "Nota 2:"))
        self.label_nota4.setText(_translate("MainWindow", "Nota 4:"))
        self.label_nota3.setText(_translate("MainWindow", "Nota 3:"))
        self.pushButton_calcular.setText(_translate("MainWindow", "Calcular"))
