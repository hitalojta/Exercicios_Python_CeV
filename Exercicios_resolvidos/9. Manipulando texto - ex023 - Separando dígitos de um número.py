"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados
"""

num = int(input('Digite um número de 0 a 9999: '))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'Unidade: {uni}\n'
      f'Dezena: {dez}\n'
      f'Centena: {cen}\n'
      f'Milhar: {mil}')
