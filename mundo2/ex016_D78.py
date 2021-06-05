valores = []
maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valores para posição {v}: '))) #INPUT PARA ATRIBUIR VALORES A LISTA
    if v == 0: # VERIFICA E ADICIONA O PRIMEIRO VALOR AS VARIAVEIS MAIOR E MENOR NA RESPECTIVA POSIÇÃO ADICIONADA
        maior = menor = valores[v] #AS VARIAVEIS RECEBEM OS VALORES
    else:
#DEPOIS DO PRIMEIO VALOR SER ATRIBUÍDO A PARTIR DE AGORA ELE PASSA SER ADICIONADO NAS VAIRIAVEIS MAIOR E MENOR SENDO
#ELES O MAIOR E MENOR
        if valores[v] > maior: #VERIFICA SE O MAIOR VALOR DENTRO DA LISTA É MAIOR E ADICIONA A VARIAVEL MAIOR
            maior = valores[v]
        if valores[v] < menor: #VERIFICA SE O MAIOR VALOR DENTRO DA LISTA É MENOR E ADICIONA A VARIAVEL MENOR
            menor = valores[v]
print('==='*30)
print(f'Você digitou os valores {valores}')
print(f'Em ordem crescente a lista é escrita desta forma {sorted(valores)}')
print(f'O maior valor digitado foi {maior} na(s) posição(s)', end=' ')
for i, v in enumerate(valores): #CONTADOR DE MAIORES DENTRO DA LISTA VERIFICA A POSIÇÃO SE EM 'I' O 'V' É O MAIOR VALOR E ADICIONA A QNT NA REPETIÇÃO
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor} na(s) posição(s)', end=' ')
for i, v in enumerate(valores): #CONTADOR DE MENORES DENTRO DA LISTA VERIFICA A POSIÇÃO SE EM 'I' O 'V' É O MENOR VALOR E ADICIONA A QNT NA REPETIÇÃO
    if v == menor:
        print(f'{i}...', end=' ')
print('')
print(f'A soma dos valores da lista é {sum(valores)}')