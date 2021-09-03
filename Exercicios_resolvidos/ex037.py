num = int(input('=== Digite um número inteiro qualquer: '))
print('\n=== Qual será a base de conversão?\n\n'
      '[ 1 ] para \033[1;33mBINÁRIO\033[m\n'
      '[ 2 ] para \033[1;33mOCTAL\033[m\n'
      '[ 3 ] para \033[1;33mHEXADECIMAL\033[m\n')
opcao = int(input('=== Sua opção: '))
if opcao == 1:
    print(f'\n{num} convertido para BINÁRIO é igual a \033[4m{bin(num)[2:]}\033[m.')
elif opcao == 2:
    print(f'\n{num} convertido para OCTAL é igual a \033[4m{oct(num)[2:]}\033[m')
elif opcao == 3:
    print(f'\n{num} convertido para HEXADECIMAL é igual a \033[4m{hex(num)[2:]}\033[m')
else:
    print('\n\033[31mOpção de conversão inválida, o programa será encerrado.\033[m')
