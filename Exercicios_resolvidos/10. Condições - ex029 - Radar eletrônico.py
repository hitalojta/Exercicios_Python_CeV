"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$:7,00 por cada Km
acima do limite
"""

velo = float(input('Digite o valor da velocidade do carro, em Km/h:\n'))

if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você foi multado. Valor: {multa:.2f} reais.')
else:
    print('Velocidade abaixo do limite. Tudo certo.')
