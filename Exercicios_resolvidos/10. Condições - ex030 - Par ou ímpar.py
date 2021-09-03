"""
Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR ou ÍMPAR.
"""

num = int(input('Digite um número inteiro:\n'))

par = num % 2

print('Número par.' if par == 0 else "Número ímpar.")
