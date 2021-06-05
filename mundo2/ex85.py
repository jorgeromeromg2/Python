'''valores = []
par = []
impar = []
for v in range(1, 8):
    valores.append(int(input(f'Digite o {v}º valor: ')))
    if valores[0] % 2 == 0:
        par.append(valores[:])
    elif valores[0] % 2 != 0:
        impar.append(valores[:])
    valores.clear()
print(sorted(par))
print(sorted(impar))'''

numeros = [[], []]
valor = 0
for v in range(1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('==='*30)
print(f'Os números pares digitados são: {numeros[0]}')
print(f'Os números ímpares digitados são: {numeros[1]}')