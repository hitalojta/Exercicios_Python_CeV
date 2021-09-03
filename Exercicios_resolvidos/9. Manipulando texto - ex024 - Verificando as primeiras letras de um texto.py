"""
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "SANTO".
"""

nome = str(input('Digite o nome da cidade: ')) \
    .upper().replace('-', ' ').split()  # split já dá um strip automatico

print('A cidade começa com o nome \'Santo\'? -> {}'
      .format(nome[0] == 'SANTO'))
