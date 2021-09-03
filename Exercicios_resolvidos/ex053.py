palavra = str(input('Digite a frase a ser analisada:\n-> ')).lower().split()
junto = ''.join(palavra)

checapar = len(junto) % 2

dif = 0
if checapar != 0:
    for c in range(0, int((len(junto)-1)/2), 1):
        c2 = (len(junto)-1) - c
        if junto[c] != junto[c2]:
            dif += 1
    if dif == 0:
        print('\nA frase digitada é \033[32mSIM um palíndromo!\033[m')
    else:
        print('\nA frase digitada \033[31mNÃO é um palíndromo!\033[m')
else:
    for c in range(0, int(len(junto)/2), 1):
        c2 = (len(junto)-1) - c
        if junto[c] != junto[c2]:
            dif += 1
    if dif == 0:
        print('\nA frase digitada é \033[32mSIM um palíndromo!\033[m')
    else:
        print('\nA frase digitada \033[31mNÃO é um palíndromo!\033[m')
