# LAÇOS DE REPETIÇÃO

for c in range(0, 3): #contagem começa do zero
    print(c)
print('\n')
for c2 in range(6, 0, -1):
    print(c2)
print('\n')
for c3 in range (10, 0, -2):
    print(c3)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c4 in range(inicio, fim + 1, passo):
    print(c4)
print('FIM')

s = 0
for c5 in range(0, 4):
    n = int(input('Digite um valor inteiro: '))
    s += n #s = s + n
print(f'O somatório dos números é: {s}')