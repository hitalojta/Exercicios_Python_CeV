n = input('Digite um valor: ')
print(n)
print(type(n))

n2 = str(input('Digite um valor: '))
print(n2)
print(type(n2))

n3 = int(input('Digite um valor: '))
print(n3)
print(type(n3))

n4 = float(input('Digite um valor: '))
print(n4)
print(type(n4))

n5 = bool(input('Digite um valor: '))
print(n5)
print(type(n5))

n6 = input('Digite um valor: ')
print(n6.isalpha()) #verifica se só tem letras
print(n6.isnumeric()) #verifica se é numerico
print(n6.isalnum()) #verifica se é alfanumerico
print(n6.isupper()) #verifica se tudo maiusculo
print(n6.islower()) #verifica se tudo minusculo
print(n6.isspace()) #verifica se é espaço