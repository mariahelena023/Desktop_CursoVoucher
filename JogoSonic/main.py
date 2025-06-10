import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from jogoSonic import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_selectSonic.clicked.connect(lambda: self.alterar_imagem("Sonic"))
        self.ui.pushButton_selectTails.clicked.connect(lambda: self.alterar_imagem("Tails"))
        self.ui.pushButton_selectAmy.clicked.connect(lambda: self.alterar_imagem("Amy"))
        self.ui.pushButton_selectKnuckles.clicked.connect(lambda: self.alterar_imagem("Knuckles"))
        self.ui.pushButton_selectShadow.clicked.connect(lambda: self.alterar_imagem("Shadow"))

    def alterar_imagem(self, nome_personagem):
        caminho_img = {
            "Sonic": "img/sonic.png",
            "Tails": "img/tails.png",
            "Amy": "img/amy.png",
            "Knuckles": "img/knuckles.png",
            "Shadow": "img/shadow.png"
        }

        if nome_personagem in caminho_img:
            pixmap = QPixmap(caminho_img[nome_personagem])
            self.ui.label_personagemSelecionado.setPixmap(pixmap)
            self.ui.label_personagemSelecionado.setScaledContents(True)
        else:
            print(f"imagem para {nome_personagem} não encontrada!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
