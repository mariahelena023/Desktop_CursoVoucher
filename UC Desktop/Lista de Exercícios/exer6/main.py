import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer6 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_verificar.clicked.connect(self.verificar)

    def verificar(self):
        n = int(self.ui.lineEdit_num.text())

        if n < 2:
            self.ui.label_resultado.setText(f"{n} não é primo")
        else:
            primo = True

            for i in range(2, (n // 2) + 1):
                if n % i == 0:
                    primo = False
                    break

            if primo:
                self.ui.label_resultado.setText(f"{n} é primo")
            else:
                self.ui.label_resultado.setText(f"{n} não é primo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
