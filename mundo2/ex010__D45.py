#------PEDRA PAPEL E TESOURA----
from random import randint
import emoji
from time import sleep
computador = randint(1, 3) #NUMEROS ALEATORIOS
print(8 * '--')
print('VAMOS JOGAR.')
print(8 * '--')
jogador = int(input(' Digite \n 1 - PEDRA  \n 2 - PAPEL \n 3 - TESOURA \n Escolha uma opção: '))
if jogador == 1 or jogador == 2 or jogador == 3:
    sleep(1)
    print('\033[3:32mJO\033[m')
    sleep(1)
    print('\033[3:32mKEN\033[m')
    sleep(1)
    print('\033[3:32mPÔ..\033[m')
    sleep(1)
    if jogador == 1 and computador == 2:
        print(emoji.emojize(''' Você escolheu :fist: 
O computador escolheu :hand:.
Você perdeu! :weary:''', use_aliases=True))
    elif jogador == 2 and computador == 1:
        print(emoji.emojize('''' Você escolheu :hand:
O computador escolheu :fist:.
Você ganhou! :stuck_out_tongue_closed_eyes:''', use_aliases=True))
    elif jogador == 1 and computador == 3:
        print(emoji.emojize('''Você escolheu :fist:
O computador escolheu :v:.
Você ganhou! :stuck_out_tongue_closed_eyes:''', use_aliases=True))
    elif jogador == 1 and computador == 1:
        print(emoji.emojize('''Você escolheu :fist:
O computador escolheu :fist:.
Você empatou! :weary:''', use_aliases=True))
    elif jogador == 2 and computador == 2:
        print(emoji.emojize('''Você escolheu :hand:
O computador escolheu :hand:.
Você empatou! :weary:''', use_aliases=True))
    elif jogador == 2 and computador == 3:
        print(emoji.emojize('''Você escolheu :hand:
O computador escolheu :v:.
Você perdeu! :weary:''', use_aliases=True))
    elif jogador == 3 and computador == 1:
        print(emoji.emojize('''Você escolheu :v:
O computador escolheu :fist:.
Você perdeu! :weary:''', use_aliases=True))
    elif jogador == 3 and computador == 2:
        print(emoji.emojize('''Você escolheu :v:
O computador escolheu :hand:.
Você ganhou! :stuck_out_tongue_closed_eyes:''', use_aliases=True))
    elif jogador == 3 and computador == 3:
        print(emoji.emojize('''Você escolheu :v:
O computador escolheu :v:.
Você empatou!''', use_aliases=True))
else:
    print('Você digitou uma opção inexistente. Tente novamente!')