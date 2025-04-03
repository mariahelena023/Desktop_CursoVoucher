import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from parImpar import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_verificar.clicked.connect(self.verificar_numero)

    def verificar_numero(self):
        num = int(self.ui.lineEdit_numero.text())

        if num % 2 == 0:
            self.ui.label_resultado.setText("é par!")
        else:
            self.ui.label_resultado.setText("é ímpar!")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())