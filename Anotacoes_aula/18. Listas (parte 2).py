# LISTAS PARTE 2

teste = list()
teste.append('Gustavo')
teste.append(40)
dupla = list()
dupla.append(teste) # Se fosse apenas (teste)
                     # ambas as listas estariam "conectadas"
teste[0] = 'Maria'
teste[1] = 22
dupla.append(teste) # Esse [:] faz a cópia independente
print(dupla)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
print('-'*20)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

#  ----------------------

galera2 = []
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear() # limpa a lista!
print(galera2)

for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} pessoas maiores e {totmen} pessoas menores de idade.')