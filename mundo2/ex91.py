from random import randint
from time import sleep
from operator import itemgetter
lista = {'Jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6)} #O DICIONARIO CRIADO SEM A ANECESSIDADE DE SUPLICIDADE NO INICIO.
print('Valores sorteados em um dado: ')
for k, v in lista.items():
    print(f'O {k} tirou {v} no dado.') #ITEM = CHAVE(KEY) E VALOR(VALUE) DA CHAVE.
    sleep(1)
print('==='*10)
print(f'{"==":>3}{" RANKING DOS JOGADORES":>3}{"==":>3}')
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True) #LISTA CRIADA SEM A NECESSIDADE DE DECLARA-LA ISOLADA
#AUTOMATICAMENTE O DICIONÁRIO FOI INSERIDO DENTRO DA LISTA.
print('---'*15)
for i, v in enumerate(ranking):
    print(f'{" ":>4}{i+1}º Lugar: {v[0]} com {v[1]}.') #'I' ENUMERA, V'RANKING[POSIÇÃO]
    sleep(1)
