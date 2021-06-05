#-----NÚMERO PRIMO-----
'''num = int(input('Digite um número: '))
if num % 2 != 0 or num == 2:
    print('Este número é PRIMO!')
else:
    print('Este não primo!')'''
num = int(input('Digite o primeiro número: '))
tot = 0
for p in range(1, num + 1):
    if num % p == 0:
        print('\033[33m', end='') #PINTA A QUANTIDADE DE VEZES QUE RETORNA ESSA CONDIÇÃO NO RANGE
        tot += 1 #CONTA A QUANIDADE DE VEZES QUE ELE RETORNA E SOMA MAIS 1 - UNIDADE CONTADORA
    else:
        print('\033[31m', end='') #PINTA A QUANTIDADE DE VEZES QUE RETORNA ESSA CONDIÇÃO NO RANGE
    print('{}'.format(p), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo!') #CONDIÇÃO AFIRMANDO QUE ELE É PRIMO
else:
    print('Ele não é primo!') #CONDIÇÃO AFIRMANDO QUE ELE NÃO É PRIMO
