# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:01:28 2024

@author: 202102307198
"""

def copiar_conteudo_arquivo():
    # Solicita ao usuário o nome do arquivo de origem
    arquivo_origem = input("Digite o nome do arquivo de origem: ")
    # Solicita ao usuário o nome do arquivo de destino
    arquivo_destino = input("Digite o nome do arquivo de destino: ")

    try:
        # Abre o arquivo de origem para leitura
        with open(arquivo_origem, 'r') as origem:
            # Lê o conteúdo do arquivo de origem
            conteudo = origem.read()
       
        # Abre o arquivo de destino para escrita
        with open(arquivo_destino, 'w') as destino:
            # Escreve o conteúdo lido no arquivo de destino
            destino.write(conteudo)

        print(f"Conteúdo copiado com sucesso de {arquivo_origem} para {arquivo_destino}.")
    except FileNotFoundError:
        print("O arquivo de origem especificado não foi encontrado.")
    except IOError:
        print("Erro ao acessar o arquivo. Verifique se o arquivo não está em uso ou protegido contra escrita.")
    except Exception as e:
        print("Ocorreu um erro inesperado:", e)

# Chama a função para testar
copiar_conteudo_arquivo()