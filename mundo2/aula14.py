'''for c in range(1, 3):
    print(c, end=' ')
print('FIm')'''
'''
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('Fim')'''

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim!')

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')'''

'''res = 'S'
while res == 'S':
    num = int(input('Digite um valor: '))
    res = str(input('Deseja continuar[S/N]: ')).upper()
print('Fim')'''

'''num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1 #A CADA NÚMERO PAR DIGITADO O QUANTITATIVO É ADICIONADO. PARA SOMAR É PRECISO SER ASSIM [par += num ]
        else:
            impar += 1 #A CADA NÚMERO IMPAR DIGITADO O QUANTITATIVO É ADICIONADO
print('A quantidade de números pares é {}'.format(par))
print('A quantidade de números impares é {}'.format(impar))
print('Acabou')
'''