import random

min_numero = 1
max_numero = 100

numero_alvo = random.randint(min_numero, max_numero)

tentativas = 0

while True:
    palpite_usuario = input("Digite um número entre {} e {}: ".format(min_numero, max_numero))

    try:
        palpite_usuario = int(palpite_usuario)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        continue

    tentativas += 1

    if palpite_usuario == numero_alvo:
        print("Parabéns! Você acertou o número {} em {} tentativas.".format(numero_alvo, tentativas))
        break
    elif palpite_usuario < numero_alvo:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")