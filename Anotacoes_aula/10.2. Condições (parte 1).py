tempo = int(input('Quantos anos tem o seu carro? '))

if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho.')

print('Carro novo!' if tempo <= 3 else 'Carro velho.') #forma reduzida

print('--FIM--')
