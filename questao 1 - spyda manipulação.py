def gravar_nome_em_arquivo():
    # Solicita ao usuário que informe seu nome
    nome = input("Digite seu nome: ")

    # Nome do arquivo onde será gravado o nome
    nome_arquivo = "nomes.txt"

    # Abre o arquivo em modo de escrita ('w')
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve o nome no arquivo
        arquivo.write(nome)

    print("Seu nome foi gravado com sucesso no arquivo", nome_arquivo)

# Chamada da função
gravar_nome_em_arquivo()
