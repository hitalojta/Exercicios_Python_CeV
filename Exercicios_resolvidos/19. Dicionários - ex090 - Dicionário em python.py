"""
Faça um programa que leia nome e media de um aluno, guardando
tambem a situação em um dicionario. No final, mostre o conteudo
da estrutura na tela.
"""

aluno = dict()
aluno['Nome'] = str(input('Nome do aluno(a): ')).strip().title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] <= 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
