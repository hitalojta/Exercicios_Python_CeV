"""
Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome
"""

nome = str(input('Digite o nome da pessoa: '))\
    .upper().replace('-', ' ').split()

print('A pessoa possui o sobrenome Silva? -> {}'
      .format('SILVA' in nome))
