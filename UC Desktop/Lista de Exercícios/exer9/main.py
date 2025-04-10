import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer9 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_verificar.clicked.connect(self.verificar)

    def verificar(self):
        p = self.ui.lineEdit_p.text()

        if p == p[::-1]:
            self.ui.label_resultado.setText(f"{p} é um palíndromo!")
        else:
            self.ui.label_resultado.setText(f"{p} não é um palíndromo!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
