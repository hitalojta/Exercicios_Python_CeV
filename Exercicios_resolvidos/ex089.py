nomes = []
notas = []
temp = []
while True:
    nomes.append(str(input('Nome: ')).strip().title())
    for c in range(1, 3):
        nota = float(input(f'Nota {c}:'))
        while nota > 10 or nota < 0:
            nota = float(input(f'\033[31mValor inválido.\033[m\nNota {c}:'))
        temp.append(nota)
    notas.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('\033[31mOpção inválida.\033[m\nQuer continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print('-' * 25)
print(f'No.  NOME        MÉDIA')
print('-' * 25)
for num, name in enumerate(nomes):
    media = (notas[num][0] + notas[num][1]) / 2
    print(f'{num}    {name: <10}{media: >7.2f}')
print('-' * 25)
while True:
    aluno = int(input('Digite o No. do aluno cujas notas deseja ver (999 encerra): '))
    while aluno < 0 or aluno > len(nomes) - 1 and aluno != 999:
        aluno = int(
            input('\033[31mNúmero inválido.\033[m\nDigite o No. do aluno cujas notas deseja ver (999 encerra): '))
    if aluno == 999:
        break
    print(f'Notas de {nomes[aluno]} são {notas[aluno]}')
print('FINALIZANDO...\n <<< VOLTE SEMPRE >>>')

# do Guanabara:
# ficha = list()
# while True:
#     nome = str(input('Nome: ')).strip().title()
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
#     if resp in 'Nn':
#         break
# print('-='*30)
# print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-'*26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[0]:>8.1f}')
# while True:
#     print('-'*35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')