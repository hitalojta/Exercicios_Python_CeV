dados = []
temp = []
pesomax = pesomin = 0
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso em Kg: ')))
    if len(dados) == 0:
        pesomax = pesomin = temp[1]
    else:
        if temp[1] >= pesomax:
            pesomax = temp[1]
        if temp[1] < pesomin:
            pesomin = temp[1]
    dados.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Opção inválida. Continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'n':
        break
print('-='*20)
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {pesomax}Kg. Peso de ', end='')
for p in dados:
    if p[1] == pesomax:
        print(f'{p[0]}', end='; ')
print(f'\nO menor peso foi de {pesomin}Kg. Peso de ', end='')
for p in dados:
    if p[1] == pesomin:
        print(f'{p[0]}', end='; ')

# INPUT SEM CLEAR DA LISTA:
#     guys.append ( [ input('Digite o nome ') ,  float ( input('Digite o peso') ) ] )