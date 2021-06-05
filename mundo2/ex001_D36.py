#-----EMPRESTIMO------

imovel = float(input('Qual valor do imóvel a ser financiado aproximadamente? R$ '))
salario = float(input('Qual é a sua renda familiar? R$ '))
prestacao = int(input('Quantas prestações? '))
if prestacao > 300:
    print('\033[1:30:41m As prestações devem ser menores de 25 anos \033[m')
elif (salario * 0.3) < (imovel / prestacao):
    print('\033[1:30:41m Sua renda ou prestações não são compatíveis com a modalidade de compra!'
          '\033[m')
else:
    print('\033[1:30:42m Parabéns! Seu financiamento foi aprovado. O imóvel avaliado em R$ {:.2f} reais com '
          'parcelas de R$ {:.2f} reais podendo financiar até R$ {} reais no imóvel.'
          '\033[1:30:32m'.format(imovel, (salario * 0.3), ((salario * 0.3) * prestacao)))

