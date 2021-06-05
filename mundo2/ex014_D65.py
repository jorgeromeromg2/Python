#MAIOR E MENOR VALORES
n = soma = cont = media = maior = menor = 0
continuar = ''
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma/cont
print('Você digitou {} números que somados são {} e a média foi {}.'.format(cont, soma, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
