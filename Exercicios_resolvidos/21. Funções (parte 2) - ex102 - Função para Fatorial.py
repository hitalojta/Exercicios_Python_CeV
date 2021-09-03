"""
Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o numero a calcular
e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de
calculo do fatorial.
"""

# def fatorial(num, show):
#     '''
#     -> Calcula o Fatorial de um número.
#     :param num: O número a ser calculado
#     :param show: Mostrar ou não a conta
#     :return: O valor do fatorial de um número 'n'
#     '''
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#         if c == 1 and show:
#             print(f'{c} = ', end='')
#         elif show:
#             print(f'{c} x ', end='')
#     print(f'{f}')
#
#
# show2 = False
# n = int(input('Digite um número: '))
# mostra = str(input('Quer mostrar o processo? [S/N]: ')).strip().lower()
# while mostra not in 'sn':
#     mostra = str(input('\033[31mOpção inválida!\033[m\nQuer mostrar o processo? [S/N]: ')).strip().lower()
# if mostra == 's':
#     show2 = True
# fatorial(n, show2)

# Guanabara


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: Mostrar ou não a conta
    :return: O valor do fatorial de um número 'n'
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


help(fatorial)
print(fatorial(5, show=True))
