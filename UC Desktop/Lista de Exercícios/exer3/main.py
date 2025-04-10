import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer3 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        n = int(self.ui.lineEdit_num.text())

        resultado = f"Tabuada do {n}:\n"
        for i in range(0, 11):
            resultado += f"{n} x {i} = {n * i}\n"

        self.ui.label_resultado.setText(resultado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())