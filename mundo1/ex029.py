dist = float(input('Digite a distância da viagem: '))
acima = float(dist * 0.50)
abaixo = float(dist * 0.45)
if dist <= 200:
    print('O valor cobrado será R$ {} reais'.format(acima))
else:
    print('O valor cobrado será R$ {} reais'.format(abaixo))
