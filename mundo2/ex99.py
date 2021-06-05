from random import randint
from time import sleep


def maior(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        sleep(0.5)
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    sleep(1)
    print(f'Foram informador {cont} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')


maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10))
maior()