#FATIAMENTO DE STRING

frase = 'Curso em vídeo Python!'

print(frase)

print('Numero de caracteres:', len(frase))

print('A quantidade de letras \'o\' no string é:', frase.count('o'))

print('A quantidade de letras \'o\' no fatiamento de 0 a 12 é:', frase.count('o', 0, 13))

print('Onde começou o trecho \'deo\' no string:', frase.find('deo')) #Se retornar -1 é pq não existe na string analisada.

print('Existe a palavra \'Curso\' na string? ', 'Curso' in frase)

print('Trocar a palavra \'Python\' por \'Android\':\n', frase.replace('Python', 'Android')) #troca mas não salva. Para isso, tem que atribuir a uma variavel

print('Tudo em maiúsculo:', frase.upper())

print('Tudo em minúsculo:', frase.lower())

print('Apenas o primeiro caractere ficará maiúsculo do string:', frase.capitalize())

print('Cada palavra ficará com a primeira letra maiúscula:', frase.title())

frase2 = '   Aprenda Python  '

print('Remove os espaços inuteis da string, da esquerda e direita', frase2.strip())

print('Remove os espaços inúteis da string da direita:', frase2.rstrip())

print('Remove os espaços inúteis da string da esquerda:', frase2.lstrip())

print('Separa o string em palavras individuais:', frase.split()) #cada palavra vira uma posição na string

print('Junta o string que está separado:', ''.join(frase)) #???