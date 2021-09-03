"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos
um modulo chamado dado. Crie uma função chamada leiadinheiro()
que seja capaz de funcionar como a função input(), mas com uma
validação de dados para aceitar apenas valores que sejam monetarios.
"""

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiadinheiro('Digite o preço: R$:')
moeda.resumo(p, 35, 22)
