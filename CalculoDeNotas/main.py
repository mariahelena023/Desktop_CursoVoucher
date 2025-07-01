import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from calculoDeNotas import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dados_candidatos = {}

        self.ui.pushButton_cancelar.clicked.connect(self.limpar_campos)
        self.ui.pushButton_salvarNotas.clicked.connect(self.salvar_notas)


    def limpar_campos(self):
        self.ui.lineEdit_cpf.clear()
        self.ui.lineEdit_matematica.clear()
        self.ui.lineEdit_portugues.clear()
        self.ui.lineEdit_conhecimentosGerais.clear()
        self.ui.lineEdit_conhecimentosEspecifico.clear()

    def salvar_notas(self):
        cpf = int(self.ui.lineEdit_cpf.text())
        matematica_acertos = int(self.ui.lineEdit_matematica.text())
        portugues_acertos = int(self.ui.lineEdit_portugues.text())
        conhecimentosGerais_acertos = int(self.ui.lineEdit_conhecimentosGerais.text())
        conhecimentosEspecificos_acertos = int(self.ui.lineEdit_conhecimentosEspecifico.text())

        self.dados_candidatos[cpf] = {
            "Matemática": matematica_acertos,
            "Português": portugues_acertos,
            "Conhecimentos Gerais": conhecimentosGerais_acertos,
            "Conhecimentos Específicos": conhecimentosEspecificos_acertos
        }

        self.salvar_json()
        QMessageBox.information(self, 'Sucesso', 'Dados salvos com sucesso!')
        self.limpar_campos()

    def salvar_json(self):
        try:
            #verificar se o arquivo existe
            if os.path.exists('dados_candidatos.son'):

                #se existir: carregar dados
                with open('dados_candidatos.json', 'r') as f:
                    dados_existentes = json.load(f)

                #atualizar os dados existentes com os novos dados
                dados_existentes.update(self.dados_candidatos)

                #abrir o arquivo em modo de escrita para salvar os dados atualizados
                with open('dados_candidatos.json', 'w') as f:
                    json.dump(dados_existentes, f, indent=4)
            else:
                #se o arquivo não existir: salvar os dados
                with open('dados_candidatos.json', 'w') as f:
                    json.dump(self.dados_candidatos, f, indent=4)
        except Exception as e:
            QMessageBox.critical(self, 'Erro ao salvar!', f'Ocorreu um erro ao salvar os dados.')
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())