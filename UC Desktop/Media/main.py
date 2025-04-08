import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from media import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.calcular)

    def calcular(self):
        n1 = float(self.ui.lineEdit_nota1.text())
        n2 = float(self.ui.lineEdit_nota2.text())
        n3 = float(self.ui.lineEdit_nota3.text())
        n4 = float(self.ui.lineEdit_nota4.text())

        resultado = (n1 + n2 + n3 + n4) / 4   

        if resultado >= 6:
            self.ui.label_resultado.setText(str(f"sua média foi {resultado}, você foi aprovado!"))
        else:
            self.ui.label_resultado.setText(str(f"sua média foi {resultado}, você foi reprovado!"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())