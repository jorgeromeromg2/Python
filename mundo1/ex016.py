'''import math #OPERACOES MATEMATICAS
n1 = float(input('Digite um número: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(n1, math.trunc(n1)))

from math import trunc
n1 = float(input('Digite um número: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(n1, trunc(n1)))'''

n1 = float(input('Digite um número: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(n1, int(n1)))