nome = str(input('Digite uma frase: ')).strip()

print('Numero de vezes que a letra \'A\' aparece: {}'
      .format(nome.upper().count('A')))

print('A letra \'A\' aparece pela primeira vez na posição: {}'
      .format(nome.upper().find('A')+1))

print('A letra \'A\' aparece pela última vez na posição: {}'
      .format(nome.upper().rfind('A')+1)) #O 'r' faz buscar pela direita

