import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from hello import Ui_MainWindow

class MainHello(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.mostrar_mensagem)

    def mostrar_mensagem(self):
        self.ui.label.setText("Hello, Word!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainHello()
    window.show()
    sys.exit(app.exec_())
