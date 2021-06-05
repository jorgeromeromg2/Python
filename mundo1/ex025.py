velocidade = float(input('Digite sua velocidade: '))
multa = float(velocidade - 80)*7
limite = (velocidade - 80)
if velocidade <= 80:
    print('Você está dentro do limite de velocidade.')
else:
    print('Você ultrapassou o limite permitido de 80Km. Terá que pagar uma multa de R$ {} pelos {}Km excedidos.'.format
          (multa, limite))
