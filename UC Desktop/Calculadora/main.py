import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from calculadora import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        num1 = float(self.ui.lineEdit_num1.text())
        num2 = float(self.ui.lineEdit_num2.text())

        soma = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        self.ui.label_resultado.setText(str(f"soma: {soma}\nsubtração: {sub}\nmultiplicação: {mult}\ndivisão: {div}"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())