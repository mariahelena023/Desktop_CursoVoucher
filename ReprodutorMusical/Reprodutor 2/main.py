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
        self.isPaused_casual = False
        self.isPaused_gnarly = False
        self.isPaused_drama = False

        self.ui.horizontalSlider_volume.valueChanged.connect(self.controlar_volume)

        # Casual
        self.ui.pushButton_Play_casual.clicked.connect(self.play_casual)
        self.ui.pushButton_Parar_casual.clicked.connect(self.parar_casual)
        self.ui.pushButton_Pausar_casual.clicked.connect(self.pausar_casual)
        
        # Arabella
        self.ui.pushButton_Play_arabella.clicked.connect(self.play_arabella)
        self.ui.pushButton_Parar_arabella.clicked.connect(self.parar_arabella)
        self.ui.pushButton_Pausar_arabella.clicked.connect(self.pausar_arabella)
        
        # Gnarly
        self.ui.pushButton_Play_gnarly.clicked.connect(self.play_gnarly)
        self.ui.pushButton_Parar_gnarly.clicked.connect(self.parar_gnarly)
        self.ui.pushButton_Pausar_gnarly.clicked.connect(self.pausar_gnarly)

        # Cachimbo da Paz
        self.ui.pushButton_Play_cachimboDaPaz.clicked.connect(self.play_capushButton_Play_cachimboDaPaz)
        self.ui.pushButton_Parar_capushButton_Play_cachimboDaPaz.clicked.connect(self.parar_capushButton_Play_cachimboDaPaz)
        self.ui.pushButton_Pausar_capushButton_Play_cachimboDaPaz.clicked.connect(self.pausar_capushButton_Play_cachimboDaPaz)
        
        # That's What I Like
        self.ui.pushButton_Play_thatsWhatILike.clicked.connect(self.play_thapushButton_Play_thatsWhatILike)
        self.ui.pushButton_Parar_thapushButton_Play_thatsWhatILike.clicked.connect(self.parar_thapushButton_Play_thatsWhatILike)
        self.ui.pushButton_Pausar_thapushButton_Play_thatsWhatILike.clicked.connect(self.pausar_thapushButton_Play_thatsWhatILike)

    def controlar_volume(self):
        volume = self.ui.horizontalSlider_volume.value()
        self.player.setVolume(volume)
        print(f"Volume ajustado para: {volume}")

    # Casual
    def play_casual(self):
        caminho_musica = os.path.abspath("musicas/Casual.mp3")
        print("Local da música: ", caminho_musica)
        
        if self.isPaused_casual:
            self.player.play()
            self.isPaused_casual = False

        else:
            url = QUrl.fromLocalFile(caminho_musica)
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Trocando música...")
            else:
                print("Erro: caminho de arquivo inválido!")
    
    def parar_casual(self):
        self.player.stop()
        self.isPaused_casual = False
        print("A música parou!")
    
    def pausar_casual(self):
        self.player.pause()
        self.isPaused_casual = True
        print("A música pausou!")
    
    # arabella
    def play_arabella(self):
        caminho_musica = os.path.abspath("musicas/Arabella.mp3")
        print("Local da música: ", caminho_musica)
        
        if self.isPaused_arabella:
            self.player.play()
            self.isPaused_arabella = False

        else:
            url = QUrl.fromLocalFile(caminho_musica)
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Trocando música...")
            else:
                print("Erro: caminho de arquivo inválido!")
    
    def parar_arabella(self):
        self.player.stop()
        self.isPaused_arabella = False
        print("A música parou!")
    
    def pausar_arabella(self):
        self.player.pause()
        self.isPaused_arabella = True
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