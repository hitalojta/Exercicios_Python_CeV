nome = str(input('Digite o nome da pessoa: '))\
    .upper().replace('-', ' ').split()

print('A pessoa possui o sobrenome Silva? -> {}'
      .format('SILVA' in nome))
