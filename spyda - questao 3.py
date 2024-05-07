def converter_para_fahrenheit():
    # Solicita ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit, "°F")

# Chamada da função
converter_para_fahrenheit()


