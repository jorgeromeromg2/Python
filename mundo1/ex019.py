#------ SORTEANDO DADOS DA LISTA ---------
import random
dado1 = input('Digite o primerio dado: ')
dado2 = input('Digite o segundo dado: ')
dado3 = input('Digite o terceiro dado: ')
dado4 = input('Digite o quarto dado: ')
lista = [dado1, dado2, dado3, dado4]
escolha = random.choice(lista)
print('O dado escolhido é {}.'.format(escolha))
