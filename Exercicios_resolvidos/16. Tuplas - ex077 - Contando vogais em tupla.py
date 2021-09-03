"""
Crie um programa que tenha uma tupla com varias palavras
(nao usar acentos). Depois disso, voce deve mostrar, para cada
palavra, quais sao as suas vogais
"""

times = ('Atlético', 'Internacional', 'Palmeiras',
         'Goiás', 'Botafogo', 'Grêmio', 'Chapecoense', 'Fortaleza',
         'Bragantino', 'Vasco', 'Ceará', 'Bahia',
         'Sport', 'Flamengo', 'Corinthians',
         'Santos', 'Fluminense', 'Coritiba')
for p in times:
    print(f'\nA palavra {p.upper()} possui as vogais:', end=' ')
    for letras in p:
        if letras in 'aáàâãeéêiíoóôõuú':
            print(letras.lower(), end=' ')
