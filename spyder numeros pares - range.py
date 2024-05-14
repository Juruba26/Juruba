def numeros_pares(numero):
    """Retorna uma lista com todos os números pares entre 1 e o número dado, inclusive."""
    return list(range(2, numero + 1, 2))

# Exemplo de uso:
numero = 55
pares = numeros_pares(numero)
print("Números pares até", numero, ":", pares)

