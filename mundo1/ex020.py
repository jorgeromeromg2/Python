#-------- ESCOLHENDO A LISTA E ORDENANDO --------
from random import shuffle
dado1 = input('Digite o primerio dado: ')
dado2 = input('Digite o segundo dado: ')
dado3 = input('Digite o terceiro dado: ')
dado4 = input('Digite o quarto dado: ')
lista = [dado1, dado2, dado3, dado4]
shuffle(lista)
print('O dado escolhido em sua ordem é: ')
print(lista)