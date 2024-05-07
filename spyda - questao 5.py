def solicitar_nomes():
    nomes = []

    # Loop infinito para solicitar nomes
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        nomes.append(nome)  # Adiciona o nome à lista

    # Imprime todos os nomes digitados
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Chamada da função
solicitar_nomes()



