'''n = soma = cont = 0
while True:
    n = int(input('Digite um número para ser somado: '))
    if n == 999:
        break
    soma += n
    cont += 1
#print('A soma dos {} números digitados é {}.'.format(cont, soma))
print(f'A soma dos {cont:^10} números digitados é {soma:-<5}.')'''


resp = str(input('Digite uma letra: ')).strip().upper()[0]
print(resp)

