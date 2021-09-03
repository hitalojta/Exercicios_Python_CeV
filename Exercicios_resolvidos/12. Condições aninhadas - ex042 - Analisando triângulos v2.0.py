"""
Refaça o desafio 35 dos triangulos, acrescentando o recurso de
mostrar que tipo de triangulo será formado:
- equilatero: todos os lados iguais
- isosceles: dois lados iguais
- escaleno: todos os lados diferentes
"""

n1 = float(input('Digite o valor do primeiro lado:\n'))
n2 = float(input('Digite o valor do segundo lado:\n'))
n3 = float(input('Digite o valor do terceiro lado:\n'))

if abs(n2 - n3) < n1 < n2 + n3 and abs(n1 - n3) < n2 < n1 + n3 and abs(n1 - n2) < n3 < n1 + n2:
    print('\033[33mAs retas podem formar um triângulo!\033[m')
    if n1 == n2 == n3:
        print('\nO triângulo é \033[1;32mEQUILÁTERO\033[m porque possui todos os lados iguais!')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('\nO triângulo é \033[1;32mISÓSCELES\033[m porque possui dois lados iguais!')
    else:
        print('\nO triângulo é \033[1;32mESCALENO\033[m porque possui todos os lados diferentes!')
else:
    print('\n\033[31mNão é possível formar um triângulo.\033[m')
