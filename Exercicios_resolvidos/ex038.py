n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('\nDigite o segundo número inteiro: '))

if n1 > n2:
    print(f'\nO primeiro valor {n1} é maior!')
elif n1 < n2:
    print(f'\nO segundo valor {n2} é maior!')
else:
    print('\nNão existe valor maior, os dois são iguais.')
