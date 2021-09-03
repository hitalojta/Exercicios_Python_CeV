"""
Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parametro e mostre uma mensagem com tamanho
adaptavel
Ex:
escreva("Olá, mundo!")
Saída:
-----------
Olá, mundo!
-----------
"""


def escreva(texto):
    print('-' * (len(texto) + 4))
    print(f'  {texto}')
    print('-' * (len(texto) + 4))


escreva(str(input('Digite o texto: ')).strip())
