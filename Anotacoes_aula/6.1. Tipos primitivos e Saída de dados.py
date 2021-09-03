# Desafio 3
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1+n2
#print('A soma entre', n1, 'e', n2, 'resulta em {}!'.format(s)) #[FORMATO ANTIGO]
print('A soma entre {0} e {1} resulta em {2}!'.format(n1, n2, s))

print(type(n1))
print(type(n2))
print(type(s))

#Desafio 4

nome = input('Digite algo para verificação: ')
print('O tipo primitivo é {}.'.format(type(nome)))

print('É alfabetico, apenas?', nome.isalpha()) #False pq tem espaço
print('É numérico?', nome.isnumeric()) #verifica se é numerico
print('É alfanumérico?', nome.isalnum()) #verifica se é alfanumerico
print('Tudo maiúsculo?', nome.isupper()) #verifica se tudo maiusculo
print('Tudo minúsculo?', nome.islower()) #verifica se tudo minusculo
print('É apenas espaço?', nome.isspace()) #verifica se é espaço