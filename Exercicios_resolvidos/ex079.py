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
