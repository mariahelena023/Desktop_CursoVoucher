import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from formJogo import Ui_MainWindow  

class FormularioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_idade.setValidator(QIntValidator(0, 150))
        
        self.ui.pushButton_salvar.clicked.connect(self.enviar_dados)
        self.ui.pushButton_apagar.clicked.connect(self.limpar_campos)

    def enviar_dados(self):
        nomeCompleto = self.ui.lineEdit_nomeCompleto.text()
        nomeUsuario = self.ui.lineEdit_nomeUsuario.text()
        email = self.ui.lineEdit_email.text()
        idade = self.ui.lineEdit_idade.text()
        senha = self.ui.lineEdit_senha.text()
        personagem = "Bmo" if self.ui.radioButton_personagem1.isChecked() else "Finn" if self.ui.radioButton_personagem2.isChecked() else "Jake" if self.ui.radioButton_personagem3.isChecked() else "Princesa Jujuba" if self.ui.radioButton_personagem4.isChecked() else "Marceline" if self.ui.radioButton_personagem5.isChecked else "Não informado"

        if idade < 18:
            QMessageBox.warning(self, "Atenção", "Você precisa ser maior de idade para se cadastrar!")
            return
        
        if not (nomeCompleto and nomeUsuario and email and idade and senha and personagem):
            QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos")
            return

        conteudo = f"Nome Completo: {nomeCompleto}\nNome Usuario: {nomeUsuario}\nEmail: {email}\nIdade: {idade}\n Personagem escolhido: {personagem}"

        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{str(e)}")

    def limpar_campos(self):
        self.ui.lineEdit_nomeCompleto.clear()
        self.ui.lineEdit_nomeUsuario.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_idade.clear()
        self.ui.lineEdit_senha.clear()
        self.ui.radioButton_personagem1.setChecked(False)
        self.ui.radioButton_personagem2.setChecked(False)
        self.ui.radioButton_personagem3.setChecked(False)
        self.ui.radioButton_personagem4.setChecked(False)
        self.ui.radioButton_personagem5.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormularioApp()
    window.show()
    sys.exit(app.exec_()) 
