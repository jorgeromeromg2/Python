'''def contador(i=0, f=0, p=0): # ZERO IGUALADO A FUNÇÃO SUPRI A AUSENCIA DO PROGRAMA PRINCIPAL
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contaegm
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    s = i + f + p
    print(f'A soma vale {s}')


# Programa Principal - Escopo Global
# help(contador) IMPRIME NA TELA A FUNÇÃO DO PROGRAMA
contador(2, 5, 9)
contador(1)
contador(f=6, p=6)'''
import random

'''def funcao(a):
    from random import randint
    global n1
    n1 = 4
    a += 1
    print(f'N1 dentro vale {n1}')
    print(f'A dentro vale {a}')


n1 = 2
funcao(n1)
print(f'N1 global vale {n1}')'''

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 7, 1)
r2 = somar(5, 8)
r3 = somar(4)
print(f'A soma dos valores é {r1}, {r2} e {r3}')
'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# Programa principal
while True:
    num = int(input('Digite um número: '))
    if par(num):
        print('É par!')
    else:
        print('Não é par!')
    continuar = str(input('Deseja continuar ? '))
    if continuar not in 'Ss':
        break