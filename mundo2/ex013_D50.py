#-------SOMA ENTRE NÚMEROS -----
p = 0
i = 0
cont1 = 0
cont2 = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        p += n
        cont1 += 1
    else:
        i += n
        cont2 += 1
print('\033[1:32mO somatório dos {} números pares digitados é: {}\033[m'.format(cont1, p))
print('\033[1:33mO somatório dos {} números ímpares digitados é: {}\033[m'.format(cont2, i))
