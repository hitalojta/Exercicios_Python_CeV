"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele
"""

nome = input('Digite algo: ')
print('Tipo primitivo: ', type(nome))
print('Só tem espaços? ', nome.isspace())
print('É um número? ', nome.isnumeric())
print('É alfabético? ', nome.isalpha())
print('É alfanumérico? ', nome.isalnum())
print('Está em maiúsculas? ', nome.isupper())
print('Está em minúsculas? ', nome.islower())
print('Está capitalizada? ', nome.istitle())
