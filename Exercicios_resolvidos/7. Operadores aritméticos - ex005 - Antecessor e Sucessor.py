"""
Faça um programa que leia um número inteiro e mostre na tela o seu
sucessor e seu antecessor.
"""

# Desafio 5

numero = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {} e o sucessor é {}.'.format(numero, numero - 1, numero + 1))
