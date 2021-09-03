print('{:=^30}'.format(' BANCO DOS TROUXAS '))
num = int(input('Que valor você quer sacar? R$:'))
while num < 0:
    num = int(input('\033[31mValor inválido!\033[m\n'
                      'Que valor você quer sacar?\nR$:'))
if num >= 50:
    ced50 = num // 50
    print(f'Total de {ced50:.0f} cédulas de R$:50.00')
    num %= 50
if num >= 20:
    ced20 = num // 20
    print(f'Total de {ced20:.0f} cédulas de R$:20.00')
    num %= 20
if num >= 10:
    ced10 = num // 10
    print(f'Total de {ced10:.0f} cédulas de R$:10.00')
    num %= 10
if 0 < num < 10:
    ced1 = num
    print(f'Total de {num:.0f} cédulas de R$:1.00')
print('='*30)
print('Volte sempre ao Banco dos Trouxas! Tenha um bom dia!')


#  dos comentários do Youtube
'''valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [100, 50, 20, 10, 5, 2, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')'''


#  da vídeo aula:
'''valor = int(input('Que valor você quer sacar? R$:'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$:{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
'''