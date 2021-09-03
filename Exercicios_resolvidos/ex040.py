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
