import os as o

# Modo tradicional

# O nome do arquivo que você quer ler
nome_do_arquivo = 'teste.txt'

def ler_arquivo(ler = nome_do_arquivo):
    try:
        # 'with' garante que o arquivo será fechado no final.
        # 'r' é o modo de leitura (read).
        # 'encoding="utf-8"' é importante para ler caracteres especiais corretamente.
        with open(ler, 'r', encoding='utf-8') as arquivo:
            print(f"Lendo o arquivo '{ler}' linha por linha:\n")
            for linha in arquivo:
                # .strip() remove espaços em branco e quebras de linha do início e fim da linha
                print(linha.strip())

    except FileNotFoundError:
        print(f"Erro: O arquivo '{ler}' não foi encontrado.")
    except Exception as e:
         print(f"Ocorreu um erro: {e}")
         
ler_arquivo()
