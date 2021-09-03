"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 ate 30: sobrepeso
- 30 ate 40: obesidade
- acima de 40: obesidade morbida
"""

print('-=' * 5, 'IMC', 5 * '=-')
peso = float(input('Digite o seu peso, em quilogramas:\n'))
altura = float(input('Digite sua altura, em centímetros:\n'))

imc = peso / ((altura/100)**2)

print (f'\nSeu valor de IMC é: {imc:.1f}')

if imc < 18.5:
    print('\nStatus: Abaixo do peso! Seu cosplay de holocausto!')
elif 18.5 <= imc < 25:
    print('\nStatus: Peso ideal! Boa, campeão!')
elif 25 <= imc < 30:
    print('\nStatus: Sobrepeso! Bora perder uns quilos, cu de preguiça!')
elif 30 <= imc < 40:
    print('\nStatus: Obesidade! Sua lontra!')
else:
    print('\nObesidade mórbida! Volta pro oceano, sua baleia!')
