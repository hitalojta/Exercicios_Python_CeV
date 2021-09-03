dist = float(input('Digite a distância, em Km, da viagem:\n'))

if dist <= 200:
    preco = dist * 0.5
    print(f'Preço da viagem: {preco:.2f} reais.')
else:
    preco = dist * 0.45
    print(f'Preço da viagem: {preco:.2f} reais.')

#preco = dist * 0.5 if dist <= 200 else dist * 0.45 #simplificado
#print('Preço da passagem: {}'.format(preco))
