# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formJogo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(410, 0, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.label_nomeCompleto = QtWidgets.QLabel(self.centralwidget)
        self.label_nomeCompleto.setGeometry(QtCore.QRect(360, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nomeCompleto.setFont(font)
        self.label_nomeCompleto.setObjectName("label_nomeCompleto")
        self.lineEdit_nomeCompleto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nomeCompleto.setGeometry(QtCore.QRect(490, 120, 321, 22))
        self.lineEdit_nomeCompleto.setObjectName("lineEdit_nomeCompleto")
        self.label_nomeUsuario = QtWidgets.QLabel(self.centralwidget)
        self.label_nomeUsuario.setGeometry(QtCore.QRect(350, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nomeUsuario.setFont(font)
        self.label_nomeUsuario.setObjectName("label_nomeUsuario")
        self.lineEdit_nomeUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nomeUsuario.setGeometry(QtCore.QRect(490, 160, 321, 22))
        self.lineEdit_nomeUsuario.setObjectName("lineEdit_nomeUsuario")
        self.lineEdit_idade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_idade.setGeometry(QtCore.QRect(490, 240, 61, 22))
        self.lineEdit_idade.setObjectName("lineEdit_idade")
        self.label_idade = QtWidgets.QLabel(self.centralwidget)
        self.label_idade.setGeometry(QtCore.QRect(430, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_idade.setFont(font)
        self.label_idade.setObjectName("label_idade")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(490, 200, 321, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(430, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setGeometry(QtCore.QRect(640, 240, 171, 22))
        self.lineEdit_senha.setText("")
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setGeometry(QtCore.QRect(580, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_senha.setFont(font)
        self.label_senha.setObjectName("label_senha")
        self.label_selecionePersonagem = QtWidgets.QLabel(self.centralwidget)
        self.label_selecionePersonagem.setGeometry(QtCore.QRect(550, 340, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_selecionePersonagem.setFont(font)
        self.label_selecionePersonagem.setObjectName("label_selecionePersonagem")
        self.label_imgPersonagem1 = QtWidgets.QLabel(self.centralwidget)
        self.label_imgPersonagem1.setGeometry(QtCore.QRect(170, 430, 151, 151))
        self.label_imgPersonagem1.setText("")
        self.label_imgPersonagem1.setPixmap(QtGui.QPixmap("img/bmo.jpg"))
        self.label_imgPersonagem1.setScaledContents(True)
        self.label_imgPersonagem1.setObjectName("label_imgPersonagem1")
        self.label_imgPersonagem2 = QtWidgets.QLabel(self.centralwidget)
        self.label_imgPersonagem2.setGeometry(QtCore.QRect(350, 430, 151, 151))
        self.label_imgPersonagem2.setText("")
        self.label_imgPersonagem2.setPixmap(QtGui.QPixmap("img/finn.jpg"))
        self.label_imgPersonagem2.setScaledContents(True)
        self.label_imgPersonagem2.setObjectName("label_imgPersonagem2")
        self.label_imgPersonagem3 = QtWidgets.QLabel(self.centralwidget)
        self.label_imgPersonagem3.setGeometry(QtCore.QRect(530, 430, 151, 151))
        self.label_imgPersonagem3.setText("")
        self.label_imgPersonagem3.setPixmap(QtGui.QPixmap("img/jake.jpg"))
        self.label_imgPersonagem3.setScaledContents(True)
        self.label_imgPersonagem3.setObjectName("label_imgPersonagem3")
        self.label_imgPersonagem4 = QtWidgets.QLabel(self.centralwidget)
        self.label_imgPersonagem4.setGeometry(QtCore.QRect(710, 430, 151, 151))
        self.label_imgPersonagem4.setText("")
        self.label_imgPersonagem4.setPixmap(QtGui.QPixmap("img/jujuba.jpg"))
        self.label_imgPersonagem4.setScaledContents(True)
        self.label_imgPersonagem4.setObjectName("label_imgPersonagem4")
        self.label_imgPersonagem5 = QtWidgets.QLabel(self.centralwidget)
        self.label_imgPersonagem5.setGeometry(QtCore.QRect(890, 430, 151, 151))
        self.label_imgPersonagem5.setText("")
        self.label_imgPersonagem5.setPixmap(QtGui.QPixmap("img/marceline.jpg"))
        self.label_imgPersonagem5.setScaledContents(True)
        self.label_imgPersonagem5.setObjectName("label_imgPersonagem5")
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setGeometry(QtCore.QRect(630, 620, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_salvar.setFont(font)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.radioButton_personagem1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_personagem1.setGeometry(QtCore.QRect(220, 400, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_personagem1.setFont(font)
        self.radioButton_personagem1.setObjectName("radioButton_personagem1")
        self.radioButton_personagem2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_personagem2.setGeometry(QtCore.QRect(400, 400, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_personagem2.setFont(font)
        self.radioButton_personagem2.setObjectName("radioButton_personagem2")
        self.radioButton_personagem3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_personagem3.setGeometry(QtCore.QRect(570, 400, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_personagem3.setFont(font)
        self.radioButton_personagem3.setObjectName("radioButton_personagem3")
        self.radioButton_personagem4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_personagem4.setGeometry(QtCore.QRect(710, 400, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_personagem4.setFont(font)
        self.radioButton_personagem4.setObjectName("radioButton_personagem4")
        self.radioButton_personagem5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_personagem5.setGeometry(QtCore.QRect(910, 400, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_personagem5.setFont(font)
        self.radioButton_personagem5.setObjectName("radioButton_personagem5")
        self.pushButton_apagar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apagar.setGeometry(QtCore.QRect(530, 620, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_apagar.setFont(font)
        self.pushButton_apagar.setObjectName("pushButton_apagar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 26))
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
        self.label_titulo.setText(_translate("MainWindow", "Preencha seus Dados"))
        self.label_nomeCompleto.setText(_translate("MainWindow", "Nome Completo:"))
        self.label_nomeUsuario.setText(_translate("MainWindow", "Nome de Usuário:"))
        self.label_idade.setText(_translate("MainWindow", "Idade:"))
        self.label_email.setText(_translate("MainWindow", "E-mail:"))
        self.label_senha.setText(_translate("MainWindow", "Senha:"))
        self.label_selecionePersonagem.setText(_translate("MainWindow", "Escolha Seu Personagem:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
        self.radioButton_personagem1.setText(_translate("MainWindow", "Bmo"))
        self.radioButton_personagem2.setText(_translate("MainWindow", "Finn"))
        self.radioButton_personagem3.setText(_translate("MainWindow", "Jake"))
        self.radioButton_personagem4.setText(_translate("MainWindow", "Princesa Jujuba"))
        self.radioButton_personagem5.setText(_translate("MainWindow", "Marceline"))
        self.pushButton_apagar.setText(_translate("MainWindow", "Apagar"))
