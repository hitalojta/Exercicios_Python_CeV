# Desafio 11

largura = float(input('Digite o valor da largura da parede em metros: '))
altura = float(input('Digite o valor da altura da parede em metros: '))
area = largura * altura
quantia = area / 2
print(f'A parede possui {area} metros quadrados de área. '
      f'Cada litro de tinta pinta uma área de 2m². Portanto, '
      f'serão necessários {quantia} litros de tinta para pintar'
      f' a parede.')

