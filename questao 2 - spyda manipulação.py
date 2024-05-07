# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:01:07 2024

@author: 202102307198
"""

def imprimir_conteudo_arquivo():
    # Solicita ao usuário o nome do arquivo de texto
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    # Abre o arquivo em modo de leitura ('r')
    with open(nome_arquivo, 'r') as arquivo:
        # Lê e imprime o conteúdo do arquivo
        conteudo = arquivo.read()
        print("Conteúdo do arquivo", nome_arquivo + ":")
        print(conteudo)

# Chamada da função
imprimir_conteudo_arquivo()
