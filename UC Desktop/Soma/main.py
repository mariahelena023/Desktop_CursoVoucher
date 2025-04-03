import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from soma import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_somar.clicked.connect(self.somar)

    def somar(self):
        n1 = float(self.ui.lineEdit_n1.text())
        n2 = float(self.ui.lineEdit_n2.text())

        resultado = n1 + n2

        self.ui.label_resultado_resultado.setText(str(resultado))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())