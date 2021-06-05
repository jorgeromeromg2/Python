valor = list()
while True:
    v = (int(input('Digite um valor: ')))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('O valor já existe. Não será adicionado.')
    continuar = str(input('Deseja adicionar mais valores? [S/N]'))
    if continuar in 'Nn':
        break
print('==='*30)
valor.sort()
print(f'Você digitou os valores {valor}')