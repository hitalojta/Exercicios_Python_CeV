"""
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada
"""

# Desafio 9

numero = int(input('Digite um número inteiro: '))
print('\n{}'.format('='*12))
print(f'A tabuada de {numero} é:\n{numero}x1 = {numero * 1}\n'
      f'{numero}x2 = {numero * 2}\n{numero}x3 = {numero * 3}\n'
      f'{numero}x4 = {numero * 4}\n{numero}x5 = {numero * 5}\n'
      f'{numero}x6 = {numero * 6}\n{numero}x7 = {numero * 7}\n'
      f'{numero}x8 = {numero * 8}\n{numero}x9 = {numero * 9}\n'
      f'{numero}x10 = {numero * 10}')
print('='*12)

