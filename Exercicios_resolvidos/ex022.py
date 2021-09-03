#nome = str(input('Digite seu nome: ')).strip()
nome = str(input('Digite seu nome: '))

nome = nome.strip()
cont = len(nome) - nome.count(' ')

nomesp = nome.split()
#nome1 = nomesp[0] -> desnecessário, só alonga, já aplica direto len(nomesp[0])

#nome.find(' ') -> Contaria o número de letras antes do primeiro espaço. Portanto, contaria o numero de letras do primeiro nome.

print(f'Letras maiúsculas: {nome.upper()}\nLetras minúsculas: {nome.lower()}'
      f'\nQuantas letras ao todo (sem espaço): {cont}\n'
      f'Quantas letras tem o primeiro nome: {len(nomesp[0])}')