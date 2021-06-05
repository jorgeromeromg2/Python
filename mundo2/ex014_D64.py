cont = n = total = 0
while total < 999:
    total = int(input('Digite um número [999 para parar]: '))
    if total != 999:
        n += total
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, n))

'''
n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: ))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: )) #O FLAG ESTANDO NA ULTIMA LINHA FAZ ELE SAIR DO WHILE
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))'''