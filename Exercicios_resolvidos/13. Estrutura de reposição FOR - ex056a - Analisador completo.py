"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- a média de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos
"""

#fiz esse após analisar resposta
somaidade = 0
idadevelho = 0
contmulher20 = 0
nomevelho = ''
for c in range(1, 5):
    print('{:=^20}'.format(f' PESSOA {c} '))
    nome = str(input('Digite o nome:')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [ M / F ]: ')).lower()
    somaidade += idade
    if sexo == 'm' and idade > idadevelho:
        nomevelho = nome
        idadevelho = idade
    if sexo == 'f' and idade < 20:
        contmulher20 += 1

mediaidade = somaidade / 4

print(f'A média das idades é: {mediaidade} anos.')

if nomevelho == '':
    print('Não há homens entre as pessoas dadas!')
else:
    print(f'O homem mais velho possui {idadevelho} anos e se chama {nomevelho}.')

print(f'Do grupo, {contmulher20} mulheres possuem menos de 20 anos.')