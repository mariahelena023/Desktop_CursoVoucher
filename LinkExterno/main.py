import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
from front import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao_whatsapp.clicked.connect(self.abrir_whatsapp)
        self.ui.botao_instagram.clicked.connect(self.abrir_instagram)
        self.ui.botao_github.clicked.connect(self.abrir_github)

    def abrir_whatsapp(self):
        whatsapp_link = "https://wa.me/67991691198"
        webbrowser.open(whatsapp_link)
    def abrir_instagram(self):
        instagram_link = "https://www.instagram.com/mariah__toledo"
        webbrowser.open(instagram_link)
    def abrir_github(self):
        github_link = "https://github.com/mariahelena023"
        webbrowser.open(github_link)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())