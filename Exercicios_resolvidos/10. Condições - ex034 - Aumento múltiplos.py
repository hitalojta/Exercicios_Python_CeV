"""
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor de seu aumento.
Para salários acima de R$:1250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%
"""

sal = float(input('Qual o valor do salário?\n'))

if sal > 1250:
    print(f'Aumento salarial de 10%: {sal*0.1:.2f}\nValor final: {sal*1.1:.2f}')
else:
    print(f'Aumento salarial de 15%: {sal*0.15:.2f}\nValor final: {sal*1.15:.2f}')
