"""
Crie um algoritmo que leia um numero e mostre o seu dobro, triplo
e raiz quadrada
"""

# Desafio 6

numero = float(input('Digite um número: '))
print('O dobro de {} é {}.\nO triplo é {}.\nA raiz quadrada é {}.'.format(numero,
    numero * 2, numero * 3, numero ** (1/2))) # pow(numero, 1/2)
