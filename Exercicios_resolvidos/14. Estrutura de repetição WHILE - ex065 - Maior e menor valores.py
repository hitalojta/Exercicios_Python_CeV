"""
Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
"""

maior = menor = soma = cont = 0
perg = 'N'
while perg not in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    perg = str(input('Deseja encerrar a inserção de números? [S/N]: ')).strip().lower()[0]


print(f'\nA média entre todos os {cont} números digitados é: {soma / cont}\n'
      f'O maior valor digitado foi: {maior}\n'
      f'O menor valor digitado foi: {menor}')
