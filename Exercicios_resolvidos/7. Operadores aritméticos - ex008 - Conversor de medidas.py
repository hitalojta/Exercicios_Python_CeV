"""
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milimetros
"""

# Desafio 8

medida = float(input('Digite a medida de comprimento, em metros: '))
cent = medida * 100
mili = medida * 1000
print('{} metros equivalem a {:.0f} centímetros e {:.0f} milímetros.'.format(medida, cent, mili))

