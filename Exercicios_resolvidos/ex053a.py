frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#  inverso = junto[::-1] <- isso elimina a necessidade do 'for'

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Portanto, temos um palíndromo!')
else:
    print('Portanto, não temos um palíndromo.')
