"""
Escreva um programa que converta uma temperatura digitada em
Celsius (ºC) e converta para Fahrenheit (ºF)
"""

# Desafio 14

tc = float(input('Insira o valor da temperatura, em Celsius: '))

tf = (tc * (9/5)) + 32

print(f'{tc} graus Celsius equivalem a {tf:.1f} graus Fahrenheit.')