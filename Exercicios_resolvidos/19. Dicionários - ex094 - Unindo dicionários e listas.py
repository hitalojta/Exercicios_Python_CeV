"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionario e todos os
dicionarios em uma lista. No final, mostre:
a) quantas pessoas cadastradas
b) a média de idade
c) uma lista com mulheres
d) uma lista com idade acima da media
"""

lista = list()
temp = dict()
sidade = 0
while True:
    temp['nome'] = str(input('Nome: ')).strip().title()
    temp['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]
    while temp['sexo'] not in 'MF':
        temp['sexo'] = str(input('\033[31mOpção inválida!\033[m\nSexo [M/F]:')).strip().upper()[0]
    temp['idade'] = int(input('Idade: '))
    sidade += temp['idade']
    lista.append(temp.copy())
    temp.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('\033[31mOpção inválida!\033[m\nQuer continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print('-=' * 30)
print(f'A) O grupo tem {len(lista)} pessoas.')
print(f'B) A média de idade é de {(sidade / len(lista)):.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(f'{lista[c]["nome"]}', end='; ')
print()
print('D) Lista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] > (sidade / len(lista)):
        print('\t', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
