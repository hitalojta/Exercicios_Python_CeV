# LISTAS v = [] ou v = list()
lanche = ['hamburguer', 'suco', 'pizza', 'picolé']
print(lanche)
# Adiciona novo elemento no final da lista
lanche.append('Cookie')
print(lanche)
# Adiciona o elemento na posição dada e a lista aumenta
lanche.insert(1, 'hot dog')
print(lanche)
# Apaga o elemento na posição dada
del lanche[3]
print(lanche)
# Apaga o último elemento
lanche.pop()  # pode apagar também numa posição específica pop(x)
print(lanche)
# Apaga o 1º elemento nomeado que está na lista
lanche.remove('suco')
print(lanche)
# Cria uma lista
valores = list(range(4, 11))
print(valores)
# Para deixar em ordem
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
sorted(valores) # <-- outra forma
print(valores)
valores.sort(reverse=True)
print(valores)
# Para saber quantos elementos há dentro da lista
print('Nº de elementos dentro da lista:', len(valores))
