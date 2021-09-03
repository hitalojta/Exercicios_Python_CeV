nome = input ('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}.\nO produto é {m}.\nA divisão é {d:.3f}.', end='<<>>')
#print('A soma é {}.\nO produto é {}.\nA divisão é {:.3f}.'.format(s, m, d), end='<<>>')
print('Divisão inteira {} e potência {}.'.format(di, e))
