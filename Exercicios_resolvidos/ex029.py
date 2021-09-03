velo = float(input('Digite o valor da velocidade do carro, em Km/h:\n'))

if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você foi multado. Valor: {multa:.2f} reais.')
else:
    print('Velocidade abaixo do limite. Tudo certo.')
