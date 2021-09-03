n1 = float(input('Digite a primeira nota:\n'))
n2 = float(input('Digite a segunda nota:\n'))

m = (n1 + n2) / 2

print(f'A sua média é: {m:.1f}\n')

if m >= 6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado.')

print('Aprovado!' if m >= 6 else 'Reprovado.') #versao simplificada
