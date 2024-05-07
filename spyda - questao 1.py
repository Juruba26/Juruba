def calcular_operacao():
    # Solicita ao usuário os números e a operação desejada
    num1 = float(input("Digite o primeiro número:1 "))
    num2 = float(input("Digite o segundo número:2 "))
    operacao = input("Digite a operação desejada (+, -, *, /): +")

    # Verifica a operação e calcula o resultado
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero!")
            return

    # Imprime o resultado
    print("O resultado da operação é:", resultado)

# Chamada da função
calcular_operacao()
