'''num = 4
print(20 * str('-=-'))
print('Estou pensando em um número, tente adivinhar...')
print(20 * str('-=-'))
num1 = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
if num1 == num:
    print('Parabéns, você acertou!')
else:
    print('Tente novamente!')'''

from random import randint
from time import sleep
computador = randint(0, 5)  # lista aleatória
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você me venceu.')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))