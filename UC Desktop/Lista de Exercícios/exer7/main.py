import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer7 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_conferir.clicked.connect(self.conferir)

    def conferir(self):
        try:
            n = int(self.ui.lineEdit_num.text())

            if n <= 0:
                self.ui.label_resultado.setText("o número deve ser inteiro positivo")
                return

            fibonacci = []

            if n == 1:
                fibonacci = [0]
            elif n == 2:
                fibonacci = [0, 1]
            else:
                fibonacci = [0, 1]
                for i in range(2, n):
                    proximo = fibonacci[-1] + fibonacci[-2]
                    fibonacci.append(proximo)

            self.ui.label_resultado.setText(f"Sequência de Fibonacci ({n} termos): {fibonacci}")

        except ValueError:
            self.ui.label_resultado.setText("Insira um número válido")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
