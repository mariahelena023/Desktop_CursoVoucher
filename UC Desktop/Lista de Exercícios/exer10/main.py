import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer10 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_ordenar.clicked.connect(self.ordenar)

    def ordenar(self):
        try:
            n = [int(self.ui.lineEdit_num1.text()), int(self.ui.lineEdit_num2.text()), int(self.ui.lineEdit_num3.text()), int(self.ui.lineEdit_num4.text()), int(self.ui.lineEdit_num5.text()), int(self.ui.lineEdit_num6.text()), int(self.ui.lineEdit_num7.text()), int(self.ui.lineEdit_num8.text()), int(self.ui.lineEdit_num9.text()), int(self.ui.lineEdit_num10.text())]

            crescente = sorted(n)
            decrescente = sorted(n, reverse=True)

            self.ui.label_resultado.setText(f"lista crescente: {crescente}\n\n lista decrescente: {decrescente}")

        except ValueError:
            self.ui.label_resultado.setText("apenas números inteiros")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
