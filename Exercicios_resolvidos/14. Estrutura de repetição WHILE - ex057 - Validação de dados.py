"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores M ou F. Caso esteja errado peça para digitar novamente
até ter um valor correto.
"""

sexo = str(input('Digite o sexo da pessoa [F/M]: ')).strip()[0]
#  Para pegar apenas a primeira letra, usou o [0] acima
while sexo not in 'FfMm':
    sexo = str(input('Opção inválida. Digite novamente o sexo da pessoa [F/M]: ')).strip()[0]
if sexo in 'Ff':
    print('\nSexo FEMININO registrado com sucesso.')
else:
    print('\nSexo MASCULINO registrado com sucesso.')

print('\n----- Fim -----')
