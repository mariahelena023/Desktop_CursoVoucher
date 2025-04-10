import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer2 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        n = int(self.ui.lineEdit_num.text())

        if n < 0:
            self.ui.label_resultado.setText("por favor, insira um número inteiro positivo.")
        else:
            soma = (n * (n + 1)) // 2
            self.ui.label_resultado.setText(f"a soma dos {n} primeiros números naturais é: {soma}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())