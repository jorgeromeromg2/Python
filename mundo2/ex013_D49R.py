#-----TABUADA--------
num = int(input('Digite um número para consultar a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
