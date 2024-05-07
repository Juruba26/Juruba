# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:05:35 2024

@author: 202102307198
"""

def encontrar_nome_por_numero():
    # Solicita ao usuário o número para pesquisa
    numero_procurado = input("Digite o número para encontrar o nome correspondente: ")
   
    try:
        # Abre o arquivo para leitura
        with open("dados.txt", "r") as arquivo:
            for linha in arquivo:
                # Divide cada linha pelo delimitador vírgula
                numero, nome = linha.strip().split(',')
                # Verifica se o número na linha é o número procurado
                if numero.strip() == numero_procurado:
                    print(f"Nome encontrado: {nome.strip()}")
                    break
            else:
                # Este else pertence ao for, não ao if: executa se o loop não foi interrompido por break
                print("Número não encontrado no arquivo.")
    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)

# Chama a função para testar
encontrar_nome_por_numero()
