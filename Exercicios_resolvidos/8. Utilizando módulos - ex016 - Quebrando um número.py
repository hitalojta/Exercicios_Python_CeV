"""
Crie um programa que leia um número real qualquer pelo teclado e
mostre na tela a sua porção inteira
"""

# from math import trunc
import math

num = float(input('Digite um número: '))

print(f'A porção inteira do número digitado é {math.trunc(num)}')
# print(f'A porção inteira do número digitado é {trunc(num)}')
# print(f'A porção inteira do número digitado é {int(num)}')
