from random import randint
from time import sleep
jogo = []
jogadas = int(input('Quantos jogos você quer que eu sorteie? '))
print(3*'-=', f'SORTEANDO {jogadas} NÚMEROS', 3*'-=')
for j in range(1, jogadas+1):
    for t in range(0, 7):
        jogo = [randint(1, 60), randint(0, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
        jogo.sort()
    print(f'Jogo {j:^1}: {jogo}')
    sleep(1)
print(3*'-=', 'BOA SORTE', 3*'-=')

'''lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'{i}, {l}')
    sleep(1)'''