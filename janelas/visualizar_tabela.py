import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class TabelaArquivoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabela do Arquivo')
        self.resize(500, 400)

        layout = QVBoxLayout()
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)
        self.setLayout(layout)

        self.carregar_arquivo(r'd:\Downloads\Sincronizados\janelas\teste01.txt')

    def carregar_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                linhas = [linha.strip() for linha in f if linha.strip()]
                if not linhas:
                    return

                # Detecta o separador automaticamente para cada linha
                dados = []
                for linha in linhas:
                    if ',' in linha:
                        dados.append(linha.split(','))
                    elif ';' in linha:
                        dados.append(linha.split(';'))
                    elif '\t' in linha:
                        dados.append(linha.split('\t'))
                    else:
                        dados.append([linha])  # Linha única

                # Define o número de linhas e colunas
                self.tabela.setRowCount(len(dados))
                self.tabela.setColumnCount(max(len(l) for l in dados))

                # Preenche a tabela
                for i, linha in enumerate(dados):
                    for j, valor in enumerate(linha):
                        self.tabela.setItem(i, j, QTableWidgetItem(valor))
        except FileNotFoundError:
            self.tabela.setRowCount(1)
            self.tabela.setColumnCount(1)
            self.tabela.setItem(0, 0, QTableWidgetItem("Arquivo não encontrado"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabelaArquivoWindow()
    window.show()
    sys.exit(app.exec())