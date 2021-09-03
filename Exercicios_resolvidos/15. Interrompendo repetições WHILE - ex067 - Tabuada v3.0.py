"""
Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
"""

print('\033[33m----- TABUADA -----\033[m')
while True:
    num = int(input('Quer ver a tabuada de que valor? (valor negativo encerra): '))
    if num < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f' {num} X {c:>2} = {num * c:>2}')
    print('-'*30)
print('-'*30)
print('\n\033[31mPROGRAMA ENCERRADO. Volte sempre!\033[m')