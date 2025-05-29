import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from exibirNome import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_exibir.clicked.connect(self.exibir_nome)
        self.ui.pushButton_exibir.clicked.connect(self.exibir_idade)


    def exibir_nome(self):
        nome = self.ui.lineEdit_nome.text()
        self.ui.labelExibir_nome.setText(f"Nome: {nome}")
    def exibir_idade(self):
        idade = self.ui.lineEdit_idade.text()
        self.ui.labelExibir_idade.setText(f"Idade: {idade}")


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())