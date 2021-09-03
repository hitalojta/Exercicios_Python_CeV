"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo
"""

# from math import radians, sin, cos, tan
import math

ang = float(input('Digite o valor do ângulo, em graus: '))

# sen = math.sin(math.pi*ang/180)
# cos = math.cos(math.pi*ang/180)
# tan = math.tan(math.pi*ang/180)
sen = math.sin(math.radians(ang))  # math.radians converte graus para radianos
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'Valor do seno: {sen:.2f}\nValor do cosseno: {cos:.2f}\nValor da tangente: {tan:.2f}')
