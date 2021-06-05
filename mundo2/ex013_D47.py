#------NUMEROS E SEU INTERVALO------PARES DO 2 AO 50------
'''print('Intervalo de números.')
primeiro = int(input('Digite o primeiro número da sequência: '))
ultimo = int(input('Digite o último número da sequência: '))
intervalo = int(input('Qual intervalo deseja: '))
for c in range(primeiro, ultimo+1, intervalo):
    print(c)
print('Sua sequência iniciou em {} e terminou em {} com um intervalo de {} em {}.'.format(primeiro, ultimo, intervalo,
                                                                                          intervalo))'''

for n in range(2, 51, 2):
    print(n, end=' ')
print('Fim')