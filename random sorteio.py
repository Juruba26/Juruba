import random
def sorteio_premios():
 premios = ["Carro", "Viagem", "Notebook", "Smartphone"]
 participante = input("Digite seu nome: ")
 premio = random.choice(premios)
 print(f"Parabéns, {participante}! Você ganhou um(a) {premio}.")
sorteio_premios()
