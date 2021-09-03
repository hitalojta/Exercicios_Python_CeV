#  variáveis compostas (tuplas, listas, dicionarios)
#                         ()      []         {}

#  TUPLAS (entre parenteses, apesar de ser desnecessaria
#  Tuplas são IMUTAVEIS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche[0])
print(lanche[3])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
print(lanche[-3:])
print('---'*10)
print(sorted(lanche)) #põe em ordem alfabetica
print('=-='*10)
#  lanche[1] = refrigerante -> não pode pq é imutável

for comida in lanche:  #lanche fica como range
    print(f'Vou comer {comida}.')
print('=-='*10)
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')
print('=-='*10)
for pos, Comida in enumerate(lanche):  #pega a posição e o item correspondente
    print(f'Vou comer {Comida} na posição {pos}')
print('=-='*10)
a = (2, 5, 4)
b = (5, 8, 1, 2)
# a ordem dos fatores ALTERA o resultado
c = b + a #  é diferente de 'a + b'
print(f'c =', c)
print(f'Quantos elementos tem em \'c\': {len(c)}')
print(f'Quantos 5 tem em \'c\': {c.count(5)}')
print(f'Em que posição está o 5: {c.index(5)}')
print(f'Em que posição está o 5 após a posição 1: {c.index(5, 1)}')
print('=-='*10)
pessoa = ('Gustavo', 39, 'M', 99.88) #  pode ser elementos alpha e num
print(pessoa)
del(pessoa) #  apaga da memória

