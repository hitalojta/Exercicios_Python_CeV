"""
Crie um programa onde o usuário possa digitar vários valores
numericos e cadastre-os em uma lista. Caso o numero ja exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores unicos digitados, em ordem crescente.
"""

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Insira outro valor...')
    else:
        lista.append(n)
        print('Valor adicionado!')
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'n':
        break
print('-='*20)
lista.sort()
print(f'Você digitou os valores {lista}')
