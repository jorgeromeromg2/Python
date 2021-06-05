#-----PROGRESSÃO ARITMÉTICA------
'''num1 = int(input('Digite o primeiro termo da P.A: '))
num3 = int(input('Digite a razão da P.A: '))
for n in range(num1, 10*num3, num3):
    print('O termos da P.A são {} '.format(n))'''

primeiro = int(input('Primerio termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' » ')
print('FIM')