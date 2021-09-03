nome = str(input('Digite o nome da cidade: '))\
    .upper().replace('-', ' ').split() #split já dá um strip automatico

print('A cidade começa com o nome \'Santo\'? -> {}'
      .format(nome[0] == 'SANTO'))
