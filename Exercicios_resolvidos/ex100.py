from random import sample
from time import sleep

numeros = list(sample(range(1, 10), 5))


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for p in numeros:
        print(f'{p} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar():
    spar = 0
    for p in numeros:
        if p % 2 == 0:
            spar += p
    print(f'Somando os valores pares de {numeros}, temos {spar}')


sorteia()
somapar()

# from random import randint
# from time import sleep
#
#
# def sorteia(lista):
#     print('Sorteando 5 valores da lista: ', end='')
#     for cont in range(0, 5):
#         n = randint(1, 10)
#         lista.append(n)
#         print(f'{n} ', end='')
#         sleep(0.3)
#     print('PRONTO!')
#
#
# def somapar(lista):
#     soma = 0
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando os valores pares de {lista}, temos {soma}.')
# numeros = list()
# sorteia(numeros)
# print(numeros)
# somapar(numeros)
