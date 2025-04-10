import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer5 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        try:
            n = [int(self.ui.lineEdit_num1.text()), int(self.ui.lineEdit_num2.text()), int(self.ui.lineEdit_num3.text()), int(self.ui.lineEdit_num4.text()), int(self.ui.lineEdit_num5.text())]

            maior = max(n)
            menor = min(n)

            self.ui.label_resultado.setText(f"o maior número digitado foi: {maior}\n\n o menor número digitado foi: {menor}")

        except ValueError:
            self.ui.label_resultado.setText("apenas números inteiros")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
