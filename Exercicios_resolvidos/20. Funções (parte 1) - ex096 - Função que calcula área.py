"""
Faça um programa que tenha uma função chamada area(), que
receba as dimensoes de um terreno retangular (largura e
comprimento) e mostre a area do terreno
"""


def area(lar, com):
    a = lar * com
    print(f'A área de um terreno {lar}m X {com}m é de {a}m².')


print('Controle de terrenos')
print('-'*20)
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
