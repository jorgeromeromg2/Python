valores = []
valor = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        valor = int(input('Este valor já existe. Digite outro valor: '))
    else:
        valores.append(valor)
    continuar = str(input('Deseja continuar? [S/N]'))
    valores.sort(reverse=True)
    if continuar in 'Nn':
        break
print('==='*20)
print(f'Você digitou {len(valores)} elementos.')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista')
print(f'O valores em ordem decrescente são {valores}')