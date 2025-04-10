import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exer8 import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_inverter.clicked.connect(self.inverter)

    def inverter(self):
        n = [int(self.ui.lineEdit_num1.text()), int(self.ui.lineEdit_num2.text()), int(self.ui.lineEdit_num3.text()), int(self.ui.lineEdit_num4.text()), int(self.ui.lineEdit_num5.text()), int(self.ui.lineEdit_num6.text()), int(self.ui.lineEdit_num7.text()), int(self.ui.lineEdit_num8.text()), int(self.ui.lineEdit_num9.text()), int(self.ui.lineEdit_num10.text())]

        n_i = n.copy()
        n_i.reverse()

        
        self.ui.label_resultado.setText(f"lista normal: {n} \n\n lista invertida: {n_i}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
