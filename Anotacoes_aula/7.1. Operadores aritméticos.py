n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

# Adição
print('Para adição, utiliza-se \'+\'.')
print('A soma de {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
# Subtração
print('Para subtração, utiliza-se \'-\'')
print('A subtração de {} menos {} é igual a {}.'.format(n1, n2, n1 - n2))
# Multiplicação
print('Para multiplicação, utiliza-se \'*\'')
print('A multiplicação de {} por {} é igual a {}.'.format(n1, n2, n1 * n2))
# Divisão
print('Para divisão, utiliza-se \'/\'')
print('A divisão de {} por {} é igual a {}.'.format(n1, n2, n1 / n2))
# Potência
print('Para potenciação, utiliza-se \'**\'')
print('O valor de {} elevado a {} é igual a {}.'.format(n1, n2, n1 ** n2))
# Divisão inteira
print('Para divisão inteira, utiliza-se \'//\'')
print('A divisão inteira de {} por {} é igual a {}.'.format(n1, n2, n1 // n2))
# Resto da divisão
print('Para resto da divisão, utiliza-se \'%\'')
print('O resto da divisão de {} por {} é igual a {}.'.format(n1, n2, n1 % n2))

#-- Ordem de Procedência
#1 - ()
#2 - **
#3 - *, /, //, %
#4 - +, -