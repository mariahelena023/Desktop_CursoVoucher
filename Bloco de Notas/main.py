import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from blocoNotas import Ui_MainWindow

class Main(QMainWindow):
    def __init__(sdelf):
        super().__init__()
        self.ui = ui.MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())