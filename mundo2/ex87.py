matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma1 = soma2 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para posição [{l}, {c}]: ')))
        #soma2 += matriz[l][2] # MINHA SOLUÇÃO - SOMA DA TERCEIRA LINHA
        if matriz[l][c] % 2 == 0:
            soma1 += matriz[l][c] #SOMA DOS VALORES PARES
        '''if len(matriz) == 0: #MINHA SOLUÇÃO - MAIOR VALOR DAS LINHAS
            maior = matriz[1][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]'''
print('==='*10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {soma1}')
for l in range(0, 3): # SOLUÇÃO DO CURSO - SOMA DA TERCEIRA COLUNA
    soma2 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma2}')
for c in range(0, 3): # SOLUÇÃO DO CURSO - MAIOR VALOR DAS LINHAS
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')