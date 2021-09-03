"""
Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os numeros pares
"""

# num = (int(input('Digite o 1º número: ')),
#        int(input('Digite o 2º número: ')),
#        int(input('Digite o 3º número: ')),
#        int(input('Digite 0 4º número: ')))
num = tuple(int(input(f'Digite o {i+1}º numero: ')) for i in range(4))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vez(es).')
try: #  só verifica uma vez, nao fica repetindo feito while. Evita dar erro caso não seja o tipo certo (str, int, float, bool)
    print(f'O valor 3 apareceu primeiro na posição {num.index(3)+1}')
except:
    print('Não existe o número 3 na tupla.')
print('Os números pares são: ', end='')
for c in num:
    if c % 2 == 0 and c != 0:
        print(c, end=' ')
