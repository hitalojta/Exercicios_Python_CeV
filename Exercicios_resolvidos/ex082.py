lista = []
listai = []
listap = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    sair = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if sair in 'n':
        break
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listap}')
print(f'A lista de ímpares é {listai}')
