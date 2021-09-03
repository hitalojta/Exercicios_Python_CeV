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


def resumo(num=0, aum=0, dim=0):
    print('-' * 35)
    print("RESUMO DO VALOR".center(35))
    print('-' * 35)
    print(f'{"Preço analisado:":_<20}{moeda(num):_>15}')
    print(f'{"Dobro do preço:":_<20}{dobro(num, True):_>15}')
    print(f'{"Metade do preço:":_<20}{metade(num, True):_>15}')
    print(f'{f"{aum}% de aumento:":_<20}{aumentar(num, aum, True):_>15}')
    print(f'{f"{dim}% de redução:":_<20}{diminuir(num, dim, True):_>15}')
    print('-' * 35)
# Guanabara usou tabulação "\t" para alinhar, antes das funções
