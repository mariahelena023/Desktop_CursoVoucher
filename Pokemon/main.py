import sys
from PyQt5 import QtWidgets, QtGui
from pokemon import Ui_MainWindow  

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)  

        self.ui.pushButton_adivinhar.clicked.connect(self.verificar_resposta)

    def verificar_resposta(self):
        self.ui.label_img.setPixmap(QtGui.QPixmap("img/pikachu.png"))
        self.ui.label_img.setScaledContents(True)
        
        self.ui.radioButton_op1.setStyleSheet(f"color: red")
        self.ui.radioButton_op2.setStyleSheet(f"color: green")
        self.ui.radioButton_op3.setStyleSheet(f"color: red")
        self.ui.radioButton_op4.setStyleSheet(f"color: red")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())