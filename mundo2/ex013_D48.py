#------NUMEROS IMPARES DIVISIVEIS POR 3--------
'''primeiro = int(input('Digite o primeiro número da sequência: '))
ultimo = int(input('Digite o último número da sequência: '))
for c in range(primeiro, ultimo):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
print('Na contagem de {} à {} os números em tela são impares múltiplos de 3'.format(primeiro, ultimo))'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1   #QUANTIDAE DE VALORES SELECIONADOS
        soma += c   #SOMATORIO DOS VALORES SELECIONADOS
        #print(c, end=' ')
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))