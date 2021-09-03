"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO
"""

n1 = float(input('Digite a primeira nota do aluno:\n'))
n2 = float(input('Digite a segunda nota do aluno:\n'))

media = (n1 + n2) / 2

if media < 5:
    print(f'Média do aluno: {media:.1f}\n\n'
          f'Situação do aluno: \033[4;31mREPROVADO\033[m')
elif media >= 7:
    print(f'Média do aluno: {media:.1f}\n\n'
          f'Situação do aluno: \033[4;32mAPROVADO\033[m')
else:
    print(f'Média do aluno: {media:.1f}\n\n'
          f'Situação do aluno: \033[4;33mRECUPERAÇÃO\033[m')
