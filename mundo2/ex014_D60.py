#----FATORIAL-----
'''from math import factorial
fat = int(input('Digite o número e descubra seu fatorial: '))
num1 = factorial(fat)
print('O fatorial de {} é {}'.format(fat, num1))'''

'''n1 = int(input('Digite um número para calcular o fatorial: '))
f = 1
print('Calculando {}! = '.format(n1), end='')
while n1 > 0:
    print('{}'.format(n1), end='')
    print(' x ' if n1 > 1 else ' = ', end='')
    f *= n1
    n1 -= 1
print('{}'.format(f))'''

fat = int(input('Digite um número: '))
c = 1
print('Calculando {}! = '.format(fat), end='')
for n in range(fat, 0, -1):
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    c *= n
print(' {} '.format(c))
