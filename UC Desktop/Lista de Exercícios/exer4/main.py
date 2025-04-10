import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer4 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_contar.clicked.connect(self.contar)

    def contar(self):
        n = int(self.ui.lineEdit_num.text())

        contagem = "contagem regressiva:\n"
        for i in range(n, -1, -1):
            contagem += str(i) + "\n"

        self.ui.label_contagem.setText(contagem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())