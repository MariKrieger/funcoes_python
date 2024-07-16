numero = int(input('Digite um número qualquer: '))


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if is_prime(numero):
    print("{} é um número primo.".format(numero))
else:
    print("{} não é um número primo.".format(numero))