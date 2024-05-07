def criar_lista_compras():
    # Solicita ao usuário os itens da lista de compras
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Separa os itens e armazena em uma lista
    lista_compras = entrada.split(", ")

    # Imprime os itens da lista
    print("Lista de Compras:")
    for i, item in enumerate(lista_compras, start=1):
        print("Item {}: {}".format(i, item))

# Chamada da função
criar_lista_compras()
