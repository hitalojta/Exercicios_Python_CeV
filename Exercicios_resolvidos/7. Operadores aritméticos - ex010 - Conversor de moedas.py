"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar
"""

# Desafio 10

grana = float(input('Quanto dinheiro você tem na carteira? R$:'))
print(f'Na cotação de R$:3,27, você pode comprar {(grana / 3.27):.2f} dólares.')
