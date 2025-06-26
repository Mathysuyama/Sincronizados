import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

def carregar_arquivo(tabela, nome_arquivo):
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

            tabela.setRowCount(len(dados))
            tabela.setColumnCount(max(len(l) for l in dados))

            for i, linha in enumerate(dados):
                for j, valor in enumerate(linha):
                    tabela.setItem(i, j, QTableWidgetItem(valor))
    except FileNotFoundError:
        tabela.setRowCount(1)
        tabela.setColumnCount(1)
        tabela.setItem(0, 0, QTableWidgetItem("Arquivo não encontrado"))