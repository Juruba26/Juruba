def converter_para_fahrenheit():
    # Solicita ao usu�rio a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura para Fahrenheit usando a f�rmula de convers�o
    fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado
    print("A temperatura em Fahrenheit �:", fahrenheit, "�F")

# Chamada da fun��o
converter_para_fahrenheit()


