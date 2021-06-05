#----SEQUENCIA DE FIBONNACI------
print('-=-'*10)
print('Sequência de Fibonacci')
print('-=-'*10)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*20)
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' - {}'.format(t3), end='')
    cont += 1
print(' Fim')