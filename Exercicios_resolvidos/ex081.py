lista= []
while True:
    lista.append(int(input('Digite um número: ')))
    sair = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if sair in 'n':
        break
print(f'Você digitou os valores {lista}.')
print(f'Foram digitados {len(lista)} números.')
# lista.sort(reverse=True)
# print(f'Lista ordenada em ordem decrescente: {lista} ')
print(f'Lista ordenada em ordem decrescente: {sorted(lista, reverse=True)} ')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista.')
