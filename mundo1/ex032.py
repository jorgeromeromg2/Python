salario = float(input('Digite o seu salário: '))
if salario > 1250:
    # novo = salario + (salario * 10 / 100)
    print('Parabéns, você receberá um aumento de R$ {:.2f} reais equivalente a 10%.'.format((salario * 0.10) + salario))
else:
    # novo = salario + (salario * 15 / 100)
    print('Parabéns, você receberá um aumento de R$ {:.2f} reais equivalente a 15%'.format((salario * 0.15) + salario))
