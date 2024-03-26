def soma_e_media(lista):
    """
    Calcula a soma e a média de uma lista de números.

    Args:
    lista (list): Uma lista de números.

    Returns:
    tuple: Uma tupla contendo a soma e a média dos números na lista.
    """
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    """
    Substitui as ocorrências de uma palavra por outra em uma lista de palavras.

    Args:
    lista (list): Uma lista de palavras.
    palavra_antiga (str): A palavra a ser substituída.
    palavra_nova (str): A nova palavra que substituirá a antiga.

    Returns:
    list: A lista com as substituições realizadas.
    """
    return [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]

def imprimir_triangulo(num_linhas):
    """
    Gera um triângulo de asteriscos para o número de linhas informado.

    Args:
    num_linhas (int): O número de linhas do triângulo.

    Returns:
    None
    """
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplos de uso:
if __name__ == "__main__":
    # Questão 1
    lista_numeros = [1, 2, 3, 4]
    soma, media = soma_e_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    # Questão 2
    lista_palavras = ["uva", "morango", "limão"]
    nova_lista = substituir_palavra(lista_palavras, "banana", "maçã")
    print("Lista com substituição:", nova_lista)

    # Questão 3
    num_linhas = 5
    imprimir_triangulo(num_linhas)


