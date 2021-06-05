from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando valores para lista... ')
    sleep(1)
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print(f'\nPRONTO! {len(lista)} valores sorteados' )


def somaPar(lista):
    print('Somando os valores da lista...')
    somap = 0
    somai = 0
    for valor in lista:
        if valor % 2 == 0:
            somap += valor
        else:
            somai += valor
    sleep(0.5)
    print(f'A soma dos valores pares na lista é {somap}')
    sleep(0.5)
    print(f'A soma dos valores impares na lista é {somai}')


numeros = []
sorteia(numeros)
somaPar(numeros)