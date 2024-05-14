def bombom(dinheiro, preco):
    """Calcula o número de bombons e o troco dados o dinheiro e o preço de um bombom."""
    num_bombons = dinheiro // preco
    troco = dinheiro % preco
    return num_bombons, troco

def maisbombom(dinheiro, preco):
    """Calcula quanto Joãozinho terá que pedir para sua mãe para comprar um bombom a mais."""
    troco_atual = bombom(dinheiro, preco)[1]
    preco_bombom_extra = preco - troco_atual
    return preco_bombom_extra

# Exemplo de uso:
dinheiro_disponivel = 352
preco_bombom = 5
preco_bombom_extra = maisbombom(dinheiro_disponivel, preco_bombom)
print("Joãozinho terá que pedir", preco_bombom_extra, "à sua mãe para comprar um bombom a mais.")
