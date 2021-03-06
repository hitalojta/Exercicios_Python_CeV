"""
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.
"""

valor = float(input('Qual o valor da casa?\nR$:'))
sal = float(input('Qual o valor do salário do comprador?\nR$:'))
anos = int(input('Em quantos anos será pago?\nAnos: '))

parcela = valor / (anos * 12)

if parcela > 0.3 * sal:
    print('\033[31mEmpréstimo NEGADO.\033[m\n'
          'Valor da parcela excede 30% do salário do comprador.\n'
          'Valor da parcela: {:.2f}\n'
          '30% do salário do comprador: {:.2f}'
          .format(parcela, 0.3 * sal))
else:
    print('\033[32mEmpréstimo APROVADO!\033[m\n'
          'Valor da parcela: {:.2f}\n'
          '30% do salário do comprador: {:.2f}'
          .format(parcela, 0.3 * sal))
