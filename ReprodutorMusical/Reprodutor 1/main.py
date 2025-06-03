import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow
from play import Ui_MainWindow  

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.isPaused_likeJennie = False
        self.isPaused_gnarly = False
        self.isPaused_drama = False

        self.ui.horizontalSlider_volume.valueChanged.connect(self.controlar_volume)

        # Like Jennie
        self.ui.pushButton_Play_likeJennie.clicked.connect(self.play_likeJennie)
        self.ui.pushButton_Parar_likeJennie.clicked.connect(self.parar_likeJennie)
        self.ui.pushButton_Pausar_likeJennie.clicked.connect(self.pausar_likeJennie)
        
        # Gnarly
        self.ui.pushButton_Play_gnarly.clicked.connect(self.play_gnarly)
        self.ui.pushButton_Parar_gnarly.clicked.connect(self.parar_gnarly)
        self.ui.pushButton_Pausar_gnarly.clicked.connect(self.pausar_gnarly)

        # Drama
        self.ui.pushButton_Play_drama.clicked.connect(self.play_drama)
        self.ui.pushButton_Parar_drama.clicked.connect(self.parar_drama)
        self.ui.pushButton_Pausar_drama.clicked.connect(self.pausar_drama)

    def controlar_volume(self):
        volume = self.ui.horizontalSlider_volume.value()
        self.player.setVolume(volume)
        print(f"Volume ajustado para: {volume}")

    # Like Jennie
    def play_likeJennie(self):
        caminho_musica = os.path.abspath("musicas/LikeJennie.mp3")
        print("Local da música: ", caminho_musica)
        
        if self.isPaused_likeJennie:
            self.player.play()
            self.isPaused_likeJennie = False

        else:
            url = QUrl.fromLocalFile(caminho_musica)
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Trocando música...")
            else:
                print("Erro: caminho de arquivo inválido!")
    
    def parar_likeJennie(self):
        self.player.stop()
        self.isPaused_likeJennie = False
        print("A música parou!")
    
    def pausar_likeJennie(self):
        self.player.pause()
        self.isPaused_likeJennie = True
        print("A música pausou!")

    # Gnarly
    def play_gnarly(self):
        caminho_musica = os.path.abspath("musicas/Gnarly.mp3")
        print("Local da música: ", caminho_musica)
        
        if self.isPaused_gnarly:
            self.player.play()
            self.isPaused_gnarly = False

        else:
            url = QUrl.fromLocalFile(caminho_musica)
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Trocando música...")
            else:
                print("Erro: caminho de arquivo inválido!")
    
    def parar_gnarly(self):
        self.player.stop()
        self.isPaused_gnarly= False
        print("A música parou!")
    
    def pausar_gnarly(self):
        self.player.pause()
        self.isPaused_gnarly = True
        print("A música pausou!")

    # Drama
    def play_drama(self):
        caminho_musica = os.path.abspath("musicas/Drama.mp3")
        print("Local da música: ", caminho_musica)
        
        if self.isPaused_drama:
            self.player.play()
            self.isPaused_drama = False

        else:
            url = QUrl.fromLocalFile(caminho_musica)
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Trocando música...")
            else:
                print("Erro: caminho de arquivo inválido!")
    
    def parar_drama(self):
        self.player.stop()
        self.isPaused_drama = False
        print("A música parou!")

    def pausar_drama(self):
        self.player.pause()
        self.isPaused_drama = True
        print("A música pausou!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())