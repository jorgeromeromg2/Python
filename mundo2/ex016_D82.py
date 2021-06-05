'''
#FORMA 1
valores = []
par = []
impar = []
while True:
    valor = int(input('Digite um número: '))
    while valor in valores:
        valor = int(input('Este número já foi digitado. Digite outro número: '))
    valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('==='*20)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')'''


#FORMA 2
valores = []
par = []
impar = []
c = 0
while True:
    valor = int(input('Digite um número: '))
    while valor in valores:
        valor = int(input('Este número já foi digitado. Digite outro número: '))
    valores.append(valor)
    c += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
for p, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('==='*20)
print(f'A lista completa é: {valores} contendo {len(valores)} números.')
print(f'A lista de pares é: {par} contendo {len(par)} números.')
print(f'A lista de impares é: {impar} contendo {len(impar)} números.')