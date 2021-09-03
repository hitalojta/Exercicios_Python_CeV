contmulher = conthomem = contidade = 0
while True:
    print('-'*25)
    print('{: ^25}'.format(' CADASTRE UMA PESSOA '))
    print('-' * 25)
    idade = int(input('Digite a idade: '))
    while idade < 0:
        idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().lower()[0]
    while sexo not in 'mf':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().lower()[0]
    if idade > 18:
        contidade += 1
    if sexo == 'm':
        conthomem += 1
    if sexo == 'f' and idade < 20:
        contmulher += 1
    print('-'*25)
    sair = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while sair not in 'sn':
        sair = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if sair == 'n':
        break
print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {contidade}\n'
      f'Ao todo temos {conthomem} homens cadastrados\n'
      f'E temos {contmulher} nulheres com menos de 20 anos.')
