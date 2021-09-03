#from math import hypot
import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

#hip = math.sqrt(pow(co, 2) + pow(ca, 2))
hip = math.hypot(co, ca) #calculo de hipotenusa
#hip = hypot(co, ca)

print('Um triângulo retângulo de catetos {} e {} '
      'possui uma hipotenusa de valor {:.1f}.'.format(co, ca, hip))
