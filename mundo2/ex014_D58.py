'''from random import randint
from time import sleep
computador = randint(0, 10)  # lista aleatória
print('\033[42m-=-\033[m' * 20)
print('Vou pensar em um número entre 0 e 5...')
print('\033[42m-=-\033[m' * 20)
jogador = 0
jogadas = 0
while jogador != computador:
    jogador = int(input('\033[32mEm que número eu pensei?\033[m '))
    print('\033[34mPROCESSANDO...\033[m')
    sleep(1)
    if jogador == computador or jogador != computador:
        jogadas += 1
        if jogador == computador:
            print('\033[36mParabéns, você me venceu.\033[m')
        else:
            print('\033[37mGanhei! Eu, computador, pensei no número {} e você no {}.\033[m'.format(computador, jogador))
print('Você acertou na {}º tentativa'.format(jogadas))'''

'''
#------REFEITO------
from random import randint
computador = randint(0, 10)
jogador = 0
jogadas = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador < computador:
        print('Maior que {}...tente novamente!'.format(jogador))
    if jogador > computador:
        print('Menor que {}...tente novamente!'.format(jogador))
    jogadas += 1
print('Parabens, você acertou na {}º tentativa!'.format(jogadas))'''

#------RESOLUÇÃO-----
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente mais uma vez.')
        elif jogador > computador:
            print('Menos...tente mais uma vez.')
print('Acertou com {} tentativas.'.format(palpite))
