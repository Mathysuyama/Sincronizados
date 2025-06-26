import sys
from carregar_arquivo import carregar_arquivo
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
        carregar_arquivo(self.tabela, 'teste01.txt')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabelaArquivoWindow()
    window.show()
    sys.exit(app.exec())