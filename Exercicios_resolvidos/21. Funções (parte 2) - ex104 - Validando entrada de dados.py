"""
Crie um programa que tenha a função leiaint(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo
a validação para aceitar apenas um valor numerico.
Ex:
n = leiaint("Digite um 'n'")
"""


def leiaint(perg):
    num = input(perg)
    while not num.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        num = input(perg)
    return int(num)


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
