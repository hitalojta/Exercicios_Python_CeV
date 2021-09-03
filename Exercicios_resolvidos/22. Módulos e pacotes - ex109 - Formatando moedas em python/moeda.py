def moeda(num=0, moeda='R$'):
    return f'{moeda}:{num:.2f}'.replace('.', ',')


def metade(num, cond=False):
    val = num / 2
    return moeda(val) if cond else val


def dobro(num, cond=False):
    val = num * 2
    return moeda(val) if cond else val


def aumentar(num, q, cond=False):
    val = num * (1 + q / 100)
    return moeda(val) if cond else val


def diminuir(num, q, cond=False):
    val = num * (1 - q / 100)
    return moeda(val) if cond else val
