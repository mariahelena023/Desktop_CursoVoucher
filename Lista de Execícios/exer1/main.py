import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer1 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        num = int(self.ui.lineEdit_num.text())

        if num < 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            fatorial = 1
            resultado = ""

            for i in range(num, 0, -1):
                fatorial *= i
                resultado += str(i)
                if i > 1:
                    resultado += " * "

                    self.ui.label_resultado.setText(f"{num}! = {resultado} = {fatorial}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())