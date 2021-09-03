"""
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte.
Seu programa deverá ler um numero pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
"""

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20 a ser escrito por extenso: '))
while num not in range (0, 21):
    num = int(input('Número inválido. Digite de 0 a 20: '))
print(f'O número {num} por extenso é {contagem[num]}.')
