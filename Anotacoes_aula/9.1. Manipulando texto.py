frase = 'Curso em Vídeo Python'
print(frase)
print(frase[0])
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print('''Dumping: wastes are often stored on the ground surface where 
the water table is deep. Contaminant may move to the groundwater even 
if the soil remains unsaturated''')

print(frase.upper().count('O'))#Poe pra maiusculo e conta

print(len(frase))

frase = frase.replace('Python', 'Android')
print(frase)

frase = 'Curso em Vídeo Python'

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))

dividido = frase.split() #divide em palavras
print(dividido[0])
print(dividido[2][3]) #vai na palavra e depois nas letras