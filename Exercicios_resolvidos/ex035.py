n1 = float(input('Digite o valor do primeiro lado:\n'))
n2 = float(input('Digite o valor do segundo lado:\n'))
n3 = float(input('Digite o valor do terceiro lado:\n'))

if abs(n2 - n3) < n1 < n2 + n3 and abs(n1 - n3) < n2 < n1 + n3 and abs(n1 - n2) < n3 < n1 + n2:
    print('As retas podem formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')
