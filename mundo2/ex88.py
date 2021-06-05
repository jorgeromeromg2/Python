from random import randint
from time import sleep
jogo = []
jogo1 = []
jogadas = int(input('Quantos jogos você quer que eu sorteie? '))
print(3*'-=', f'SORTEANDO {jogadas} NÚMEROS', 3*'-=')
for j in range(1, jogadas+1):
    jogo.clear()
    jogo1 = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    jogo.append(jogo1[:])
    jogo1.clear()
    print(f'Jogo {j:^1}: {jogo}')
    sleep(1)
print('Boa sorte')
