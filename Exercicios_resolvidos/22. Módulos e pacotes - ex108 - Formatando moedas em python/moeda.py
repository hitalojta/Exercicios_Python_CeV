def metade(num=0):
    return num / 2


def dobro(num=0):
    return num * 2


def aumentar(num=0, q=0):
    return num * (1 + q / 100)


def diminuir(num=0, q=0):
    return num * (1 - q / 100)


def moeda(num=0, moeda='R$'):
    return f'{moeda}:{num:.2f}'.replace('.', ',')
