# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'play.ui'
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
        self.pushButton_Play_likeJennie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Play_likeJennie.setGeometry(QtCore.QRect(130, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Play_likeJennie.setFont(font)
        self.pushButton_Play_likeJennie.setObjectName("pushButton_Play_likeJennie")
        self.pushButton_Parar_likeJennie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Parar_likeJennie.setGeometry(QtCore.QRect(130, 420, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Parar_likeJennie.setFont(font)
        self.pushButton_Parar_likeJennie.setObjectName("pushButton_Parar_likeJennie")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(220, 50, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.pushButton_Play_gnarly = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Play_gnarly.setGeometry(QtCore.QRect(340, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Play_gnarly.setFont(font)
        self.pushButton_Play_gnarly.setObjectName("pushButton_Play_gnarly")
        self.pushButton_Parar_gnarly = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Parar_gnarly.setGeometry(QtCore.QRect(340, 420, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Parar_gnarly.setFont(font)
        self.pushButton_Parar_gnarly.setObjectName("pushButton_Parar_gnarly")
        self.pushButton_Parar_drama = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Parar_drama.setGeometry(QtCore.QRect(550, 420, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Parar_drama.setFont(font)
        self.pushButton_Parar_drama.setObjectName("pushButton_Parar_drama")
        self.pushButton_Play_drama = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Play_drama.setGeometry(QtCore.QRect(550, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Play_drama.setFont(font)
        self.pushButton_Play_drama.setObjectName("pushButton_Play_drama")
        self.label_img_likeJennie = QtWidgets.QLabel(self.centralwidget)
        self.label_img_likeJennie.setGeometry(QtCore.QRect(130, 210, 121, 111))
        self.label_img_likeJennie.setText("")
        self.label_img_likeJennie.setPixmap(QtGui.QPixmap("imagens/likeJennie.png"))
        self.label_img_likeJennie.setScaledContents(True)
        self.label_img_likeJennie.setObjectName("label_img_likeJennie")
        self.label_img_gnarly = QtWidgets.QLabel(self.centralwidget)
        self.label_img_gnarly.setGeometry(QtCore.QRect(340, 210, 121, 111))
        self.label_img_gnarly.setText("")
        self.label_img_gnarly.setPixmap(QtGui.QPixmap("imagens/gnarly.png"))
        self.label_img_gnarly.setScaledContents(True)
        self.label_img_gnarly.setObjectName("label_img_gnarly")
        self.label_img_drama = QtWidgets.QLabel(self.centralwidget)
        self.label_img_drama.setGeometry(QtCore.QRect(550, 210, 121, 111))
        self.label_img_drama.setText("")
        self.label_img_drama.setPixmap(QtGui.QPixmap("imagens/drama.png"))
        self.label_img_drama.setScaledContents(True)
        self.label_img_drama.setObjectName("label_img_drama")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 180, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 180, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 180, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_Pausar_likeJennie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pausar_likeJennie.setGeometry(QtCore.QRect(130, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Pausar_likeJennie.setFont(font)
        self.pushButton_Pausar_likeJennie.setObjectName("pushButton_Pausar_likeJennie")
        self.pushButton_Pausar_gnarly = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pausar_gnarly.setGeometry(QtCore.QRect(340, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Pausar_gnarly.setFont(font)
        self.pushButton_Pausar_gnarly.setObjectName("pushButton_Pausar_gnarly")
        self.pushButton_Pausar_drama = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Pausar_drama.setGeometry(QtCore.QRect(550, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Pausar_drama.setFont(font)
        self.pushButton_Pausar_drama.setObjectName("pushButton_Pausar_drama")
        self.horizontalSlider_volume = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_volume.setGeometry(QtCore.QRect(320, 500, 160, 22))
        self.horizontalSlider_volume.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_volume.setObjectName("horizontalSlider_volume")
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
        self.pushButton_Play_likeJennie.setText(_translate("MainWindow", "Play"))
        self.pushButton_Parar_likeJennie.setText(_translate("MainWindow", "Parar"))
        self.label_titulo.setText(_translate("MainWindow", "Spotify (Toledo\'s Version)"))
        self.pushButton_Play_gnarly.setText(_translate("MainWindow", "Play"))
        self.pushButton_Parar_gnarly.setText(_translate("MainWindow", "Parar"))
        self.pushButton_Parar_drama.setText(_translate("MainWindow", "Parar"))
        self.pushButton_Play_drama.setText(_translate("MainWindow", "Play"))
        self.label.setText(_translate("MainWindow", "Like JENNIE"))
        self.label_2.setText(_translate("MainWindow", "Gnarly"))
        self.label_3.setText(_translate("MainWindow", "Drama"))
        self.pushButton_Pausar_likeJennie.setText(_translate("MainWindow", "Pausar"))
        self.pushButton_Pausar_gnarly.setText(_translate("MainWindow", "Pausar"))
        self.pushButton_Pausar_drama.setText(_translate("MainWindow", "Pausar"))
