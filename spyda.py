# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:17:49 2024

@author: 202102307198
"""

# Definindo as variáveis
numeros = [23, 43, 56, 63]
frase = "Gabigol eu te amo"
palavra = "Python"

# Imprimindo a média aritmética dos números
media = sum(numeros) / len(numeros)
print("Média aritmética dos números:", media)

# Imprimindo o quadrado do segundo número (índice 1)
quadrado = numeros[1] ** 2
print("Quadrado do segundo número:", quadrado)

# Imprimindo o dobro do terceiro número (índice 2)
dobro = numeros[2] * 2
print("Dobro do terceiro número:", dobro)

# Imprimindo a quantidade de letras da palavra
qtd_letras = len(palavra)
print("Quantidade de letras da palavra:", qtd_letras)

# Imprimindo a quantidade de espaços em branco na frase
qtd_espacos = frase.count(" ")
print("Quantidade de espaços em branco na frase:", qtd_espacos)

# Verificando se o primeiro número é maior que o segundo
primeiro_maior = numeros[0] > numeros[1]
print("O primeiro número é maior que o segundo:", primeiro_maior)

# Encontrando o maior número na lista
maior_numero = max(numeros)
print("O maior número é:", maior_numero)
