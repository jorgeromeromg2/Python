#-------SISTEMA DE COMPRA COM DESCONTO------
print(10 * '--=--')
print('CONDIÇÃO ESPECIAL PARA PAGAMENTOS')
print(10 * '--=--')
nome = str(input('Digite seu nome: ')).capitalize()
valor = float(input('Digite o valor do produto: R$ '))
condicao = int(input(' 1 - dinheiro ou cheque\n 2 - cartão à vista\n '
                     '3 - cartão até 2x\n 4 - cartão 3x ou mais (com juros).\n Escolha uma opção para pagamento: '))
if condicao == 1:
    print('{}, você pagará R$ {:.2f} reais no total optando pela condição de pagamento '
          'em dinheiro ou cartão.'.format(nome, valor - (valor * 0.1)))
elif condicao == 2:
    print('{}, você pagará R$ {:.2f} reais no total optando pela condição de pagamento '
          'com cartão à vista.'.format(nome, valor - (valor * 0.05)))
elif condicao == 3:
    print('{}, você pagará R$ {:.2f} reais no total optando pela condição de pagamento '
          'em até 2x (sem juros). Seu parcelamento ficará de R$ {:.2f} reais por mês.'.format(nome, valor, valor/2))
elif condicao == 4:
    parcela = int(input('Em quantas vezes deseja parcelar: '))
    print('{}, você pagará R$ {:.2f} reais no total optando pela condição de pagamento {}x no cartão(com juros).'
          'Seu parcelamento ficará de R$ {:.2f} reais por mês.'.format(nome, valor + (valor * 20/100), parcela,
                                                                       (valor + (valor * 20/100))/parcela))
else:
    print('{}, esta opção de condição para pagamento não existente! Tente novamente.'.format(nome))